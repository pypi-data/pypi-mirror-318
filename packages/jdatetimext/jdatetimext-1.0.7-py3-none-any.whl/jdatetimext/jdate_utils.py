import jdatetime
from datetime import datetime, timedelta

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_FORMAT = '%Y-%m-%d'


def j_start_j(date_type='day', date_value=datetime.now() ):
    '''
    It takes a datetime and date_type (day, week,...). Then it find the START date of the date_type.
    The calculation and output will be on JALAALI calendar.
    Example:
        date_type: 'year'
        date_value: 2024-11-25 10:08:50
        return: jdatetime.datetime(1403, 1, 1, 0, 0)
    :param date_type: string
    :param date_value: datetime
    :return: jdatetime
    '''
    quarter_list = [1, 4, 7, 10]
    # print(f"+++++ \n date_type: {date_type}, date_value: {date_value}")
    if type(date_value) == str:
        date_value = date_value.split('.', 1)[0]
        date_value_d = datetime.strptime(date_value, DATETIME_FORMAT)
    else:
        date_value_d = date_value

    jdate_value = jdatetime.datetime.fromgregorian(datetime=date_value_d)
    jdate_value_d = jdate_value
    j_year = jdate_value.year
    j_month = jdate_value.month
    j_day = jdate_value.day
    j_hour = jdate_value.hour
    j_minute = jdate_value.minute
    j_second = jdate_value.second
    if date_type == 'year':
        jdate_value_d = jdatetime.datetime(j_year, 1, 1, 0, 0)
    elif date_type == 'quarter':
        jdate_value_d = jdatetime.datetime(j_year, quarter_list[(j_month - 1) // 3], 1, 0, 0, 0)
    elif date_type == 'month':
        jdate_value_d = jdatetime.datetime(j_year, j_month, 1, 0, 0, 0)
    elif date_type == 'week':
        if jdate_value.weeknumber() != 1:
            jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, 0, 0, 0) - timedelta(days=jdate_value.weekday())
        else:
            jdate_value_d = jdatetime.datetime(j_year, 1, 1, 0, 0)

    elif date_type == 'day':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, 0, 0, 0)
    elif date_type == 'hour':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, j_hour, 0, 0)
    elif date_type == 'minute':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, j_hour, j_minute, 0)
    elif date_type == 'second':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, j_hour, j_minute, j_second)
    elif date_type == '_':
        jdate_value_d = jdate_value

    return jdate_value_d

def j_start(date_type='day', date_value=datetime.now()):
    '''
    It takes a datetime and date_type (day, week,...). Then it find the START date of the date_type.
    The calculation is based on Jalaali calendar but the output will be GREGORIAN calendar
    Example:
        date_type: 'year'
        date_value: 2024-11-25 10:08:50
        return: datetime.datetime(2024, 3, 20, 0, 0)
    :param date_type: string
    :param date_value: datetime
    :return: datetime
    '''
    return j_start_j(date_type, date_value).togregorian()

def j_end_j(date_type='day', date_value=datetime.now() ):
    '''
    It takes a datetime and date_type (day, week,...). Then it find the END date of the date_type.
    The calculation and output will be on JALAALI calendar.
    Example:
        date_type: 'year'
        date_value: 2024-11-25 10:08:50
        return: jdatetime.datetime(1404, 1, 1, 0, 0)
    :param date_type: string
    :param date_value: datetime
    :return: jdatetime
    '''

    quarter_list = [1, 4, 7, 10]
    if type(date_value) == str:
        date_value = date_value.split('.', 1)[0]
        date_value_d = datetime.strptime(date_value, DATETIME_FORMAT)
    else:
        date_value_d = date_value


    jdate_value = jdatetime.datetime.fromgregorian(date=date_value_d)
    jdate_value_d = jdate_value
    j_year = jdate_value.year
    j_month = jdate_value.month
    j_day = jdate_value.day
    j_hour = jdate_value.hour
    j_minute = jdate_value.minute
    j_second = jdate_value.second
    if date_type == 'year':
        jdate_value_d = jdatetime.datetime(j_year + 1, 1, 1, 0, 0)
    elif date_type == 'quarter':
        j_month = quarter_list[(j_month - 1) // 3]
        if j_month < 9:
            j_month += 3
        else:
            j_month = 1
            j_year += 1
        jdate_value_d = jdatetime.datetime(j_year, j_month, 1, 0, 0, 0)
    elif date_type == 'month':
        first_day = jdatetime.datetime(j_year, j_month, 1, 0, 0, 0)
        next_month = first_day.replace(day=28) + timedelta(days=5)
        jdate_value_d = next_month.replace(day=1)
    elif date_type == 'week':
        if jdate_value_d.weeknumber() < 52:
            # TODO: The last week of a year can be share between two years. last day of the week is the last day of
            #   that year.
            #   if last day of this week has the same year record, its ok
            #   if not, find the last day of the year, then set the last day of the year as end of the week
            jdate_value_d = jdate_value_d + timedelta(days=7 - jdate_value_d.weekday())
        else:
            # TODO:
            #   find the last day of current week by finding the next week first day minus one.
            next_week_start = jdate_value_d + timedelta(days=7 - jdate_value_d.weekday())
            if next_week_start.year == j_year:
                jdate_value_d = jdate_value_d + timedelta(days=7 - jdate_value_d.weekday())
            else:
                jdate_value_d = jdatetime.datetime(j_year + 1, 1, 1, 0, 0)

    elif date_type == 'day':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, 0, 0, 0) + timedelta(days=1)
    elif date_type == 'hour':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, j_hour, 0, 0) + timedelta(hours=1)
    elif date_type == 'minute':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, j_hour, j_minute, 0) + timedelta(
            minutes=1)
    elif date_type == 'second':
        jdate_value_d = jdatetime.datetime(j_year, j_month, j_day, j_hour, j_minute, j_second) + timedelta(
            seconds=1)
    else:
        jdate_value_d = jdate_value

    return jdate_value_d

