from flask import jsonify, request
from app import app
from methods import get_dict_from_file, filter_cities_by_population


@app.route('/twocities/api/v1.0/', methods=['GET'])
def get_two_cities():
    city1 = request.args.get('first', type=str).capitalize()
    city2 = request.args.get('second', type=str).capitalize()
    if city1 == '' or city2 == '':
        return jsonify("One of the city is empty")
    result_cities = []
    result_cities1 = [items for items in GEO_CITIES_INFO if city1 in items['alternatenames'] and items["feature_class"] == 'P']
    result_cities2 = [items for items in GEO_CITIES_INFO if city2 in items['alternatenames'] and items["feature_class"] == 'P']
    if result_cities1 and result_cities2:
        result_cities.append(filter_cities_by_population(result_cities1))
        result_cities.append(filter_cities_by_population(result_cities2))
    else:
        return jsonify("Here aren't city with name {} or {}. Please try again".format(city1, city2))
    return jsonify(result_cities)


@app.route('/geonameid/api/v1.0/', methods=['GET'])
def get_info_by_id():
    geo_id = request.args.get('id', type=str)
    for items in GEO_CITIES_INFO:
        if items['geonameid'] == geo_id:
            return jsonify(items)
    return {}


@app.route('/cities/api/v1.0/', methods=['GET'])
def get_list_of_cities():
    page = request.args.get('page', type=int)
    amount = request.args.get('amount', type=int)
    start = (amount * (page - 1) - 1)
    end = (amount * page) - 1
    result = [city for city in GEO_CITIES_INFO[start:end]]
    return jsonify(result)


if __name__ == '__main__':
    GEO_CITIES_INFO = get_dict_from_file()
    app.run(host='127.0.0.1', port=8000, debug=True)

