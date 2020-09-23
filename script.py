from flask import jsonify, request
from app import app
from methods import get_dict_from_file


def get_city_by_id(geo_id):
    for items in GEO_CITIES_INFO:
        if items['geonameid'] == geo_id:
            return items
    return {}


def get_city_by_amount(page, amount):
    start = (amount*(page - 1) - 1)
    end = (amount*page) - 1
    result = [city for city in GEO_CITIES_INFO[start:end]]
    return result


@app.route('/geonameid/api/v1.0/', methods=['GET'])
def get_info_by_id():
    id = request.args.get('id', type=str)
    response = get_city_by_id(id)
    return jsonify(response)


@app.route('/cities/api/v1.0/', methods=['GET'])
def get_list_of_cities():
    page = request.args.get('page', type=int)
    amount = request.args.get('amount', type=int)
    return jsonify(get_city_by_amount(page, amount))


if __name__ == '__main__':
    GEO_CITIES_INFO = get_dict_from_file()
    app.run(host='127.0.0.1', port=8000, debug=True)

