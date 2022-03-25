from tkinter import *

import requests
import json



root = Tk()
def weather_info():
    info = Toplevel()

    info.geometry("600x400")

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = Location.get()
    API_KEY = "563b8223ff1fc3b63d12a1149e3e9a6a"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
    fi = f"{CITY:-^30}"
    snd = (f"Temperature: {temperature}")
    trd = (f"Humidity: {humidity}")
    frth = (f"Pressure: {pressure}")
    fth = (f"Weather Report: {report[0]['description']}")
   
    Label(info,text="Dynamic Weather App",font=("Helvetica", "20", "bold"),pady=10).pack(pady=10)
    Label(info,text=fi).pack()
    Label(info,text=snd).pack()
    Label(info,text=trd).pack()
    Label(info,text=frth).pack()
    Label(info,text=fth).pack()
    info.mainloop()


root.geometry("600x400")
root.title("Weather App")
root.iconbitmap("C:\\Users\\Dayn\\Desktop\\Work\\Codeyoung_DBMS\\Cloud.ico")


sunandcloud = PhotoImage(file = "C:\\Users\\Dayn\\Desktop\\Work\\Codeyoung_DBMS\\CloudyWeather.png")

DynamicLabel = Label(root,text="Dynamic Weather App",font=("Helvetica", "20", "bold"),pady=10)
DynamicLabel.pack(pady=10)
imagelabel = Label(root,image=sunandcloud,pady=10)
imagelabel.pack(pady=10)
Location = Entry(root,width=20,font=("Helvetica", "20"))
Location.pack(pady=10)
searchButton = Button(root,text=" Search ",command= weather_info)
searchButton.pack()
Button(root,text="Close",command=root.destroy).pack(pady=10)



root.mainloop()