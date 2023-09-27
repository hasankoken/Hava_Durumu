import requests
while True:
   API_KEY = "ce25b36e5789d65062d9b2085394b938"
   CITY = input("Enter your city :")
   URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
   response = requests.get(URL)
   if response.status_code == 200:
      data = response.json()
      main = data['main']
      temperature = main['temp']
      temperature=(temperature-273.15)
      humidity = main['humidity']
      pressure = main['pressure']
      report = data['weather']
      print(f"{CITY:-^30}")
      print(f"Sıcaklık: {temperature}")
      print(f"Nem: % {humidity}")
      print(f"Basınç: {pressure}")
      print(f"Hava Raporu: {report[0]['description']}")
   else:
      print("Error in the HTTP request")
