FIELDNAMES = [
    "geonameid", "name", "asciiname",
    "alternatenames", "latitude", "longtitude",
    "feature_class", "feature_code", "country_code",
    "cc2", "admin1_code", "admin2_code", "admin3_code",
    "admin4_code", "population", "elevation", "dem",
    "timezone", "modification date"
]


def get_dict_from_file():
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
