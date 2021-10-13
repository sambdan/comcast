# import required modules
import requests, json

# Enter your API key here
api_key = "de9cf3829854b386a2c8d684e6ae0fd4"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = raw_input("Enter city : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

        y = x["main"]
        current_temperature = 9/5*(y["temp"]-273) +32
        z = x["weather"]

        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in fahrenheit unit) = " +
                                        str(current_temperature) +
                "\n description = " +
                                        str(weather_description))

else:
        print("City Not Found ")