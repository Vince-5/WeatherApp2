from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = 'your_api_key_here'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

def getweather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_celsius, weather1]
        return final
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        city = request.form['city']
        weather = getweather(city)
        if weather:
            return render_template('index.html', weather=weather)
        else:
            return render_template('index.html', error="Cannot find city")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
