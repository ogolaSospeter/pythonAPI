from flask import Flask, jsonify, request, render_template, redirect, url_for
import requests

app = Flask(__name__)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

app.config['SECRET'] = 'secret'

@app.route('/get_dog_breeds', methods=['GET'])
def get_dog_breeds():
    api_url = 'https://dogapi.dog/api/v2/breeds'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/get_dog_breeds_groups',methods=['GET'])
def get_dog_breeds_groups():
    api_url = 'https://dogapi.dog/api/v2/groups'

    try:
        response = requests.get(api_url)
        data = response.json()
        return data
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/get_dog/<int:dog_id>/', methods=['GET'])
def get_dog():
    api_url = ''
    try:
        response = request.get(api_url)
        dog_data = response.json
        return jsonify(dog_data)

    except Exception as e:
        return jsonify({'Error in Fetch Operation': str(e)})


#The Meals API
@app.route('/get_meals', methods=['GET'])
def get_meals():
    api_url = 'https://opentdb.com/api.php?amount=1&category=18'
    try:
        response = requests.get(api_url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_twitter', methods=['GET'])
def get_twitter():
    api_url = 'https://www.geeksforgeeks.org/api/students'
    try:
        response = requests.get(api_url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/get_dog_facts', methods=['GET'])
def get_dog_facts():
    api_url = 'https://dogapi.dog/api/v2/facts'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/get_dog_images', methods=['GET'])
def get_dog_images():
    api_url = 'https://dogapi.dog/api/v2/groups?page[number]=2'
    
    try:
        response = requests.get(api_url)
        data = response.json()
        dogs = jsonify(data)
        return dogs
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def index():
    data = get_dog_breeds()
    return render_template('index.html', data=data)
    

if __name__ == '__main__':
    app.run(debug=True)