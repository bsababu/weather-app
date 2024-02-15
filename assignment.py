'''  '''


import requests
from tkinter import *
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk
from urllib.request import urlopen

api_key='772eeb78e737a08931a04b86c6341c32'
iconss = 'http://openweathermap.org/img/w/{}.png'
# url ='https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid='
weather_url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def index():
    root = Tk()
    today = date.today()
    root.title("City Weather App")
    root.geometry('500x350')
    city_name = StringVar()
    enter_city = Entry(root, textvariable=city_name)
    enter_city.pack()
    lbl_loc = Label(root,text="Enter the city name", font=('italic',12),fg='#ffd966')
    lbl_loc.pack()
    current_temp_lbl = Label(root,text='Current Temperature')
    current_temp_lbl.pack()
    current_tm_lbl = Label(root,text=f'Current date: {today}')
    current_tm_lbl.pack()


    def getCity(city):
        try:
            response = requests.get(weather_url.format(city,api_key))
            jason = response.json()
            city_name=jason['name']
            country=jason['sys']['country']
            temp=jason['main']['temp'] - 273.15
            icon=jason['weather'][0]['icon']
            img_icon = f'http://openweathermap.org/img/w/{icon}.png'
            weather_info=jason['weather'][0]['main']
            # print(jason)
            result = (city_name,country,temp,img_icon,weather_info)
            return result
        except ValueError as e:
            print(e)

    
    def searchFunc():
        city = city_name.get()
        weather = getCity(city)
        if weather:
            lbl_loc['text'] = '{}.{}'.format(weather[0],weather[1])
            
            imageurl = weather[3]

            img = Image.open(urlopen(imageurl))

            test = ImageTk.PhotoImage(img)
            img_lbl = Label(image=test)
            img_lbl.image = test
            img_lbl.place(x=225, y=125)
            current_temp_lbl['text'] = '{0:2f}°'.format(weather[2])
            search_btn['text']='The icon below'
        else:
            messagebox.showerror('Err',' {} not found'.format(city))

    search_btn = Button(root,text="Search", command=searchFunc)
    #search_btn.grid(column=1, row=0)
    search_btn.pack()
    root.mainloop() # Execute Tkinter


if __name__=="__main__":
    print(index())