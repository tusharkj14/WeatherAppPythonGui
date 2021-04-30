from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from MainWeather import get_weather

Builder.load_file('KVDesign.kv')
Window.size = (500, 200)
class MyLayout(Widget):
    
    def press(self):
        city = self.ids.city.text
        temp_details = get_weather(str(city))
        if (city!="") & (temp_details!={}): 
            self.ids.temp_city.text = f'{city}\'s Weather Report:\n'
            self.ids.temp_city.text += f'Temperature - {temp_details["temperature"]} degree Celsius\n'
            self.ids.temp_city.text += f'Humidity - {temp_details["humidity"]} %\n'
            self.ids.temp_city.text += f'Atm Pressure - {temp_details["pressure"]} hPa\n'
            self.ids.temp_city.text += f'Description - {temp_details["report"]}'
        
        elif (temp_details=={}):
            self.ids.temp_city.text = f'{city}\'s data not found'
            
        self.ids.city.text = ""

class WeatherApp(App):

    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()

if __name__ == "__main__":
    WeatherApp().run()