def j_end(date_type='day', date_value=datetime.now() ):
    '''
    It takes a datetime and date_type (day, week,...). Then it find the END date of the date_type.
    The calculation is based on Jalaali calendar but the output will be GREGORIAN calendar
    Example:
        date_type: 'year'
        date_value: 2024-11-25 10:08:50
        return: datetime.datetime(2025, 3, 21, 0, 0)
    :param date_type: string
    :param date_value: datetime
    :return: datetime
    '''
    return j_end_j(date_type, date_value).togregorian()

def j_start_end(date_type='day', date_value=datetime.now()):
    '''
    It takes a datetime and date_type (day, week,...). Then it find the START and END date of the date_type.
    The calculation is based on Jalaali calendar but the output will be GREGORIAN calendar
    Example:
        date_type: 'year'
        date_value: 2024-11-25 10:08:50
        return: (datetime.datetime(2024, 3, 20, 0, 0), datetime.datetime(2025, 3, 21, 0, 0))
    :param date_type: string
    :param date_value: datetime
    :return: (datetime, datetime)
    '''
    start_date = j_start(date_type, date_value)
    end_date = j_end(date_type, date_value)
    return (start_date, end_date)

def j_start_end_j(date_type='day', date_value=datetime.now()):
    '''
    It takes a datetime and date_type (day, week,...). Then it find the START and END date of the date_type.
    The calculation is based on Jalaali calendar but the output will be JDATETIME of JALAALI calendar
    Example:
        date_type: 'year'
        date_value: 2024-11-25 10:08:50
        return: (jdatetime.datetime(1403, 1, 1, 0, 0), jdatetime.datetime(1403, 12, 30, 23, 59, 59)) <1>

    <1>: Jalaali output is the last second ot end date. 1403-12-30 23:59:59

    :param date_type: string
    :param date_value: datetime
    :return: (datetime, datetime)
    '''
    start_date = j_start_j(date_type, date_value)
    end_date = j_end_j(date_type, date_value) - timedelta(seconds=1)
    return (start_date, end_date)

def j_start_end_js(date_type='day', date_value=datetime.now(), dt='datetime', format=DATETIME_FORMAT):
    '''
    It takes a datetime and date_type (day, week,...). Then it find the START and END date of the date_type.
    The calculation is based on Jalaali calendar but the output will be STRING of JALAALI calendar
    Example:
        date_type: 'year'
        date_value: 2024-11-25 10:08:50
        return: dt='date' -> ('1403-01-01', '1403-12-30') <1>
                dt=''     -> ('1403-01-01 00:00:00', '1403-12-30 23:59:59') <1>

        <1>: Jalaali output is the last second ot end date. 1403-12-30 23:59:59
    :param date_type: string
    :param date_value: datetime
    :param dt: string
    :return: (string, string)
    '''
    start_date = j_start_j(date_type, date_value).strftime(format)
    end_date = (j_end_j(date_type, date_value) - timedelta(seconds=1)).strftime(format)

    return (start_date, end_date)

def jdatejs(date_value=datetime.now(), format=DATE_FORMAT):
    return j_start_end_js(date_type='day', date_value=date_value, dt='date', format=format)[0]