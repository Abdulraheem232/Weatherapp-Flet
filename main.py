from flet import *
import requests

def main(page:Page):
    page.title = "Weather app flet"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    def getweather(e):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityname.value}&appid=dd19b95d4b73b36c6a53a3a47cca554e")
        data = response.json()

        city.value = data["name"]
        cityweather.value = f"{int(data["main"]["temp"] -273.15)}°C"
        humidity.value = f"{data["main"]["humidity"]}% humidity"
        suncondition.value = f"{data["weather"][0]["main"]}"

        if data["weather"][0]["description"] == "mist":
           weatherimage.src = "mist.png"
        elif data["weather"][0]["description"] == "rain":
            weatherimage.src = "rain.png"
        elif data["weather"][0]["description"] == "snow":
            weatherimage.src = "snow.png"
        elif data["weather"][0]["description"] == "wind":
            weatherimage.src = "wind.png"
        elif data["weather"][0]["description"] == "clear sky":
            weatherimage.src = "clear.png"
        elif data["weather"][0]["description"] == "overcast clouds":
            weatherimage.src = "clouds.png"
        elif data["weather"][0]["description"] == "drizzle":
            weatherimage.src = "drizzle.png"
        
        print(data["weather"][0])

        page.update()

    cityname =  TextField(value="Enter city name here.." , bgcolor="white" , color="black")
    getweatherbtn = Container(content=Text(value="Enter" , color="white" ,size="20"),width="100", height="44",alignment=alignment.center ,bgcolor="green", on_click=getweather)
    
    city = Text(value="City name" , size="50" , weight="bold")
    cityweather = Text(value="City temperature", size="30" , weight="bold")
    humidity = Text(value="Humidity", size="30" , weight="bold")
    suncondition = Text(value="Condition", size="30" , weight="bold")
    weatherimage = Image(src="clear.png" , width="170" , height="170")

    container = Container(bgcolor="#97b4ff",width=450 ,padding=20,height=500,border_radius=10,content=Column(controls=[
        Row(controls=[cityname,getweatherbtn] , spacing=10),
        city,
        cityweather,
        humidity,
        suncondition,
        weatherimage
    ],horizontal_alignment=CrossAxisAlignment.CENTER))

    page.add(container)

app(target=main)