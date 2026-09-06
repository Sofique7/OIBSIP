import requests

print("===== Basic Weather App =====")

city = input("Enter city name: ")

api_key = "68b0e93e93d025ed52f4c2712725aee3"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\n===== Weather Information =====")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Feels Like:", feels_like, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", weather)

else:
    print("City not found or API error.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)