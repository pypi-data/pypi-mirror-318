'''Date-related classes and functions'''

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
import sys, time, re
try:
    from DateTime import DateTime
    from DateTime.interfaces import DateError
except ImportError:
    # This module manipulates DateTime objects from the non-standard DateTime
    # module, installable via command "pip3 install DateTime"
    pass

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Days of the week
weekDaysR = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')
weekEndDays = ('Sat', 'Sun')
weekDays  = weekDaysR + weekEndDays
weekDays_ = weekDays + ('Off',)
weekDaysD = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}

# School days that last a complete day (at least in Belgium)
weekDaysC = ('Mon', 'Tue', 'Thu', 'Fri')

# Months
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
S_E_KO   = 'End date cannot be prior to start date.'

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Date:
    '''Date-related methods'''

    # Regex for matching Appy-specific date parts
    rexPart = re.compile(r'\%(dt|DT|mt|MT|dd)(\d?)')

    # Info about evert date part. For every tuple in this data structure:
    # - elem #1 is the prefix for the i18n label;
    # - elem #2 is the name of the corresponding DateTime attribute.
    infoParts = {'dt': ('day', '_aday'), 'mt': ('month', '_amon')}

    @classmethod
    def resolvePart(class_, part, date, language, _, nb=None):
        '''Resolve this date p_part'''
        # p_part corresponds to one of the symbols as defined in Date.rexPart
        if part == 'dd':
            r = str(date.day())
        else:
            # Get the translated text corresponding to this p_part
            prefix, attr = Date.infoParts[part.lower()]
            r = _(f'{prefix}_{getattr(date, attr)}', language=language)
            # Translated texts are capitalized. Lowerize it when needed.
            r = r.lower() if part.islower() else r
            if nb:
                r = r[:int(nb)]
        return r

    @classmethod
    def toUTC(class_, d):
        '''When manipulating DateTime instances, like p_d, errors can raise when
           performing operations on dates that are not in Universal time, during
           months when changing from/to summer/winter hour. This function
           returns p_d set to UTC.'''
        return DateTime(f'{d.year()}/{d.month()}/{d.day()} UTC')

    @classmethod
    def withHour(class_, date, hour):
        '''Returns this p_date (must be a DateTime object), whose "hour" part is
           ignored and has been replaced by this p_hour.'''
        # p_hour can be a string of the form HH:MM or a tuple (i_hour, i_minute)
        hourS = hour if isinstance(hour, str) else ('%d:%d' % hour)
        dateS = date.strftime('%Y/%m/%d')
        return DateTime(f'{dateS} {hourS}')

    @classmethod
    def sameDay(class_, date, other):
        '''Do p_date and p_other occur at the same day ?'''
        d1 = date.year() , date.month() , date.day()
        d2 = other.year(), other.month(), other.day()
        return d1 == d2

    @classmethod
    def asTuple(class_, d, withHour=False):
        '''Returns p_d(ate) (a DateTime object) elements (year, month, day) as a
           tuple, in that order. If p_withHour is True, it adds
           (hour, minutes).'''
        # The purpose is to compare dates without having any problem regarding
        # the timezone.
        if withHour:
            r = d.year() , d.month() , d.day(), d.hour(), d.minute()
        else:
            r = d.year() , d.month() , d.day()
        return r

    @classmethod
    def sameWeek(class_, d1, d2):
        '''Returns True if p_d1 and p_d2 (DateTime objects) occur during the
           same week.'''
        # A week starts on Monday and ends on Sunday
        i1 = weekDaysD[d1.aDay()]
        i2 = weekDaysD[d2.aDay()]
        if i1 < i2:
            delta = d2 - d1
        elif i2 < i1:
            delta = d1 - d2
        else:
            # p_d1 and p_d2 occur at the same day of the week: they occur
            # during the same week if they occcur at the same day.
            return class_.sameDay(d1, d2)
        return 0 <= delta <= 6

    @classmethod
    def getDayInterval(class_, date):
        '''Returns a tuple (startOfDay, endOfDay) representing the whole day
           into which p_date occurs.'''
        day = date.strftime('%Y/%m/%d')
        return DateTime(f'{day} 00:00'), DateTime(f'{day} 23:59')

    @classmethod
    def periodsIntersect(class_, start1, end1, start2, end2):
        '''Is there an intersection between intervals [start1, end1] and
           [start2, end2] ?'''
        # p_start1 and p_start2 must be DateTime objects.
        # p_end1 and p_end2 may be DateTime objects or None.
        #
        # Convert all parameters to seconds since the epoch
        end1 = sys.maxsize if end1 is None else end1.millis()
        end2 = sys.maxsize if end2 is None else end2.millis()
        start1 = start1.millis()
        start2 = start2.millis()
        # Intervals intersect if they are not disjoint
        if (start1 > end2) or (start2 > end1): return
        return True

    @classmethod
    def format(class_, tool, date, format=None, withHour=True, language=None,
               hourSep=' (', hourEnd=')'):
        '''Returns p_date, formatted as specified by p_format, or
           config.ui.dateFormat if not specified. If p_withHour is True, hour is
           appended, with a format specified in config.ui.hourFormat.'''
        # The separator between the date and hour parts, when both present, is
        # determined by p_hourSep. If p_hourEnd is passed, it will be appended
        # after the hour. For example, with the default values of p_hourSep
        # being " (" and hourEnd being ")", the result will be of the form:
        #
        #                            date (hour)
        #
        # Other example: with p_hourSep being " @" and p_hourEnd being the empty
        # string, the result will be of the form:
        #
        #                            date @hour
        #
        # It is common to specify p_hourSep as a translated term, like " at " in
        # english or " à " in french. Do not forget to integrate the appropriate
        # spaces within p_hourSep.
        fmt = format or tool.config.ui.dateFormat
        # Resolve Appy-specific formatting symbols used for getting translated
        # names of days or months:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  %dt[nb] | translated name of day (all lowercase). If a [nb] is
        #          | specified, only the [nb] first chars of the name will be
        #          | kept. For example, "%DT2" applied to a Monday, in english,
        #          | would produce "Mo".
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  %DT[nb] | translated name of day, capitalized
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  %mt[nb] | translated name of month (all lowercase)
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  %MT[nb] | translated name of month, capitalized
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        #  %dd     | day number, but without leading '0' if < 10
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Resolve Appy symbols by producing a version of p_fmt whose Appy
        # symbols have been resolved.
        fun = lambda m: class_.resolvePart(m.group(1), date, language, \
                                           tool.translate, nb=m.group(2))
        fmt = Date.rexPart.sub(fun, fmt)
        # Resolve all other, standard, symbols
        r = date.strftime(fmt)
        # Append hour from tool.hourFormat
        if withHour and (date._hour or date._minute):
            hourS = date.strftime(tool.config.ui.hourFormat)
            r = f'{r}{hourSep}{hourS}{hourEnd}'
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class DayIterator:
    '''Class allowing to iterate over a range of days'''

    def __init__(self, startDay, endDay, back=False):
        self.start = Date.toUTC(startDay)
        self.end = Date.toUTC(endDay)
        # If p_back is True, the iterator will allow to browse days from end to
        # start.
        self.back = back
        self.finished = False
        # Store where we are within [start, end] (or [end, start] if back)
        if not back:
            self.current = self.start
        else:
            self.current = self.end

    def __iter__(self): return self
    def __next__(self):
        '''Returns the next day'''
        if self.finished:
            raise StopIteration
        res = self.current
        # Get the next day, forward
        if not self.back:
            if self.current >= self.end:
                self.finished = True
            else:
                self.current += 1
        # Get the next day, backward
        else:
            if self.current <= self.start:
                self.finished = True
            else:
                self.current -= 1
        return res

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Week:
    '''Represents a week'''

    # A week is defined as a series of 7 consecutive days starting a Monday and
    # ending a Sunday.

    @classmethod
    def getFirstDay(class_, date):
        '''Gets the first day of the week into which this p_date is located'''
        # *d*ay *o*f *w*eek (dow) for Sunday is 0: convert it to 7
        dow = date.dow() or 7
        return date - (dow-1)

    @classmethod
    def getLastDay(class_, date):
        '''Gets the last day of the week into which this p_date is located'''
        dow = date.dow()
        if dow == 0: # A Sunday
            r = date
        else:
            r = date + (7 - dow)
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Month:
    '''Represents a month'''

    @classmethod
    def getFirstDay(class_, date, hour=None):
        '''Returns, as a DateTime object, the first day of the month into which
           p_date is included.'''
        hour = hour or '12:00'
        return DateTime(f'{date.year()}/{date.month()}/01 {hour}')

    @classmethod
    def getLastDay(class_, date, hour=None):
        '''Returns a DateTime object representing the last day of
           date.month().'''
        day = 31
        month = date.month()
        year = date.year()
        found = False
        hour = hour or '12:00'
        while not found:
            try:
                r = DateTime(f'{year}/{month}/{day} {hour}')
                found = True
            except DateError:
                day -= 1
        return r

    @classmethod
    def getInterval(class_, date, hour=None, completeWeeks=False):
        '''Returns a tuple of DateTime objects (start, end) representing the
           start and end days for the month into which p_date is included.'''
        # If p_completeWeeks is True, it returns an interval representing the
        # complete weeks being included, either partially or totally, into the
        # month in question. A "complete week" must be understood as a series of
        # 7 days, starting a Monday and ending the following Sunday. For
        # example, if p_date is 2024/05/03 and p_completeWeeks is True, it will
        # return a tuple (DateTime(2024/04/29), DateTime(2024/06/02)).
        start = class_.getFirstDay(date, hour='00:00')
        end = class_.getLastDay(date, hour=hour)
        if completeWeeks:
            start = Week.getFirstDay(start)
            end = Week.getLastDay(end)
        return start, end

    @classmethod
    def getSibling(class_, date, next=True, day=None, hour=None):
        '''Computes and returns a date corresponding to p_date but one month
           later (if p_next is True) or earlier (if p_next is False).'''
        # If day is not None, it will be used as day part in the resulting date,
        # instead of p_date's day part. If p_hour is not None, it will be used
        # as hour part instead of the one within p_date.
        if next:
            if date.month() == 12:
                year = date.year() + 1
                month = 1
            else:
                year = date.year()
                month = date.month() + 1
        else: # Get the previous month
            if date.month() == 1:
                year = date.year() - 1
                month = 12
            else:
                year = date.year()
                month = date.month() - 1
        month = str(month).zfill(2)
        dayPart = '%d' if day is None else str(day).zfill(2)
        hour = hour or '%H:%M:%S'
        fmt = f'{year}/{month}/{dayPart} {hour}'
        dateStr = date.strftime(fmt)
        try:
            r = DateTime(dateStr)
        except Exception as e:
            # Start with the first day of the target month and get its last day
            fmt = f'{year}/{month}/01'
            r = class_.getLastDay(DateTime(date.strftime(fmt)),
                                  hour=date.strftime(hour))
        return r

    @classmethod
    def getSiblingNumber(class_, date, next=True):
        '''Returns the number of the previous or p_next month w.r.t date's
           month.'''
        month = date.month()
        if next:
            r = 1 if month == 12 else month + 1
        else:
            r = 12 if month == 1 else month - 1
        return r

    @classmethod
    def getCrossedBy(class_, date, end=None, fmt='%Y%m', strict=False,
                     sorted=False):
        '''Returns, as a set of strings with this p_fmt (or a sorted list if
           p_sorted is True), the months being crossed by p_date, or, if p_end
           is passed, being crossed by range (p_date, p_end).'''
        # If p_strict is False, by "month", we mean: the complete range of dates
        # being shown when a month is shown in a monthly-view calendar. Because,
        # in that kind of view, full weeks are rendered, the "month" generally
        # encompasses several days from the previous and next months.
        #
        # If p_sorted is True, the sort key is p_fmt. Ensure it has sense to
        # sort the result with this key.
        r = set()
        fdate = date.strftime(fmt)
        r.add(fdate)
        if not strict:
            # Get the first day of the week into which p_date is
            first = Week.getFirstDay(date)
            r.add(first.strftime(fmt)) # May be from the previous month
        # Take p_end into account if present
        if end:
            # Ensure p_end is not prior to p_date
            if end < date: raise Exception(S_E_KO)
            fend = end.strftime(fmt)
            r.add(fend)
        else:
            end = date
            fend = fdate
        if not strict:
            # Get the last day of the week into which p_end is
            dow = end.dow()
            if dow != 0: # If Sunday, there is no overflow on the next month
                last = Week.getLastDay(end)
                r.add(last.strftime(fmt))
        # Add intermediary months between p_date and p_end, if distant from more
        # than one month.
        if fdate != fend and end - date > 28:
            month = class_.getSibling(date)
            smonth = month.strftime(fmt)
            while smonth not in r:
                r.add(smonth)
                month = class_.getSibling(month)
                smonth = month.strftime(fmt)
        # Sort the result if requested
        if sorted:
            r = list(r)
            r.sort()
        return r

    @classmethod
    def count(class_, start, end=None):
        '''Count the number of months that the [p_start, p_end] interval
           crosses.'''
        # p_start and p_end must be DateTime objects
        end = end or start
        if end < start: raise Exception(S_E_KO)
        # Already count the month into which p_start is
        r = 1
        current = start.year(), start.month()
        final = end.year(), end.month()
        while current != final:
            r += 1
            # Get the next month
            if current[1] == 12:
                current = current[0]+1, 1
            else:
                current = current[0], current[1]+1
        return r

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Year:
    '''Represents a year'''

    @classmethod
    def isLeap(class_, year=None):
        '''Is this p_year (or the current year by default) a leap year ?'''
        # In french, leap = "bissextile"
        year = time.localtime()[0] if year is None else year
        return ((year%400) == 0) or (((year%4) == 0) and ((year%100) != 0))

    @classmethod
    def getDays(class_, year=None):
        '''Returns the number of days within this p_year (or the current year by
           default).'''
        return 366 if Year.isLeap(year) else 365

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Seconds:
    '''Manipulates or renders seconds'''

    @classmethod
    def format(class_, seconds, sep=':'):
        '''Returns this number of p_seconds, formatted as HH:MM:SS. The
           separator between hours, minutes and seconds can be changed via
           p_sep.'''
        # Start with rounding p_seconds
        seconds = round(seconds)
        # If p_val is higher than 60, a count of minutes is computed. If this
        # count is higher than 60, a count of hours is computed. In the final
        # result, counts are separated with p_sep.
        if seconds < 60:
            minutes = hours = 0
        else:
            minutes = int(seconds / 60)
            seconds %= 60
            if minutes < 60:
                hours = 0
            else:
                hours = int(minutes / 60)
                minutes %= 60
        return f'{str(hours).zfill(2)}{sep}{str(minutes).zfill(2)}{sep}' \
               f'{str(seconds).zfill(2)}'
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
