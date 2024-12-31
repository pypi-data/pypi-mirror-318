'''Appy wrapper to Google Web Services'''

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
import urllib.parse

from appy.utils.client import Resource
from appy.model.utils import Object as O

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SV_ERR  = 'Server error: %s.'
ST_ERR  = 'Status error: %s.'
RS_ERR  = 'Resource error: %s.'
NO_KEY  = 'Google API :: No key found in config.googleApiKey'
ASK_GO  = 'Ask Google :: %s'
D_RESP  = 'Google response :: %dm.'
GA_ONE  = 'Google response :: 1 match :: %s.'
GA_MUL  = 'Google response :: %d matches.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Address:
    '''Represents an address as geolocalized by Google'''

    def __init__(self, r):
        self.address = r.formatted_address
        # Get coordinates (latitude, longitude)
        geometry = r.geometry
        # Is this an approximate result ?
        self.approximate = geometry.location_type == 'APPROXIMATE'
        # Store latitude and longitude
        location = geometry.location
        self.coordinates = location.lat, location.lng

    def __repr__(self):
        lat, lng = self.coordinates[0], self.coordinates[1]
        approx = '!approximate' if self.approximate else ''
        return f'‹Address {self.address} ({lat:.2f},{lng:.2f}){approx}›'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Google:
    '''Proxy to the Google Web Services API'''

    class Error(Exception): pass

    def __init__(self, tool):
        '''Proxy constructor'''
        self.tool = tool
        self.key = tool.config.googleApiKey
        if not self.key:
            tool.log(NO_KEY, type='warning')

    # URLs to the currently supported Google APIs
    mapsApi = 'https://maps.googleapis.com/maps/api'
    apis = O(
      geocoding=f'{mapsApi}/geocode',
      distance=f'{mapsApi}/distancematrix'
    )

    def manageError(self, message):
        '''Logs the error and raise an exception'''
        self.tool.log(message, type='error')
        raise self.Error(message)

    def call(self, url):
        '''Sends a HTTP request to Google'''
        self.tool.log(ASK_GO % url)
        server = Resource(url)
        try:
            response = server.get()
        except Resource.Error as re:
            self.manageError(RS_ERR % str(re))
        # We got a response
        if response.code != 200:
            self.manageError(SV_ERR % response.text)
        # Check the return status
        status = response.data['status']
        if status != 'OK':
            self.manageError(ST_ERR % status)
        return response.data

    def geocode(self, address, verbose=False):
        '''Returns the coordinates of some given p_address'''
        # If p_verbose is False, it returns an Address object, or a list of
        # Address objects if p_address is ambiguous and matches several
        # addresses. Else, it returns the complete data structure as described
        # in the Google API.
        if not self.key: return # Do nothing if there is no API key
        # Encode p_address
        address = urllib.parse.quote_plus(address)
        # Perform the HTTP request
        url = f'{Google.apis.geocoding}/json?address={address}&key={self.key}'
        data = self.call(url)
        # Return the complete response when required
        if verbose: return data
        # Return the coordinates and formatted addresses only
        results = data.results
        if len(results) == 1: # A single match
            r = Address(results[0])
            msg = GA_ONE % r
        else:
            r = [Address(result) for result in results]
            msg = GA_MUL % len(r)
        self.tool.log(msg)
        return r

    def distance(self, origin, destination, mode='driving', language='fr',
                 verbose=False):
        '''Returns the distance, in kms as a float, between p_origin and
           p_destination, expressed as tuples of floats:
                            ~(f_latitude, f_longitude)~.
        '''
        if not self.key: return # Do nothing if there is no API key
        # Encode parameters
        orig = str(origin)[1:-1].replace(' ', '')
        dest = str(destination)[1:-1].replace(' ', '')
        params = f'origins={orig}&destinations={dest}&mode={mode}&language=' \
                 f'{language}&key={self.key}'
        # Perform the HTTP request
        url = f'{Google.apis.distance}/json?{params}'
        data = self.call(url)
        # Return the complete response when required
        if verbose: return data
        r = data.rows[0].elements[0].distance.value
        self.tool.log(D_RESP % r)
        return r / 1000
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
