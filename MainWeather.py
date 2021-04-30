import requests, json

def get_weather(city_name):
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   
   CITY = "Delhi"
   
   API_KEY = "b7fe0381393619a00359b8dedfc7511e"
   
   URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
   
   response = requests.get(URL)
   
   if response.status_code == 200:
      
      data = response.json()
      
      main = data['main']

      return{
         "temperature": float(main['temp']) - 273.15,
         "humidity": main['humidity'],
         "pressure": main['pressure'],
         "report": data['weather'][0]['description']
      }
   
   else:
      
      print("Error in the HTTP request")
      return {}

if __name__ == "__main__":
   print(get_weather("Delhi"))