# Test for Infotecs #

## Small REST API service to get geo information about cities ##

To Run script:

1. Clone repository from `git@github.com:audiopie/infoTest.git`
2. Download data from http://download.geonames.org/export/dump/RU.zip to the app directory.
3. Open command line and  type `python script.py`. 
4. The server running on http://127.0.0.1:8000/ 

### Server supports the following methods: ###

1. The method takes one argument `id` and return information about city. 
`http://127.0.0.1:8000/geonameid/api/v1.0/?id=464173`

![return city by geonameid](https://yadi.sk/i/-hO0KiNZySHS5w) 

2. The method takes two arguments `page` and `amount` and return list of cities. 
`http://127.0.0.1:8000/cities/api/v1.0/?page=2&amount=20`

![return list of cities by page and anount](https://yadi.sk/i/N2O7UNjRx3OugQ) 

3. The function get two arguments cities name in cyrillic. Return information about cities includes which city is northerly, and their UTC time difference.
`http://127.0.0.1:8000/twocities/api/v1.0//?first=city&second=city`

![return information about two cities](https://yadi.sk/i/dAov06PY0ZLxow)

4. The method is helper, takes argument like a half-word of city and return all cities matches it.
`http://127.0.0.1:8000/matches/api/v1.0/?city=Сам`

![return list of matches cities](https://yadi.sk/i/3zwvwwRkyMNL3g)