import requests

api_token = '916afbc9f14fefe8403b4bb1b3bb572d'
url = 'http://api.openweathermap.org/data/2.5/weather'
country = input("enter country: ")
language = input("select language ru/en: ")
settings = dict(q = country, type = 'like', units = 'metric', lang = language, APPID = api_token)
res = requests.get(url, params = settings)
if language == "ru":
    data = res.json()
    print("Небо:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Ощущение температуры:", data['main']['feels_like'])
    print("Скороть ветра:", data['wind']['speed'])
else:
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("Temp:", data['main']['temp'])
    print("sensе of temperature:", data['main']['feels_like'])
    print("Wind speed:", data['wind']['speed'])