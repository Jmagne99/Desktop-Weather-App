import tkinter as tk
import requests
import time

#get data from api
def get_weather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=b8335e2cef2a52015de0da96b2fe1952"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temperature = int(json_data["main"]["temp"] - 273.15)  # (-273.15 used to convert to celcius)
    min_temperature = int(json_data["main"]["temp_min"] - 273.15)
    max_temperature = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] - 21600)) 

    final_info = condition + "\n" + str(temperature) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temperature) + "\n" + "Min Temp: " + str(min_temperature) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "WindSpeed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset 
    
    label1.config(text = final_info)
    label2.config(text = final_data)




canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

#Fonts
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas,justify='center', font =t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>',get_weather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()