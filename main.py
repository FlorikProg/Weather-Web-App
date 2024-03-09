from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form['input_field_name']
        # сохраняем введенные данные в переменную
        print('Введенные данные:', input_data)


        city = input_data  # Название города
        api_key = "Key"  # Ваш API ключ OpenWeatherMap

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        return render_template('html.html', temp=temperature)
    
    return render_template('html.html')


        

if __name__ == ("__main__"):
    app.run(host="0.0.0.0")
