'''Manage Apache virtual hosts for Appy sites on target machines'''

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
import os
from pathlib import Path

from appy.utils.string import Variables
from appy.utils.path import getTempFileName

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Template virtual host for http (to avoid)
httpSingle = '''<VirtualHost *:80>
 ServerName |domain|
 ServerAdmin |email|
 ErrorLog ${APACHE_LOG_DIR}/error.log
 CustomLog ${APACHE_LOG_DIR}/access.log combined
 RewriteEngine on
 RewriteRule ^(.*) http://localhost:|port|$1 [P]
</VirtualHost>
<Proxy "http://localhost:|port|">
 ProxySet keepalive=On
</Proxy>'''

# Template virtual host for http (redirect to https)
http = '''<VirtualHost *:80>
 ServerName |domain|
 RedirectPermanent / https://|domain|/
</VirtualHost>'''

# Template virtual host for https
https = '''<IfModule mod_ssl.c>
 <VirtualHost _default_:443>
  ServerName |domain|
  ServerAdmin |email|
  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined
  SSLEngine on
  ProxyTimeout 10800
  SSLCertificateFile |destCert|
  SSLCertificateKeyFile |destKey|
  SSLCertificateChainFile |destChain|
  SSLCACertificateFile |destChain|
  RewriteEngine on
  RewriteRule ^(.*) http://localhost:|port|$1 [P]
 </VirtualHost>
 <Proxy "http://localhost:|port|">
  ProxySet keepalive=On
 </Proxy>
</IfModule>'''

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
APA_P_KO  = '"apache" option not applied: unknown protocol: %s.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Config:
    '''Configuration elements being requested to generate an Apache virtual
       host.'''

    # Names of the attributes storing HTTPS-related certificate files
    destAttributes = ('cert', 'key', 'chain')

    def __init__(self, email, domain, protocol='https', cert=None, key=None,
                 chain=None, destFolder='ssl'):
        # The email address identifying the software creator managing the site
        self.email = email
        # The server's domain name, as known and accessed by the end users
        self.domain = domain
        # The protocol in use between end users and the server: should be
        # 'https' and not 'http', but both are supported.
        self.protocol = protocol
        # [https] Absolute path, on your DEV machine, of the certificate file
        self.cert = str(cert) if cert else None # Could be a Path object
        # [https] Private key's absolute path
        self.key = str(key) if key else None
        # [https] Certificate chain file's absolute path
        self.chain = str(chain) if chain else None
        # [https] The name of the destination folder, within
        #         Apache.configFolder, where to copy certificate-related files.
        #         Set a simple name here, not a path.
        self.destFolder = destFolder
        # The absolute path to this folder, as a pathlib.Path object
        self.destPath = Path(Apache.configFolder) / destFolder
        # Store the absolute paths to the certificate-related files whose local
        # paths are defined in attributes "cert", "key" and "chain".
        if protocol == 'https':
            for name in self.destAttributes:
                src = getattr(self, name)
                dest = self.destPath / Path(src).name
                setattr(self, 'dest%s' % name.capitalize(), str(dest))

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Apache:
    '''Represents an Apache virtual host to create or update for some Appy site
       on some target.'''

    # The folder where virtual hosts reside
    configFolder = '/etc/apache2'
    sitesFolder = '%s/sites-enabled' % configFolder

    # Restart command
    restart = 'apache2ctl restart'

    def __init__(self, target):
        self.target = target

    def get(self, config, template):
        '''Creates, from this p_template, the content of a virtual host, and
           dump it in a temp file. The method returns the path to this temp
           file.'''
        content = Variables.replace(template, config)
        path = getTempFileName()
        with open(path, 'w') as f: f.write(content)
        return path

    def copyVirtualHost(self, type, config, target):
        '''Copy a virtual host of this p_type to the p_target'''
        # Dump the virtual host definition in a local temp file
        template = eval(type)
        localPath = self.get(config, template)
        suffix = '' if type == 'httpSingle' else ('_%s' % type)
        dest = '%s/%s%s.conf' % (Apache.sitesFolder, target.siteName, suffix)
        target.copy(localPath, dest)
        os.remove(localPath)

    def deploy(self):
        '''Creates a virtual host and deploys it (copy + configure) on
           p_self.target.'''
        target = self.target
        config = target.apache
        # Set the site port on the v_config. Else, it will not be found by the
        # code (see m_get) that must inject it into the virtual host template
        # string.
        config.port = str(target.sitePort)
        if config.protocol == 'http':
            # Create a unique http virtual host
            self.copyVirtualHost('httpSingle', config, target)
            # Restart Apache
            target.execute(Apache.restart)
        elif config.protocol == 'https':
            # Create a virtual host that will redirect http traffic to https,
            # and a second one that manages https.
            for type in ('http', 'https'):
                self.copyVirtualHost(type, config, target)
            # Copy certificate files to the target. Overwrite any existing file.
            # As a preamble, ensure the destination folder for these files
            # exist.
            target.execute('mkdir -p %s' % config.destPath)
            for name in config.destAttributes:
                dest = getattr(config, 'dest%s' % name.capitalize())
                target.copy(getattr(config, name), dest)
            # Restart Apache
            target.execute(Apache.restart)
        else:
            print(APA_P_KO % config.protocol)
            return
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
