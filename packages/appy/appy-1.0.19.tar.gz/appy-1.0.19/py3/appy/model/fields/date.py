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
import time

from DateTime import DateTime
from DateTime.interfaces import DateError, SyntaxError

from appy.px import Px
from appy.utils import dates
from appy.model.fields import Field
from appy.model.fields.hour import Hour
from appy.database.operators import in_
from appy.database.indexes.date import DateIndex

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
DEF_DAY_KO  = 'Wrong value for Date::defaultDay.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Date(Field):

    # Required CSS and Javascript files for this type
    cssFiles = {'edit': ('jscalendar/calendar-blue.css',)}
    jsFiles = {'edit': ('jscalendar/calendar.js',
                        'jscalendar/lang/calendar-en.js',
                        'jscalendar/calendar-setup.js')}

    # Make class DateTime available here
    DateTime = DateTime

    # Possible values for "format"
    WITH_HOUR    = 0
    WITHOUT_HOUR = 1
    dateParts = ('year', 'month', 'day')
    hourParts = ('hour', 'minute')
    editSep = ':' # Separator between hours and minutes

    # Types of the native HTML inputs, for every format
    nativeWidgets = {WITH_HOUR: 'datetime-local', WITHOUT_HOUR: 'date'}

    # Date formats as understood by native widgets
    nativeFormats = {WITH_HOUR: '%Y-%m-%dT%H:%M', WITHOUT_HOUR: '%Y-%m-%d'}

    # Default value on the search screen
    searchDefault = (None, None, None)

    # Precision of the indexed value, in minutes
    indexPrecision = 1

    # The name of the index class storing values of this field in the catalog
    indexType = 'DateIndex'

    view = cell = buttons = Px('''<x>:value or field.empty</x>''')

    # PX for selecting hour and minutes, kindly provided by field Hour
    pxHour = Hour.edit

    # When searching / filtering dates, the encoded date may have several
    # meanings. Must the search match anything:
    # (a) with this precise date, or
    # (b) until this date, or
    # (c) from this date ?
    match = ('precise', 'until', 'from')

    edit = Px('''
     <!-- Native variant -->
     <input if="field.native" name=":name" id=":name"
            style=":field.getDateStyle(o)"
            type=":field.nativeWidgets[field.format]"
            value=":field.getNativeValue(
             field.getInputValue(inRequest, requestValue, rawValue))"/>

     <!-- Variant with one select widget for every part of the date/time -->
     <x if="not field.native"
        var="years=field.getSelectableYears(o);
             disabled=field.getDisabled(o)">

      <!-- Day -->
      <select if="field.showDay" var2="days=range(1,32); part=f'{name}_day'"
              name=":part" id=":part" disabled=":disabled">
       <option value="">-</option>
       <option for="day in days" var2="zDay=str(day).zfill(2)" value=":zDay"
         selected=":field.isSelected(o, part, 'day', \
                                     day, rawValue)">:zDay</option>
      </select> 

      <!-- Month -->
      <select var="months=range(1,13); part=f'{name}_month'"
              name=":part" id=":part" disabled=":disabled">
       <option value="">-</option>
       <option for="month in months"
         var2="zMonth=str(month).zfill(2)" value=":zMonth"
         selected=":field.isSelected(o, part, 'month', \
                                     month, rawValue)">:zMonth</option>
      </select> 

      <!-- Year -->
      <x var="part=f'{name}_year'">
       <select if="field.showYear" name=":part" id=":part" disabled=":disabled">
        <option value="">-</option>
        <option for="year in years" value=":year"
          selected=":field.isSelected(o, part, 'year', \
                                      year, rawValue)">:year</option>
       </select>
       <input if="not field.showYear" type="hidden" name=":part"
              value=":field.DateTime().year()"/>
      </x>

      <!-- The icon for displaying the calendar popup -->
      <x if="field.calendar and field.showYear and not disabled">
       <input type="hidden" id=":name" name=":name"/>
       <img id=":f'{name}_img'" src=":svg('calendar')" class="iconS"/>
       <script>::field.getJsInit(name, years)</script>
      </x>

      <!-- Hour and minutes -->
      <x if="field.format == 0">:field.pxHour</x>
     </x>''')

    search = Px('''
     <table var="years=field.getSelectableYears(o);
                 dstart,dend=field.getDefaultSearchValues(o)">
       <!-- From -->
       <tr var="fromName=f'{name}_from';
                dayFromName=f'{name}_from_day';
                monthFromName=f'{name}_from_month'">
        <td><label>:_('date_from')</label></td>
        <td>
         <select id=":dayFromName" name=":dayFromName">
          <option value="">--</option>
          <option for="value in [str(v).zfill(2) for v in range(1, 32)]"
                  value=":value" selected=":value == dstart[2]">:value</option>
         </select> / 
         <select id=":monthFromName" name=":monthFromName">
          <option value="">--</option>
          <option for="value in [str(v).zfill(2) for v in range(1, 13)]"
                  value=":value" selected=":value == dstart[1]">:value</option>
         </select> / 
         <select id=":widgetName" name=":widgetName">
          <option value="">--</option>
          <option for="value in years"
                  value=":value" selected=":value == dstart[0]">:value</option>
         </select>
         <!-- The icon for displaying the calendar popup -->
         <x if="field.calendar">
          <input type="hidden" id=":fromName" name=":fromName"/>
          <img id=":f'{fromName}_img'" src=":svg('calendar')" class="iconS"/>
          <script>::field.getJsInit(fromName, years)</script>
         </x>
         <!-- Hour and minutes when relevant -->
         <x if="field.format == 0 and field.searchHour"
            var2="hPart=f'{name}_from_hour';
                  mPart=f'{name}_from_minute'">:field.pxHour</x>
        </td>
       </tr>

       <!-- To -->
       <tr var="toName=f'{name}_to';
                dayToName=f'{name}_to_day';
                monthToName=f'{name}_to_month';
                yearToName=f'{name}_to_year'">
        <td><label>:_('date_to')</label></td>
        <td height="20px">
         <select id=":dayToName" name=":dayToName">
          <option value="">--</option>
          <option for="value in [str(v).zfill(2) for v in range(1, 32)]"
                  value=":value" selected=":value == dend[2]">:value</option>
         </select> / 
         <select id=":monthToName" name=":monthToName">
          <option value="">--</option>
          <option for="value in [str(v).zfill(2) for v in range(1, 13)]"
                  value=":value" selected=":value == dend[1]">:value</option>
         </select> / 
         <select id=":yearToName" name=":yearToName">
          <option value="">--</option>
          <option for="value in years"
                  value=":value" selected=":value == dend[0]">:value</option>
         </select>
         <!-- The icon for displaying the calendar popup -->
         <x if="field.calendar">
          <input type="hidden" id=":toName" name=":toName"/>
          <img id=":f'{toName}_img'" src=":svg('calendar')" class="iconS"/>
          <script>::field.getJsInit(toName, years)</script>
         </x>
         <!-- Hour and minutes when relevant -->
         <x if="field.format == 0 and field.searchHour"
            var2="hPart=f'{name}_to_hour';
                  mPart=f'{name}_to_minute'">:field.pxHour</x>
        </td>
       </tr>
      </table>''')

    # Widget for filtering objects (based on a date) on search results
    pxFilter = Px('''
     <div class="dropdownMenu fdrop" onmouseover="showDropdown(this)"
          onmouseout="closeDropdown(this)"
          var="inFilter,dateF,matchF=field.getFilterInfo(mode)">
        <img src=":svg('fdrop')"/>
        <span if="inFilter">›</span>

       <!-- Dropdown -->
       <div class="dropdown fdown ddown"
            var="js='on%%sDate(this,%%s,%s,%s)' % (q(mode.hook),q(field.name))">
        <!-- Precise / until / from -->
        <div for="match in field.match" class="matchD">
         <label lfor=":match">:_(f'date_match_{match}')</label>
         <input type="radio" id=":match" name="match" value=":match"
                checked=":match == matchF"/>
        </div>

        <div class="dateROW">
         <!-- Date chooser -->
         <input type="date" value=":dateF if inFilter else ''"
                onkeydown=":js % ('Key', 'true')"
                onclick=":js % ('Click', 'true')"
                onchange=":js % ('Change', 'true')"/>

         <!-- Ok / cancel -->
         <span class="clickable dateICO"
               onclick=":js % ('Filter', 'true')">✓</span>
         <span class="clickable dateICO"
               onclick=":js % ('Filter', 'false')">✖</span>
        </div>
       </div>
     </div>''',

     js='''
      onFilterDate = function(button, entered, hook, name) {
        // Get the value and match
        let div = button.parentNode,
            filter = div.parentNode,
            date = div.querySelector('input[type="date"]').value;
        // Must the filter be applied or reinitialized ?
        if (entered) {
          // Do nothing if no v_date has been entered
          if (!date || date === 'undefined') return;
          let match = filter.querySelector('input[name="match"]:checked').value;
          date = `${date}*${match}`;
        }
        else date = '';  // Reinitialize the filter: empty the date
        askBunchFiltered(hook, name, date);
      }

      onKeyDate = function(date, entered, hook, name) {
        date.fromPicker = false;
        if (event.keyCode==13) onFilterDate(date, entered, hook, name);
      }

      onClickDate = function(date, entered, hook, name) {
        date.fromPicker = true;
      }

      onChangeDate = function(date, entered, hook, name) {
        if (date.fromPicker) onFilterDate(date, entered, hook, name);
      }''',

     css='''
      .dropdown input[type=date] { border:1px solid lightgrey;
        font-size:100%; width:8.2em }
      .ddown { width:11em; overflow-x:auto; z-index:5 }
      .dateICO { color:grey; font-size:1.3em; padding-left:0.3em;
                 background-color:transparent !important }
      .dateROW { display:flex; justify-content:right; margin-top:0.4em }
      .matchD { display:flex; align-items:center; justify-content:right }
      .matchD label { text-transform:none; text-align:left; padding:0.2em 0.3em}
     ''')

    def __init__(self, validator=None, multiplicity=(0,1), default=None,
      defaultOnEdit=None, format=WITH_HOUR, dateFormat=None, hourFormat=None,
      calendar=True, startYear=time.localtime()[0]-10,
      endYear=time.localtime()[0]+10, reverseYears=False, minutesPrecision=5,
      show=True, renderable=None, page='main', group=None, layouts=None, move=0,
      indexed=False, mustIndex=True, indexValue=None, emptyIndexValue=0,
      searchable=False, filterField=None, readPermission='read',
      writePermission='write', width=None, height=None, maxChars=None,
      colspan=1, master=None, masterValue=None, focus=False, historized=False,
      mapping=None, generateLabel=None, label=None, sdefault=None, scolspan=1,
      swidth=None, sheight=None, persist=True, view=None, cell=None,
      buttons=None, edit=None, custom=None, xml=None, translations=None,
      showDay=True, defaultDay=1, showYear=True, searchHour=False, native=False,
      empty='-', matchDefault='precise', disabled=False):
        self.format = format
        self.calendar = calendar
        self.startYear = startYear
        self.endYear = endYear
        # If reverseYears is True, in the selection box, available years, from
        # self.startYear to self.endYear will be listed in reverse order.
        self.reverseYears = reverseYears
        # If p_showDay is False, the list for choosing a day will be hidden.
        # The stored DateTime object will get "1" as day part.
        self.showDay = showDay
        # When the day is not shown, what will be the value set for it ? The
        # following attribute allows to define it: it must hold an integer value
        # or string "last", that will converted to the last day of the month.
        self.defaultDay = defaultDay
        # If p_showYear is False, the list for choosing a year will not be
        # shown. The stored DateTime object will get the current year as year.
        self.showYear = showYear
        # If no p_dateFormat/p_hourFormat is specified, the application-wide
        # tool.dateFormat/tool.hourFormat is used instead.
        self.dateFormat = dateFormat
        self.hourFormat = hourFormat
        # In the context of a Date, the max hour is always 23. But it can be
        # more in the context of an Hour field.
        self.maxHour = 23
        # If "minutesPrecision" is 5, only a multiple of 5 can be encoded. If
        # you want to let users choose any number from 0 to 59, set it to 1.
        self.minutesPrecision = minutesPrecision
        # The search widget will only allow to specify start and end dates
        # without hour, event if format is WITH_HOUR, excepted if searchHour is
        # True.
        self.searchHour = searchHour
        # Value for p_sdefault must be a tuple (start, end), where each value
        # ("start" or "end"), if not None, must be a tuple (year, month, day).
        # Each of these sub-values can be None or an integer value. p_sdefault
        # can also be a method that produces the values in the specified format.
        #
        # [Experimental] the "native" mode makes use of HTML native input fields
        # "date" (if p_format is WITHOUT_HOUR) or "datetime-local" (if p_format
        # is WITH_HOUR).
        self.native = native
        # What to show on cell or view when there is no date ?
        self.empty = empty
        # When filtering p_self's values, the default match strategy is the one
        # stored in the following attribute. For more info about match
        # strategies, check static attribute Date.match defined hereabove.
        self.matchDefault = matchDefault
        # Must p_self be shown, on "edit", in "disabled" mode? It works only if
        # p_self is rendered as a non-native widget.
        self.disabled = disabled
        # Call the base constructor
        super().__init__(validator, multiplicity, default, defaultOnEdit, show,
          renderable, page, group, layouts, move, indexed, mustIndex,
          indexValue, emptyIndexValue, searchable, filterField, readPermission,
          writePermission, width, height, None, colspan, master, masterValue,
          focus, historized, mapping, generateLabel, label, sdefault, scolspan,
          swidth, sheight, persist, False, view, cell, buttons, edit, custom,
          xml, translations)
        # Define the filter PX when appropriate
        if self.indexed:
            self.filterPx = 'pxFilter'
        # This field stores DateTime values
        self.pythonType = DateTime

    def getCss(self, o, layout, r):
        '''CSS files are only required if the calendar must be shown'''
        if self.calendar: Field.getCss(self, o, layout, r)

    def getJs(self, o, layout, r, config):
        '''Javascript files are only required if the calendar must be shown'''
        if self.calendar: Field.getJs(self, o, layout, r, config)

    def getSelectableYears(self, o):
        '''Gets the list of years one may select for this field'''
        startYear = self.getAttribute(o, 'startYear')
        r = list(range(startYear, self.endYear + 1))
        if self.reverseYears: r.reverse()
        return r

    def validateValue(self, o, value):
        try:
            value = DateTime(value)
        except (DateError, ValueError, SyntaxError):
            return o.translate('bad_date')

    def getFormattedValue(self, o, value, layout='view', showChanges=False,
                          language=None):
        if self.isEmptyValue(o, value): return ''
        # Get the applicable date format
        ui = o.config.ui
        formaT = self.dateFormat or ui.dateFormat
        # A problem may occur with some extreme year values. Replace the "year"
        # part "by hand".
        if '%Y' in formaT:
            # Moreover, do not show the year at all when appropriate
            showYear = self.showYear
            repl = str(value.year()) if showYear else ''
            formaT = formaT.replace('%Y', repl)
            if not showYear:
                # Ensure there is no remaining year separator
                formaT = formaT.strip('-/')
        if not self.showDay and '%d' in formaT:
            formaT = formaT.replace('%d', '').strip('-/')
        r = dates.Date.format(o.tool, value, formaT, withHour=False)
        if self.format == Date.WITH_HOUR:
            houR = value.strftime(self.hourFormat or ui.hourFormat)
            r = f'{r} {houR}'
        return r

    def getRequestDay(self, value):
        '''Get the day to use when the day is not part of the request, due to
           p_self.showDay being False.'''
        day = self.defaultDay
        if isinstance(day, int):
            r = day
        elif day == 'last':
            # Compute the last day of the month. The year and month are already
            # available in p_value.
            r = dates.Month.getLastDay(DateTime(f'{value}01')).day()
        else:
            raise Exception(DEF_DAY_KO)
        return str(r).zfill(2)

    def getRequestValue(self, o, requestName=None):
        req = o.req
        name = requestName or self.name
        # Manage a native date
        if self.native: return req[name]
        # Manage the "date" part
        value = ''
        for part in self.dateParts:
            # The "day" part may be hidden. Use "1" by default.
            if part == 'day' and not self.showDay:
                valuePart = self.getRequestDay(value)
            else:
                valuePart = req[f'{name}_{part}']
            if not valuePart: return
            value = f'{value}{valuePart}/'
        value = value[:-1]
        # Manage the "hour" part
        if self.format == self.WITH_HOUR:
            value = f'{value} '
            for part in self.hourParts:
                valuePart = req[f'{name}_{part}']
                if not valuePart: return
                value = f'{value}{valuePart}:'
            value = value[:-1]
        return value

    def getNativeValue(self, value):
        '''Ensure p_value is a string being understood by the native HTML
           inputs.'''
        return value.strftime(Date.nativeFormats[self.format]) \
               if isinstance(value, DateTime) else value

    def getDateStyle(self, o):
        '''Gets the content of the "style" attribute for the input date widget
           on the "edit" layout.'''
        width = self.width
        return f'width:{width}' if width else ''

    def searchValueIsEmpty(self, req):
        '''We consider a search value being empty if both "from" and "to" values
           are empty. At an individual level, a "from" or "to" value is
           considered not empty if at least the year is specified.'''
        # The base method determines if the "from" year is empty
        isEmpty = Field.searchValueIsEmpty
        return isEmpty(self, req) and \
               isEmpty(self, req, widgetName=f'{self.name}_to_year')

    def getRequestSuffix(self, o):
        return '' if self.native else '_year'

    def getStorableValue(self, o, value, single=False):
        '''Converts this string p_value to a DateTime object'''
        if not self.isEmptyValue(o, value):
            if self.native:
                # Standardise this value: else, timezone may be wrong
                value = value.replace('-', '/').replace('T', ' ')
            return DateTime(value)

    def getFilterValue(self, value):
        '''Take care of match precision'''
        # Extract, from p_value, the match type
        value, match = value.split('*')
        r = super().getFilterValue(value)
        if match == 'from':
            r = in_(r, None)
        elif match == 'until':
            r = in_(None, r)
        return r

    def getValueFilter(self, value):
        '''Converts this read-to-search p_value into a value that can be
           understood by a filter.'''
        if isinstance(value, in_):
            vA, vB = value.values
            if vA is None:
                date = vB
                match = 'until'
            else:
                date = vA
                match = 'from'
        else:
            date = value
            match = 'precise'
        return f'{date.strftime("%Y-%m-%d")}*{match}'

    def getFilterInfo(self, mode):
        '''Returns, as a tuple (b_inFilter, s_date, s_match) info about a
           potential filter value from a search having this p_mode. The filter
           value, within p_mode.filters, can be a DateTime object or a in_
           operator.'''
        filters = mode.filters
        # There may be no value at all
        inFilter = self.name in filters
        if not inFilter: return False, None, self.matchDefault
        # Extract the encoded date and match
        value = filters[self.name]
        if isinstance(value, DateTime):
            date = value
            match = 'precise'
        else:
            # a in_ operator
            a, b = value.values
            match = 'from' if b is None else 'until'
            date = a or b
        return inFilter, date.strftime('%Y-%m-%d'), match

    @classmethod
    def getDateFromSearchValue(class_, year, month, day, hour, setMin):
        '''Gets the index representation of a valid DateTime object, built from
           date information coming from the request.'''
        # This info comes as strings in p_year, p_month, p_day and p_hour.
        # The method returns None if p_year is empty. If p_setMin is True, when
        # some information is missing (month or day), it is replaced with the
        # minimum value (=1). Else, it is replaced with the maximum value
        # (=12, =31).
        if not year: return
        # Set month and day
        if not month:
            month = 1 if setMin else 12
        if not day:
            day = 1 if setMin else 31
        # Set the hour
        if hour is None:
            hour = '00:00' if setMin else '23:59'
        # The specified date may be invalid (ie, 2018/02/31): ensure to produce
        # a valid date in all cases.
        try:
            r = DateTime(f'{year}/{month}/{day} {hour}')
        except:
            base = DateTime(f'{year}/{month}/01')
            r = dates.Month.getLastDay(base, hour=hour)
        return r

    @classmethod
    def getSearchPart(class_, field, req, to=False, value=None,searchHour=None):
        '''Gets the search value from p_req corresponding to the "from" or "to"
           part (depending on boolean p_to).'''
        name = field.name
        part = 'to' if to else 'from'
        hour = None
        if value is None:
            # Get the year. For the "from" part, it corresponds to the name of
            # field. For the "to" part, there is a specific key in the request.
            year = req[f'{name}_to_year'] \
                   if to else Field.getSearchValue(field, req, value=value)
            month = req[f'{name}_{part}_month']
            day = req[f'{name}_{part}_day']
            if searchHour:
                H = req[f'{name}_{part}_hour'] or '00'
                M = req[f'{name}_{part}_minute'] or '00'
                hour = f'{H}:{M}'
        else:
            # p_value is there, as a DateTime object
            year, month, day = value.year(), value.month(), value.day()
            if searchHour:
                hour = '00:00'
        return Date.getDateFromSearchValue(year, month, day, hour, not to)

    @classmethod
    def computeSearchValue(class_, field, req, value=None, searchHour=False):
        '''Converts raw search values from p_req into an interval of dates'''
        # p_value may already be a ready-to-use interval
        if isinstance(value, in_): return value
        return in_(Date.getSearchPart(field, req, False, value, searchHour),
                   Date.getSearchPart(field, req, True , value, searchHour))

    def getSearchValue(self, req, value=None):
        '''See called method's docstring'''
        return Date.computeSearchValue(self, req, value=value,
                                       searchHour=self.searchHour)

    def getDefaultSearchValues(self, o):
        '''Gets the default value for this field when shown on a search
           layout.'''
        default = self.getAttribute(o, 'sdefault')
        if not default:
            r = self.searchDefault, self.searchDefault
        else:
            # Convert months and days to zfilled strings
            r = []
            for i in (0, 1):
                value = default[i]
                if value:
                    year, month, day = value
                    if month is not None: month = str(month).zfill(2)
                    if day is not None: day = str(day).zfill(2)
                    value = year, month, day
                else:
                    value = self.searchDefault
                r.append(value)
        return r

    def isSelected(self, o, part, fieldPart, dateValue, dbValue):
        '''When displaying this field in non-native mode, must the particular
           p_dateValue be selected in the sub-field p_fieldPart corresponding to
           the date part ?'''
        # Get the value we must compare (from request or from database)
        req = o.req
        if part in req:
            compValue = req[part]
            if compValue.isdigit():
                compValue = int(compValue)
        else:
            compValue = dbValue
            if compValue:
                compValue = getattr(compValue, fieldPart)()
        # Compare the value
        return compValue == dateValue

    def isSortable(self, inRefs=False):
        '''Can this field be sortable ?'''
        return True if inRefs else Field.isSortable(self) # Sortable in Refs

    def getJsInit(self, name, years):
        '''Gets the Javascript init code for displaying a calendar popup for
           this field, for an input named p_name (which can be different from
           self.name if, ie, it is a search field).'''
        # Always express the range of years in chronological order.
        years = [years[0], years[-1]]
        years.sort()
        return f'Calendar.setup({{inputField: "{name}", button: "{name}_img",' \
               f' onSelect: onSelectDate, range:{str(years)}, firstDay: 1}})'
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
