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
from persistent.mapping import PersistentMapping

from appy.px import Px
from appy.model.base import Base
from appy.model.fields import Show
from appy.xml.escape import Escape
from appy.utils import formatNumber
from appy.utils.google import Google
from appy.model.utils import Object as O
from appy.model.fields.float import Float
from appy.model.fields.group import Group
from appy.model.fields.string import String
from appy.ui.layout import Layouts, LayoutF
from appy.model.fields.boolean import Boolean
from appy.model.workflow.standard import Owner
from appy.model.fields.computed import Computed

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
mappingTypes = (dict, PersistentMapping)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Place(Base):
    '''Represents a place on earth + a wrap to the Google Maps API'''

    workflow = Owner
    # Places are not indexed by default
    indexable = False
    listColumns = ('title', 'street', 'number', 'box', 'zip', 'city', 'country')
    selectColumns = ('title', 'address')

    # Fields in the main page are rendered in a grid group
    mainGroup = Group('main', ['15%','85%'], style='grid', hasLabel=False)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                 Title
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @staticmethod
    def update(class_):
        '''Configures the title'''
        title = class_.fields['title']
        title.layouts = Layouts.g
        title.group = Place.mainGroup

    @classmethod
    def getGeolocIcon(class_, o):
        '''Returns an icon if p_o has been geolocalized'''
        if not o.geolocalized: return
        text = o.translate('Place_geolocalized')
        return f'<span class="help" title="{text}">📌</span>'

    def getSupTitle(self, nav):
        '''Display a special icon if p_self was successfully geolocalized'''
        return Place.getGeolocIcon(self)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                        Address (postal or virtual)
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    addressGroup = Group('address', group=mainGroup, label='Place')

    # Is this place a physical place or a virtual one ?
    virtual = Boolean(group=addressGroup, label='Place',
                      layouts=Layouts(edit=LayoutF('fl', css='placE'),
                                      view=LayoutF('lf')))

    ga = {'group': addressGroup, 'placeholder': True, 'historized': True,
          'layouts': Layouts(edit=LayoutF('frv='), view=LayoutF('lf_')),
          'multiplicity': (1,1), 'label': 'Place'}

    gp = {'master': virtual, 'masterValue': False}

    # Sub-group with street, number, box
    ga['group'] = Group('address1', ['']*3, hasLabel=False, wide=False,
                        align='left', group=ga['group'], **gp)
    street = String(**ga)
    number = String(width=3, **ga)
    del ga['multiplicity']
    box = String(width=3, **ga)

    # Sub-group with postal code and city
    ga['group'] = Group('address2', ['']*2, hasLabel=False, wide=False,
                        align='left', group=ga['group'].group, **gp)
    zip = String(multiplicity=(1,1), width=6, **ga)
    city = String(multiplicity=(1,1), **ga)

    # Country
    ga['group'] = ga['group'].group
    ga.update(gp)
    country = String(**ga)

    # Add fields composing the postal address
    postalFields = ('street', 'number', 'box', 'zip', 'city', 'country')

    # URL (for a virtual address)
    placeUrl = String(validator=String.URL, master=virtual, masterValue=True,
                      label='Place', group=addressGroup, width=60)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                        Full address (computed)
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @classmethod
    def getAddress(class_, o, line=None, includeCountry=False, empty='-',
                   sep=', ', sepN=', ', sepB='/', sepC=', '):
        '''Compute p_o's full address as a one-line string if p_line is None,
           or return only the line numbered p_line else. p_line can be:
             1     Street, number, box
             2     Postal code, city[, country]
        '''
        if not o: return empty
        # Return the place URL if the address is relative
        if getattr(o, 'virtual', None): return o.placeUrl or empty
        # A word about separators. Every separator is a string.
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  sep | The separator between lines 1 and 2
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # sepN | The separator between street and *N*umber
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # sepB | The separator between street number and *B*ox
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # sepC | The separator between line 2 and *C*ountry
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Instead of being an Appy objet, p_o may also be a (persistent) dict.
        # In that case, dict keys must correspond to the standard address-based
        # fields.
        o = O(**o) if isinstance(o, mappingTypes) else o
        # Return the p_empty string if address is empty
        street = o.street
        if not street: return empty
        # Compute line 1
        if line != 2:
            nb = o.number
            number = f'{sepN}{nb}' if nb else ''
            line1 = f'{street}{number}'
            box = o.box
            if box: line1 += f'{sepB}{box}'
            if line == 1: return line1
        # Compute line 2
        line2 = o.zip or ''
        city = o.city
        if city:
            line2 = f'{line2} {city}' if line2 else city
        if includeCountry:
            country = o.country
            if country:
                line2 = f'{line2}{sepC}{country}' if line2 else country
        if line == 2: return line2
        # If we are here, return both
        return f'{line1}{sep}{line2}' if line2 else line1

    address = Computed(method=lambda o:Place.getAddress(o), show='result',
                       plainText=True, label='Place')

    @classmethod
    def getNamedAddress(class_, o, sep='<br/>', escape=True):
        '''Get p_o's address, prefixed with its name (=p_o.title)'''
        r = class_.getAddress(o)
        if escape:
            r = Escape.xhtml(r)
        name = getattr(o, 'title', '')
        if name:
            name = Escape.xhtml(name) if escape else name
            r = f'{name}{sep}{r}'
        return r

    @classmethod
    def cleanPostal(class_, o):
        '''Deletes any data related to the postal address'''
        for name in class_.postalFields:
            setattr(o, name, None)

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                        Latitude & longitude
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def showCoordinates(self):
        '''Show latitude and longitude only if not empty'''
        val = self.latitude
        return None if val is None else Show.E_

    ll = {'show': showCoordinates, 'group': mainGroup, 'label': 'Tool'}
 
    latitude = Float(**ll)
    longitude = Float(**ll)

    # Has Google successfully geolocalized the address ? If yes, fields
    # "latitude" and "longitude" are filled.
    geolocalized = Boolean(default=False, show=False, label='Tool')

    # All geolocalzation-related fields
    geoFields = ('latitude', 'longitude', 'geolocalized')

    @classmethod
    def cleanGeo(class_, o):
        '''Clean geolocalized data on p_o'''
        values = o.values
        for name in class_.geoFields:
            if name in values:
                del values[name]

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                         Geolocalize (geocode)
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @classmethod
    def geolocalize(class_, o):
        '''Contact Google Maps to try to geolocalize o's address, getting is
           longitude and latitude in its homonym fields.'''
        # This method is a class method: that way, it can be used by other
        # objects than Place objects, provided they contain the same fields.
        #
        # Get the address as a one-line Google-API-compliant address
        address = class_.getAddress(o, sep=' ', sepN=' ', sepB=' ', sepC=' ',
                                    includeCountry=True)
        # Call the service
        api = Google(o.tool)
        r = api.geocode(address)
        # Clean any geolocalization-related data if there was a problem or the
        # address is not found, ambiguous or is an approximation.
        if not r or isinstance(r, list) or r.approximate:
            class_.cleanGeo(o)
        else:
            # A single, unambiguous address
            o.latitude, o.longitude = r.coordinates
            o.geolocalized = True

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                   Compute distance between 2 geocodes
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    @classmethod
    def distanceBetween(class_, o, p, mode='driving', language='fr'):
        '''Computes and returns the distance, in kilometers (as an integer),
           between p_o and p_p.'''
        # p_o and p_p can be something else than Place objects, but must each
        # have float attributes named "latitude" and "longitude", as computed by
        # m_geolocalize.
        #
        # Call the service
        api = Google(o.tool)
        return api.distance((o.latitude, o.longitude),
                            (p.latitude, p.longitude),
                            mode=mode, language=language)
    @classmethod
    def distanceRow(class_, label, content):
        '''Get a row to be injected in the m_distanceSummary'''
        return f'<tr><th>{label}</th><td>{content}</td></tr>'

    @classmethod
    def distanceSummary(class_, o, p, km):
        '''Returns, as a XHTML table, a summary about the distance p_km, as
           computed by m_distanceBetween, between p_o and p_p.'''
        # Info about the origin
        row = class_.distanceRow
        orig = row('↦', class_.getNamedAddress(o))
        dest = row('↤', class_.getNamedAddress(p))
        km = row('km', '?' if km is None else formatNumber(km))
        return f'<table class="small">{orig}{dest}{km}</table>'

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                               The map
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    pxMap = Px('''
     <!-- The tag into which the map will be rendered -->
     <style>:f'#map {{height:266px; width:100%}}'</style>
     <div id="map"></div>
     <script>:f'function startMap() {{initMap({o.latitude},{o.longitude},4);}}'
     </script>
     <script var="url='https://maps.googleapis.com/maps/api/js';
                  params='callback=startMap&amp;v=weekly'"
             src=":f'{url}?key={o.config.googleApiKey}&amp;{params}'"
             defer="defer">
     </script>''',

    js='''
      function initMap(lat, lng, zoom) {
        // The location
        const place = { lat:lat, lng:lng };
        // The map, centered at v_place
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 10,
          center: place,
        });
        // The marker, positioned at v_place
        const marker = new google.maps.Marker({
          position: place,
          map: map,
        });
      }''')

    @classmethod
    def showMap(class_, o):
        '''Show the map if p_o is geolocalized and if a google API key is set'''
        if o.latitude is None or not o.config.googleApiKey: return
        return Show.E_

    map = Computed(method=pxMap, show=lambda o:Place.showMap(o),
                   layouts=LayoutF('f|'), label='Tool')

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                             Main methods
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def onEdit(self, created):
        '''Called when address is p_created or updated'''
        if self.virtual:
            # Ensure postal-related fields are cleaned
            Place.cleanGeo(self)
            Place.cleanPostal(self)
        else:
            # Try to geolocalize it
            if self.config.googleApiKey:
                Place.geolocalize(self)
            # Ensure virtual-related field is cleaned
            self.postalUrl = None
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
