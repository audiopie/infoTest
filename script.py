from flask import jsonify
from app import app
from methods import get_dict_from_file


def get_city_by_id(geo_id):
    geo_id = str(geo_id)
    for items in GEO_CITIES_INFO:
        if items['geonameid'] == geo_id:
            return items
    return {}


@app.route('/geonameid/<int:id>/')
def index(id):
    response = get_city_by_id(id)
    return jsonify(response)


if __name__ == '__main__':
    GEO_CITIES_INFO = get_dict_from_file()
    app.run(host='127.0.0.1', port=8000, debug=True)

