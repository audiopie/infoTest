from datetime import datetime
from pytz import timezone
from dateutil.relativedelta import relativedelta


FIELDNAMES = [
    "geonameid", "name", "asciiname",
    "alternatenames", "latitude", "longtitude",
    "feature_class", "feature_code", "country_code",
    "cc2", "admin1_code", "admin2_code", "admin3_code",
    "admin4_code", "population", "elevation", "dem",
    "timezone", "modification date"
]


def get_dict_from_file():
    """"The function read txt file and return list with dictionaries information about cities """
    list_of_geo = []
    result = []
    try:
        with open('RU.txt', 'r') as f:
            for line in f:
                list_of_geo.append(line.split('\t'))

        for i in range(len(list_of_geo)):
            item = dict(zip(FIELDNAMES, list_of_geo[i]))
            result.append(item)
        return result
    except FileNotFoundError:
        print("File 'RU.txt' must be in the same directory")
        exit()


def filter_cities_by_population(arr):
    """The function takes argument-array with dictionary and filter it by population of city.
    If population cities similar, function return first item from array.
    """
    default_population = 0
    high_population_city = []
    for item in arr:
        if int(item["population"]) > default_population:
            default_population = int(item["population"])
            high_population_city = item
    if high_population_city:
        return high_population_city
    else:
        return arr[0]


def check_latitude(arr):
    """The function takes argument-array with dictionaries of cities and compare they which city is further north.
       Return array with additional dictionary about northerly.
       """
    additional_info = {'higher_latitude': '', 'time_difference': ''}
    if float(arr[0]['latitude'] > arr[1]['latitude']):
        additional_info['higher_latitude'] = '{} situated further north than city {}'.format(
            arr[0]['name'], arr[1]['name'])
    else:
        additional_info['higher_latitude'] = '{} situated further north than city {}'.format(
            arr[1]['name'], arr[0]['name'])
    arr.append(additional_info)
    return check_time_zone(arr)


def check_time_zone(arr):
    """The function takes argument-array with dictionaries of cities and check they UTC time difference.
        Return array with additional key about time-zone.
    """
    utc_now = timezone('utc').localize(datetime.utcnow())
    city1_timezone = utc_now.astimezone(timezone(arr[0]['timezone'])).replace(tzinfo=None)
    city2_timezone = utc_now.astimezone(timezone(arr[1]['timezone'])).replace(tzinfo=None)
    offset = relativedelta(city1_timezone, city2_timezone)
    if offset.hours and offset.hours > 0:
        arr[2]['time_difference'] = '{} have difference time +{} hours from {}'.format(arr[0]['name'],
                                                                                           offset.hours, arr[1]['name'])
    elif offset.hours and offset.hours < 0:
        arr[2]['time_difference'] = '{} have difference time {} hours from {}'.format(arr[0]['name'],
                                                                                          offset.hours, arr[1]['name'])
    else:
        arr[2]['time_difference'] = '{} have the same UTC-time as city {}'.format(arr[0]['name'],
                                                                                           arr[1]['name'])
    return arr
