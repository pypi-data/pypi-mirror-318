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
import hashlib, copy
from appy.px import Px
from appy.utils import asDict
from appy.model.fields import Field
from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PARAM_EMPTY = 'Ogone: parameter "%s" has no value and has been ignored.'
RESP_OK     = '%d - Ogone answered: %s'
RESP_KO     = '%d - Ogone response SHA failed. Params: %s'
RESP_KO_ERR = 'An administrator has been contacted.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Config:
    '''If you plan, in your app, to perform on-line payments via the Ingenico
       ePayments e-Commerce system (previouly named Ogone), create an instance
       of this class in your app and place it in the 'ogone' attr of your app's
       Config class.'''

    # The URL to redirect the user to for performing an on-line payment
    payUrls = {
      'test': 'https://ogone.test.v-psp.com/ncol/test/orderstandard_utf8.asp',
      'prod': 'https://secure.ogone.com/ncol/prod/orderstandard_utf8.asp'
    }

    # Fields below are those that must be sent in every request to Ogone
    sendable = ('pspid', 'currency', 'language')

    # Default parameters sent back by Ingenico to your app, after a payment has
    # been performed, being part of the HTTP GET request (payment accepted,
    # refused, etc).

    # ! Compared to the predefined list as defined by Ingenico, params "CN" and
    # "BRAND" have been removed. Indeed, it may contains spaces; these spaces
    # are converted by Ingenico into + signs, but Appy does not convert them
    # back to spaces for HTTP GET requests.

    defaultBackParams = asDict(
      ('AAVCHECK', 'ACCEPTANCE', 'ALIAS', 'AMOUNT', 'CARDNO', 'CCCTY',
       'COMPLUS', 'CREATION_STATUS', 'CURRENCY', 'CVCCHECK',
       'DCC_COMMPERCENTAGE', 'DCC_CONVAMOUNT', 'DCC_CONVCCY', 'DCC_EXCHRATE',
       'DCC_EXCHRATESOURCE', 'DCC_EXCHRATETS', 'DCC_INDICATOR',
       'DCC_MARGINPERCENTAGE', 'DCC_VALIDHOURS', 'ECI', 'ED', 'IP', 'IPCTY',
       'NCERROR', 'ORDERID', 'PAYID', 'PAYIDSUB', 'PM', 'STATUS',
       'SUBSCRIPTION_ID', 'TRXDATE', 'VC')
    )

    def __init__(self):
        # self.env refers to the Ogone environment and can be "test" or "prod"
        self.env = 'test'
        # You merchant Ogone ID
        self.pspid = None
        # Default currency for transactions
        self.currency = 'EUR'
        # Default language
        self.language = 'en_US'
        # Key defined by Ingenico, available in your merchant profile on their
        # site, used as element to produce a hash when sending a payment
        # request.
        self.shaInKey = ''
        # Key that you define in your Ingenico merchant profile to check the
        # response coming back from the payment system.
        self.shaOutKey = ''
        # The following parameters must be those you have selected to be
        # included in the URLs called back to your site by Ingenico. You MUST
        # write them all in uppercase letters. If this list contains parameters
        # not being effectively sent by Ingenico, or sent with an empty value,
        # this is not a problem, they will be ignored. But if a single not-empty
        # parameter sent is not this list, the check with the SHA out key will
        # fail.
        #
        # Do NOT include parameter "SHASIGN" in these parameters
        self.backParams = Config.defaultBackParams

    def __repr__(self): return str(self.__dict__)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Ogone(Field):
    '''This field allows to perform online payments with the Ingenico ePayments
       e-Commerce system.'''

    # Some elements will be traversable
    traverse = Field.traverse.copy()

    urlTypes = ('accept', 'decline', 'exception', 'cancel')

    # Return status codes
    statuses = {
     '0': 'payment_abandoned', # Abandoned or aborted for an unknown reason
     '1': 'payment_canceled' , # Canceled by the customer
     '2': 'payment_refused'  , # Payment refused
     '5': 'payment_accepted' , # Payment authorized (in a 2-step process)
     '9': 'payment_accepted' , # Payment accepted
    }

    # The "view" and "cell" layouts are used to display a button for performing
    # an on-line payment.
    # ~
    # Note that variable "value" may not be present in the context, because, if
    # the field is shown on layout "buttons", on lists of objects, caller fields
    # like Ref calls directly field.cell instead of field.pxRender.
    view = cell = buttons = Px('''
     <!-- The form for sending the payment request to Ogone.
          Variable "value" is misused and contains payment parameters. -->

     <form var="env=config.ogone.env; label=_('pay')"
           method="post" id="form1" name="form1"
           action=":config.ogone.payUrls[env]" class="inline">

       <!-- The list of hidden fields required by Ogone -->
       <input type="hidden" for="key,val in value.items()"
              id=":key" name=":key" value=":val"/>

       <!-- Submit button on most layouts -->
       <input if="layout != 'view'" type="submit" id="submit2" name="submit2"
              value=":label" class="button buttonSmall pay"
              style=":svg('pay', bg='18px 18px')"/>

       <!-- Submit picto -->
       <x if="layout == 'view'">
        <input type="image" id="submit2" name="submit2" src=":svg('pay')"
               value=":label" class="pictoC" title=":label"/>
        <div align="center">:label</div>
       </x>
     </form>''',

     css='''.pay { border-bottom: 2px solid darkorange !important;
                   font-weight: bold }''')

    edit = search = ''

    def __init__(self, orderMethod, responseMethod, show='view',
      renderable=None, page='main', group=None, layouts=None, move=0,
      readPermission='read', writePermission='write', width=None, height=None,
      colspan=1, master=None, masterValue=None, focus=False, mapping=None,
      generateLabel=None, label=None, view=None, cell=None, buttons=None,
      edit=None, custom=None, xml=None, translations=None):
        # Call the base constructor
        super().__init__(None, (0,1), None, None, show, renderable, page, group,
          layouts, move, False, True, None, None, False, None, readPermission,
          writePermission, width, height, None, colspan, master, masterValue,
          focus, False, mapping, generateLabel, label, None, None, None, None,
          False, False, view, cell, buttons, edit, custom, xml, translations)
        # orderMethod must contain a method returning a dict containing info
        # about the order. Following keys are mandatory, among others:
        #   * orderID   An identifier for the order. Don't use the object ID
        #               for this, use a random number, because if the payment
        #               is canceled, Ogone will not allow you to reuse the same
        #               orderID for the next tentative.
        #   * amount    An integer representing the price for this order,
        #               multiplied by 100 (no floating point value, no commas
        #               are tolerated. Dont't forget to multiply the amount by
        #               100!
        # Check Ingenico's doc to determine the complete list of parameters to
        # define. You can use any (upper/lower/camel)case for parameter's names:
        # they will be upperized when sent to Ingenico.
        self.orderMethod = orderMethod
        # responseMethod must contain a method accepting a single parameter. The
        # method will be called when we will get Ogone's response about the
        # status of the payment. The single param is an object whose attributes
        # correspond to all parameters that you have chosen to receive in your
        # Ogone merchant account. Consult their documentation for details. The
        # method must return a tuple (url, message):
        # - url     is the URL to redirect the user to. If None, it will be the
        #           current object's view page. After the payment, the user will
        #           be redirected to that URL.
        # - message is a translated message that will be shown to the user, on
        #           "url". The following standard Appy i18n labels can be used
        #           or overridden to produce this message: "payment_accepted",
        #           "payment_refused", "payment_canceled" and
        #           "payment_abandoned".
        self.responseMethod = responseMethod

    # The Ogone field can a priori be shown on every layout, "buttons" included
    def isRenderableOn(self, layout): return layout != 'query'

    def createShaDigest(self, values, passphrase):
        '''Creates an Ogone-compliant SHA-512 digest based on key-value pairs in
           dict p_values and on some p_passphrase.'''
        # Create a sorted list of keys
        keys = list(values.keys())
        keys.sort()
        r = []
        for key in keys:
            r.append(f'{key}={values[key]}')
        r = (passphrase.join(r) + passphrase).encode()
        return hashlib.sha512(r).hexdigest()

    def getValue(self, o, name=None, layout=None, single=None, at=None):
        '''The "value" of the Ogone field is a dict that collects all the
           necessary info for making the payment.'''
        tool = o.tool
        # Get base parameters from the Ogone config object
        cfg = o.config.ogone
        r = O()
        for name in cfg.sendable:
            setattr(r, name.upper(), getattr(cfg, name))
        inKey = cfg.shaInKey
        # Add dynamic parameters (order ID, amount, client information...)
        for name, value in self.callMethod(o, self.orderMethod).items():
            # Ignore any empty parameter
            if value is None: 
                o.log(PARAM_EMPTY % name)
                continue
            # Convert the value to a str if it is not the case
            if not isinstance(value, str):
                value = str(value).strip()
            # Ignore any empty parameter
            if not value: 
                o.log(PARAM_EMPTY % name)
                continue
            # Store the parameter
            setattr(r, name.upper(), value)
        # Add standard back URLs
        r.CATALOGURL = r.HOMEURL = o.siteUrl
        # Add redirect URLs
        for t in self.urlTypes:
            setattr(r, f'{t}url'.upper(), f'{o.url}/{self.name}/process')
        # Compute a SHA-512 key as required by Ogone and add it to the result
        r.SHASIGN = self.createShaDigest(r, inKey)
        return r

    def ogoneResponseOk(self, ogoneSign, outKey, params):
        '''Returns True if the SHA-512 signature from Ogone matches retrieved
           params.'''
        digest = self.createShaDigest(params, outKey)
        return digest.lower() == ogoneSign.lower()

    def getBackParameters(self, req, configParams):
        '''Extracts, from the request, Ingenico-related parameters'''
        r = O()
        for name, value in req.items():
            # Upperize the name of the parameter
            name = name.upper()
            # Keep it only if mentioned in the config and not empty
            if not value or name not in configParams: continue
            setattr(r, name, value)
        return r

    traverse['process'] = 'perm:read'
    def process(self, o):
        '''Processes a response from Ogone'''
        # Get parameters from the request sent back by Ingenico
        cfg = o.config.ogone
        req = o.req
        params = self.getBackParameters(req, cfg.backParams)
        sparams = str(params)
        # Log and check the response
        if not self.ogoneResponseOk(req.SHASIGN, cfg.shaOutKey, params):
            o.log(RESP_KO % (o.iid, sparams))
            raise Exception(RESP_KO_ERR)
        o.log(RESP_OK % (o.iid, sparams))
        # Handle the Ogone response by calling the response method defined in
        # this Ogone field, and redirect the user to the correct page. If the
        # field method returns some URL, use it. Else, use the p_o's view URL.
        url, message = self.responseMethod(o, params)
        url = url or o.url
        o.H().commit = True
        o.goto(url, message)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
