# Defining the City Class
from AppImports import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


myapikey = 'hAeBSEjY2ODSTfYaKuezLQ==7hNVTdYJwOujZmHa'

# # Defining the application routes
# app.register_blueprint(AppRoutes)
@app.route('/')
def index():
    def getUsers():
        api_url = 'https://api.api-ninjas.com/v1/randomuser'
        response = requests.get(api_url, headers={'X-Api-Key': myapikey})
        if response.status_code == requests.codes.ok:
            return jsonify(response.text)
        else:
            print("Error:", response.status_code, response.text)

    return getUsers()

@app.route('/animals/<animal>')
def animals(animal):
    def getAnimals():
        api_url = "https://api.api-ninjas.com/v1/animals?name=" + animal
        response = requests.get(api_url, headers={'X-Api-Key': myapikey})
        if response.status_code == requests.codes.ok:
            return jsonify(response.text)
        else:
            error = "Fetch Failed!!"
            return error

    return getAnimals()

@app.route('/city/<city>')
def city(city):
    def getCity(city):
        api_url = "https://api.api-ninjas.com/v1/city?city=" + city
        response = requests.get(api_url, headers={'X-Api-Key': myapikey})
        if response.status_code == requests.codes.ok:
            return jsonify(response.text)
        else:
            error = "Fetch Failed!!"
            return error

    return getCity(city)

@app.route('/city/<city>/<state>')
def cityState(city,state):
    def getCityState(city, state):
        api_url = "https://api.api-ninjas.com/v1/city?city=" + city + "&state=" + state
        response = requests.get(api_url, headers={'X-Api-Key': myapikey})
        if response.status_code == requests.codes.ok:
            return jsonify(response.text)
        else:
            error = "Fetch Failed!!"
            return error

    return getCityState(city,state)

#getcountry
@app.route('/country/<country>')
def country(country):
    def getCountry(country):
        api_url = "https://api.api-ninjas.com/v1/country?country=" + country
        response = requests.get(api_url, headers={'X-Api-Key': myapikey})
        if response.status_code == requests.codes.ok:
            return jsonify(response.text)
        else:
            error = "Fetch Failed!!"
            return error

    return getCountry(country)


if __name__ == '__main__':
    app.run(debug=True)


