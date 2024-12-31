#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Copyright (C) 2007-2024 Gaetan Delannay

# This file is part of Appy.

# Appy is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# Appy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# Appy. If not, see <http://www.gnu.org/licenses/>.

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from pathlib import Path
from base64 import encodebytes
import xml.sax, http.client, urllib.parse, ssl
import re, io, time, socket, random, hashlib, gzip

from appy.utils import json, copyData
from appy.utils import path as putils
from appy.model.utils import Object as O
from appy.xml.marshaller import Marshaller
from appy.xml.unmarshaller import Unmarshaller

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DUR_SECS  = ', got in %.4f seconds'
RESP_T    = '\n*Headers* %s\n*Body* %s\n'
RESP_R    = '‹HttpResponse %s (%s)%s%s›'
D_ERR     = 'Distant server exception: %s'
XML_ERR   = 'Invalid XML response (%s)'
T_OUT_ERR = 'Timed out after %d second(s).'
RESS_R    = '‹Resource at %s›'
CIC_ERR   = 'Check your Internet connection (%s)'
CONN_ERR  = 'Connection error (%s)'
URL_ERR   = 'Wrong URL: %s'
ENC_ERR   = 'Cannot encode value %s'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class FormDataEncoder:
    '''Encode form data for sending it through a HTTP POST request'''

    def __init__(self, data):
        self.data = data # The data to encode, as a dict

    def marshalValue(self, name, value):
        if isinstance(value, str):
            r = f'{name}={urllib.parse.quote(value)}'
        elif isinstance(value, float):
            r = f'{name}:float={value}'
        elif isinstance(value, int):
            r = f'{name}:int={value}'
        elif isinstance(value, long):
            r = f'{name}:long={value}'
            if r[-1] == 'L':
                r = r[:-1]
        else:
            raise Exception(ENC_ERR % str(value))
        return r

    def getSep(self):
        '''Returns the separator to use between data attributes'''
        return b'&'

    def encode(self):
        '''Encodes all values from p_self.data as bytes'''
        r = []
        for name, value in self.data.items():
            val = self.marshalValue(name, value)
            if not isinstance(val, bytes):
                val = val.encode()
            r.append(val)
        return self.getSep().join(r)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class FormMultiEncoder(FormDataEncoder):
    '''Encode form data in multipart format'''

    # Parameters for creating a boundary
    dashCount = 27
    numbersCount = 25

    # Part of the boundary separator
    subSep = '\r\n'

    # Base template for any value
    anyValue = f'Content-Disposition: form-data; name="%s"'

    # Template for a basic value
    basicValue = f'{anyValue}{subSep}{subSep}%s'

    # Template for file content
    fileValue = f'{anyValue}; filename="%s"{subSep}Content-Type: %s' \
                f'{subSep}{subSep}%s'

    def __init__(self, data):
        super().__init__(data)
        # Define a boundary for separating form data
        self.boundary = self.defineBoundary()

    def defineBoundary(self):
        '''Generates a boundary in p_self.boundary'''
        # Start with dashes
        dashes = '-' * self.dashCount
        # End with a random figure
        figures = []
        i = 0
        while i < self.numbersCount:
            figures.append(str(random.randint(0,9)))
            i += 1
        return f'{dashes}{"".join(figures)}'

    def getSep(self):
        '''The attributes separator, for a multi-form encoder, is the
           boundary.'''
        sep = self.subSep
        return f'{sep}--{self.boundary}{sep}'.encode()

    def marshalValue(self, name, value):
        '''Marshalls attribute having this p_name and p_value'''
        if isinstance(value, io.BufferedReader):
            # A file
            path = Path(value.name)
            fileName = path.name
            mimeType = putils.guessMimeType(path)
            # Create, directly as bytes, the chunk of data containing the file's
            # metadata and its content.
            base = self.fileValue.encode()
            r = base % (name.encode(), fileName.encode(), mimeType.encode(),
                        value.read())
            # Now that file content has been read, close it
            value.close()
        else:
            # Any other type of content
            r = self.basicValue % (name, str(value))
        return r

    def encode(self):
        '''Dumps all field values sequentially, then add the boundary as
           prologue and epilogue.'''
        r = super().encode()
        # Add the prologue and epilogue
        sep = self.getSep()
        prologue = sep[2:]
        epilogue = sep[:-2] + b'--\r\n'
        return b''.join([prologue, r, epilogue])

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class SoapDataEncoder:
    '''Allows to encode SOAP data for sending it through a HTTP request'''

    namespaces = {'s'  : 'http://schemas.xmlsoap.org/soap/envelope/',
                  'xsd': 'http://www.w3.org/2001/XMLSchema',
                  'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}

    namespacedTags = {'Envelope': 's', 'Body': 's', '*': 'py'}

    def __init__(self, data, namespace='https://appyframe.work'):
        self.data = data
        # p_data can be:
        # - a string already containing a complete SOAP message
        # - a Python object, that we will convert to a SOAP message
        # Define the namespaces for this request
        self.ns = self.namespaces.copy()
        self.ns['py'] = namespace

    def encode(self):
        # Do nothing if we have a SOAP message already
        if isinstance(self.data, str):
            r = self.data
        else:
            # self.data is here a Python object. Wrap it in a SOAP Body.
            soap = O(Body=self.data)
            # Marshall it
            marshaller = Marshaller(rootTag='Envelope', namespaces=self.ns,
                                    namespacedTags=self.namespacedTags)
            r = marshaller.marshall(soap)
        return r.encode()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class DigestRealm:
    '''Represents information delivered by a server requiring Digest-based
       HTTP authentication.'''

    rex = re.compile(r'(\w+)="(.*?)"')

    # List of attributes whose values must not be quoted
    unquoted = ('algorithm', 'qop', 'nc')

    def md5(self, value):
        '''Produces the MD5 message digest for p_value, as a hexadecimal
           32-chars string.'''
        return hashlib.md5(str(value).encode()).hexdigest()

    def __init__(self, info):
        '''p_info is the content of header key WWW-Authenticate. This
           constructor parses it and unwraps data into self's attributes.'''
        for name, value in self.rex.findall(info):
            # For attribute "qpop", split values into a list
            if name == 'qop':
                value = value.split(',')
                for i in range(len(value)):
                    value[i] = value[i].strip()
            setattr(self, name, value)
        # Set some default values
        if not hasattr(self, 'algorithm'):
            self.algorithm = 'MD5'

    def buildCredentials(self, resource, uri, httpMethod='GET'):
        '''Builds credentials to transmit to the server'''
        login = resource.username
        realm = self.realm
        algorithm = self.algorithm
        nonce = self.nonce
        # Get the "path" part of the URI
        parsed = urllib.parse.urlparse(uri).path
        # Compute a client random nouce
        cnonce = self.md5(random.random())
        # Collect credentials info in a dict
        r = {'username': login, 'uri': uri, 'realm': realm, 'nonce': nonce,
             'algorithm': algorithm}
        # Add optional attribute "opaque"
        if hasattr(self, 'opaque'): r['opaque'] = self.opaque
        # Precompute the "HA1" part of the response, that depends on the
        # algorithm in use (MD5 or MD5-sess).
        ha1 = self.md5(f'{login}:{realm}:{resource.password}')
        if algorithm == 'MD5-sess':
            ha1 = self.md5(f'{ha1}:{nonce}:{cnonce}')
        # Take into account the quality of protection (qop)
        hasQop = hasattr(self, 'qop')
        if hasQop:
            qop = r['qop'] = self.qop[0]
            r['cnonce'] = cnonce
            r['nc'] = '00000001'
        else:
            qop = 'auth'
        # Precompute the "HA2" part of the response, that depends on qop
        if qop == 'auth-int':
            entity = self.md5('entity')
            ha2 = self.md5(f'{httpMethod}:{uri}:{entity}')
        else:
            ha2 = self.md5(f'{httpMethod}:{uri}')
        # Compute the complete response
        if hasQop:
            response = self.md5(f'{ha1}:{nonce}:{r["nc"]}:{cnonce}:{qop}:{ha2}')
        else:
            response = self.md5(f'{ha1}:{nonce}:{ha2}')
        r['response'] = response
        # Convert the dict to a formatted list, quoting values when relevant
        attrs = []
        for name, value in r.items():
            if name not in self.unquoted:
                value = f'"{value}"'
            attrs.append(f'{name}={value}')
        # Produce the final value
        attrs = ', '.join(attrs)
        return f'Digest {attrs}'

    def __repr__(self):
        '''p_self's short string representation'''
        pairs = ','.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'<Realm {pairs}>'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class HttpResponse:
    '''Stores information about a HTTP response'''

    # Useful empty dict
    emptyDict = {}

    # Redirect HTTP codes
    redirectCodes = (301, 302, 303)

    def __init__(self, resource, response, body, duration=None, utf8=True,
                 forcedResponseType=None, unmarshallParams=None):
        self.resource = resource
        self.code = response.status # The return code, ie 404, 200, 500...
        self.text = response.reason # Textual description of the code
        self.headers = response.msg # A dict-like object containing the headers
        self.body = body # The body of the HTTP response
        # p_duration, if given, is the time, in seconds, we have waited, before
        # getting this response after having sent the request.
        self.duration = duration
        self.utf8 = utf8
        # If data must be unmarshalled, customizing the unmarshalling process
        # can be done by specifying a dict of p_unmarshallParams.
        self.unmarshallParams = unmarshallParams
        # The following attribute may contain specific data extracted from
        # the previous fields. For example, when response if 302 (Redirect),
        # self.data contains the URI where we must redirect the user to.
        self.data = self.extractData(forcedResponseType)
        self.response = response

    def __repr__(self, complete=False):
        '''p_self's short string representation'''
        duration = suffix = ''
        if self.duration: duration = DUR_SECS % self.duration
        if complete:
            suffix = RESP_T % (str(self.headers), str(self.body))
        return RESP_R % (self.code, self.text, duration, suffix)

    def get(self): return self.__repr__(complete=True)

    def getResponseUrl(self, url):
        '''In the context of a 303 Redirect request, get the complete p_url to
           redirect to.'''
        if self.resource.redirectSame:
            # Re-build p_url based on p_self.host, in order to ensure we stay on
            # the same site.
            parts = urllib.parse.urlparse(url)
            r = parts.path or '/'
            if parts.query:
                r = f'{r}?{parts.query}'
        else:
            # Keep p_url as is
            r = url
        return r

    def extractContentType(self, contentType):
        '''Extract the content type from the HTTP header, potentially removing
           encoding-related data.'''
        i = contentType.find(';')
        if i != -1: return contentType[:i]
        return contentType

    def extractCookies(self, headers):
        '''Extract received cookies and put them in self.resource.headers'''
        if 'Set-Cookie' not in headers: return
        # Several "Set-Cookie" can be returned by the server, so do not access
        # the dict-like p_headers, into which only the first "Set-Cookie" will
        # be present: access the underlying p_headers._headers tuple.
        for key, value in headers._headers:
            if key != 'Set-Cookie': continue
            cookie = value.split(';')[0]
            name, value = cookie.split('=', 1)
            # Delete the cookie if it has expired
            if value.strip('"') == 'deleted':
                # Do not set this cookie, and remove it if already present
                if name in self.resource.cookies:
                    del self.resource.cookies[name]
            else:
                self.resource.cookies[name] = value

    xmlHeaders = ('text/xml', 'application/xml', 'application/soap+xml')

    def extractData(self, forcedResponseType=None):
        '''Extracts, from the various parts of the HTTP response, some useful
           information.'''
        #
        # - Find the URI where to redirect the user to if self.code is 302 or
        #   303;
        # - Return authentication-related data, if present, if self.code is 401;
        # - Unmarshall XML or JSON data into Python objects;
        # - etc
        #
        # Extract information from HTTP headers when relevant
        headers = self.headers
        self.extractCookies(headers)
        if self.code in self.redirectCodes:
            # The URL to redirect to is in header key 'location'
            return self.getResponseUrl(headers['location'])
        elif self.code == 401:
            authInfo = headers.get('WWW-Authenticate')
            return authInfo and DigestRealm(authInfo) or None
        # Determine the response type from the HTTP response or use this
        # p_forcedResponseType if passed. Forcing a response type may prevent to
        # parse the response when it is not needed. For example, suppose you
        # want to store the content of a JSON resource to a file on disk. If you
        # force the response type to "text", you will disable the JSON parsing
        # and simply get, as raw text, the JSON content in the response body.
        responseType = forcedResponseType or headers.get('Content-Type')
        if not responseType: return
        # Apply some transform on the response content depending on its type
        contentType = self.extractContentType(responseType)
        # Manage JSON content
        if contentType == 'application/json':
            return json.Decoder.decode(self.body)
        # Manage XML content
        for xmlHeader in self.xmlHeaders:
            # Ensure this is XML
            if not contentType.startswith(xmlHeader): continue
            # Return an unmarshalled version of the XML content, for easy use
            try:
                params = self.unmarshallParams or HttpResponse.emptyDict
                parser = Unmarshaller(**params)
                r = parser.parse(self.body)
                if parser.rootTag == 'exception':
                    # This is an exception: v_r contains the traceback
                    raise Resource.Error(D_ERR % r)
                return r
            except xml.sax.SAXParseException as se:
                raise Resource.Error(XML_ERR % str(se))

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
urlRex = re.compile(r'(http[s]?)://([^:/]+)(:[0-9]+)?(/.+)?', re.I)
binaryRex = re.compile(r'[\000-\006\177-\277]')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Resource:
    '''Every instance of this class represents some web resource accessible
       through HTTP.'''

    class Error(Exception): pass

    # Standard ports, by protocol
    standardPorts = {'http': 80, 'https': 443}

    def __init__(self, url, username=None, password=None, token=None,
                 measure=False, utf8=True, authMethod='Basic', timeout=10,
                 redirectSame=False):
        # The base URL corresponding to the distant resource
        self.url = url
        # A p_username and p_password must be passed when using Basic auth.
        self.username = username
        self.password = password
        # A p_token must be passed when using Bearer auth.
        self.token = token
        # Authentication method can be: "Basic", "Digest" or "Bearer"
        self.authMethod = authMethod
        # If p_measure is True, we will measure, for every request sent, the
        # time we wait until we receive the response.
        self.measure = measure
        # Default encoding is UTF-8
        self.utf8 = utf8
        # A timeout (in seconds) used when sending blocking requests to the
        # resource.
        self.timeout = timeout
        # When redirecting to some URL after receiving a "303 Redirect"
        # response, if p_redirectSame is False, the redirect URL, as transmitted
        # in the "Location" HTTP header, will be used as is. If p_redirectSame
        # is True, we will build the redirect URL by using p_self.host (see
        # below) and the "path" part coming from the Location HTTP header. This
        # approach is more secure and ensures a site doesn't redirect you to
        # another one. However, it is not configured by default because it may
        # lead to problems in the context of peer sites communication, when
        # these peers can be accessed via different host names.
        self.redirectSame = redirectSame
        # If measure is True, we will store hereafter, the total time (in
        # seconds) spent waiting for the server for all requests sent through
        # this resource object.
        self.serverTime = 0
        # Split the URL into its components
        self.protocol, self.host, self.port, self.path = self.getUrlParts(url)
        # If some headers must be sent with any request sent through this
        # resource, you can store them in the following dict.
        self.headers = {'User-Agent': 'Appy', 'Connection': 'close',
                        'Accept': '*/*', 'Accept-Encoding': 'gzip, identity'}
        # Cookies defined hereafter will be included in self.headers at every
        # request.
        self.cookies = {}

    def getUrlParts(self, url, raiseOnError=True):
        '''Return p_url parts as a tuple (protocol, host, port, path). If the
           URL is wrong (or is not a complete URL), the method raises an error
           if p_raiseOnError is True or returns None if p_raiseOnError is
           False.'''
        r = urlRex.match(url)
        if not r:
            if raiseOnError:
                raise Resource.Error(URL_ERR % str(url))
            else:
                return r
        protocol, host, port, path = r.groups()
        if port:
            port = int(port[1:])
        else:
            port = Resource.standardPorts[protocol]
        path = path or '/'
        return protocol, host, port, path

    def getHeaderHost(self, protocol, host, port):
        '''Gets the content of header key "Host"'''
        # Insert the port number if not standard
        suffix = '' if port == Resource.standardPorts[protocol] else f':{port}'
        return f'{host}{suffix}'

    def __repr__(self):
        '''p_self's short string representation'''
        return RESS_R % self.url

    def completeHeaders(self, headers):
        '''Complete the specified p_headers with mandatory headers'''
        # Get standard header values from self.headers if not defined in
        # p_headers.
        if self.headers:
            for k, v in self.headers.items():
                if k not in headers:
                    headers[k] = v
        # Add cookies
        if self.cookies:
            cookiesL = [f'{k}={v}' for k, v in self.cookies.items()]
            headers['Cookie'] = '; '.join(cookiesL)
        # Add credentials-related headers when relevant
        if 'Authorization' in headers: return
        method = self.authMethod
        if method == 'Basic':
            if self.username and self.password:
                creds = f'{self.username}:{self.password}'.encode()
                credsD = encodebytes(creds).strip().decode()
                authorization = f'{method} {credsD}'
                headers['Authorization'] = authorization
        elif method == 'Bearer':
            if self.token:
                headers['Authorization'] = f'{method} {self.token}'

    def readResponse(self, response):
        '''Reads the response content. Unzip the result when appropriate'''
        headers = response.headers
        if headers.get('Content-Encoding') == 'gzip':
            # Unzip the content
            f = gzip.GzipFile(fileobj=response)
        else:
            f = response
        # Read response bytes
        r = f.read()
        # Decode the response when relevant
        contentType = headers.get('Content-Type')
        if contentType and contentType.startswith('image/'):
            pass # No need to decode it
        else:
            try:
                r = r.decode()
            except UnicodeDecodeError:
                pass
        return r

    def send(self, method, path, body=None, headers=None, bodyType=None,
             forcedResponseType=None, unmarshallParams=None, timeout=None):
        '''Sends a HTTP request with p_method, @ this p_path'''
        # p_path can be a complete URL (http://a.b.be/c) or the "path "part (/c)
        parts = self.getUrlParts(path, raiseOnError=False)
        if parts is None:
            # p_path is a real path
            protocol, host, port = self.protocol, self.host, self.port
            path = path or '/'
        else:
            # p_path is a complete URL
            protocol, host, port, path = parts
        # Initialise a HTTP or HTTPS connection
        hc = http.client
        timeout = self.timeout if timeout is None else timeout
        if protocol == 'https':
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = hc.HTTPSConnection(host, port, timeout=timeout,
                                      context=context)
        else:
            conn = hc.HTTPConnection(host, port, timeout=timeout)
        try:
            conn.connect()
        except socket.gaierror as sge:
            raise self.Error(CIC_ERR % str(sge))
        except socket.timeout as se:
            raise self.Error(T_OUT_ERR % conn.timeout)
        except socket.error as se:
            raise self.Error(CONN_ERR % str(se))
        # Tell what kind of HTTP request it will be
        conn.putrequest(method, path, skip_host=True)
        # Add HTTP headers
        if headers is None: headers = {}
        headers['Host'] = self.getHeaderHost(protocol, host, port)
        self.completeHeaders(headers)
        for k, v in headers.items(): conn.putheader(k, v)
        conn.endheaders()
        # Add HTTP body
        if body:
            copyData(body, conn, 'send', type=bodyType or 'string')
        # Send the request, get the reply
        if self.measure: startTime = time.time()
        try:
            response = conn.getresponse()
        except socket.timeout as te:
            raise self.Error(T_OUT_ERR % conn.timeout)
        if self.measure: endTime = time.time()
        body = self.readResponse(response)
        conn.close()
        # Return a smart object containing the various parts of the response
        duration = None
        if self.measure:
            duration = endTime - startTime
            self.serverTime += duration
        return HttpResponse(self, response, body, duration=duration,
                 utf8=self.utf8, forcedResponseType=forcedResponseType,
                 unmarshallParams=unmarshallParams)

    def get(self, path=None, headers=None, params=None, followRedirect=True,
            forcedResponseType=None, unmarshallParams=None, timeout=None):
        '''Perform a HTTP GET on the server'''
        # Parameters can be given as a dict in p_params. p_forcedResponseType,
        # if passed, will be used instead of the "Content-Type" key as found in
        # the HTTP response. In the processs of unmarshalling received data,
        # specific parameters can be passed in dict p_unmarshallParams.
        path = path or self.path
        # Encode and append params if given
        if params:
            sep = '&' if '?' in path else '?'
            paramsE = urllib.parse.urlencode(params)
            path = f'{path}{sep}{paramsE}'
        r = self.send('GET', path, headers=headers,
                      forcedResponseType=forcedResponseType,
                      unmarshallParams=unmarshallParams, timeout=timeout)
        # Follow redirect when relevant
        if r.code in r.redirectCodes and followRedirect:
            # Addition durations when "measure" is True
            duration = r.duration
            r = self.get(r.data, headers=headers, timeout=timeout)
            if self.measure: r.duration += duration
            return r
        # Perform Digest-based authentication when relevant
        if r.code == 401 and self.authMethod == 'Digest' and r.data:
            # Re-trigger the request with the correct authentication headers
            headers = headers or {}
            headers['Authorization'] = r.data.buildCredentials(self, path)
            return self.get(path=path, headers=headers, params=params,
                            followRedirect=followRedirect,
                            forcedResponseType=forcedResponseType,
                            timeout=timeout)
        return r
    rss = get

    def post(self, data=None, path=None, headers=None, encode='form',
             followRedirect=True, timeout=None):
        '''Perform a HTTP POST on the server'''
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # If p_encode | It means that ...
        # is ...      |
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "form"      | the method of encoding will be:
        #             |        application/x-www-form-urlencoded
        #             | and p_data must be a dict containing for parameters as
        #             | key/value pairs ;
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # "multi"     | the method of encoding will be:
        #             |            multipart/form-data
        #             | and p_data must be a dict containing for parameters as
        #             | key/value pairs. If you want to pass a binary file as
        #             | parameter, the value of the corresponding entry in
        #             | p_data must be an open file handler, opened with
        #             | attributes "rb" (="read binary"). This p_post method
        #             | will close every such file handler after reading the
        #             | file content.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # None        | the caller is supposed to have prepared everything prior
        #             | to calling this p_post method; p_data is supposed to be
        #             | a ready-to-send request body, as bytes or string, and
        #             | the Content-Type header is supposed to be filled by the
        #             | caller as well.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        path = path or self.path
        if headers is None: headers = {}
        # Prepare the data to send
        if encode == 'form':
            # Format the form data and prepare headers
            body = FormDataEncoder(data).encode()
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        elif encode == 'multi':
            encoder = FormMultiEncoder(data)
            headers['Content-Type'] = f'multipart/form-data; ' \
                                      f'boundary={encoder.boundary}'
            body = encoder.encode()
        else:
            body = data if isinstance(data, bytes) else data.encode()
        headers['Content-Length'] = str(len(body))
        r = self.send('POST', path, headers=headers, body=body, timeout=timeout)
        if r.code in r.redirectCodes and followRedirect:
            # Update headers
            for key in ('Content-Type', 'Content-Length'):
                if key in headers: del headers[key]
            # Addition durations when "measure" is True
            duration = r.duration
            r = self.get(r.data, headers=headers, timeout=timeout)
            if self.measure: r.duration += duration
        return r

    def soap(self, data, path=None, headers=None, namespace=None,
             soapAction=None):
        '''Sends a SOAP message to this resource. p_namespace is the URL of the
           server-specific namespace. If header value "SOAPAction" is different
           from self.url, specify it in p_soapAction.'''
        path = path or self.path
        # Prepare the data to send
        data = SoapDataEncoder(data, namespace).encode()
        if headers is None: headers = {}
        headers['SOAPAction'] = soapAction or self.url
        # Content-type could be 'text/xml'
        headers['Content-Type'] = 'application/soap+xml;charset=UTF-8'
        r = self.post(data, path, headers=headers, encode=None)
        # Unwrap content from the SOAP envelope
        if hasattr(r.data, 'Body'):
            r.data = r.data.Body
        return r
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
