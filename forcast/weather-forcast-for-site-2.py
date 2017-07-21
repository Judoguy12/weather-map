import pyowm
from twython import Twython
import time,datetime
from time import sleep
while 1 ==1:
    
    dateString = "%Y/%m/%d %H:%M:%S"
    time = datetime.datetime.now().strftime(dateString)



    from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    twitter = Twython(
            consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    lat = 52.27
    lon = -2.15
    owm = pyowm.OWM('f5f228ca75823de879e024d518f7a8cf')
    observation = owm.weather_at_place("Saint-Jean-de-Monts, fr")
    w = observation.get_weather()
    sts = w.get_detailed_status()
    wind = w.get_wind()
    temp = w.get_temperature('celsius').get('temp')
    rain = w.get_rain()
    tomorrow = pyowm.timeutils.tomorrow()
    humid = w.get_humidity()
    sunrise = w.get_sunrise_time('iso')
    sunset = w.get_sunset_time('iso')
    pressure = w.get_pressure()
    fc = owm.daily_forecast('Saint-Jean-de-Monts, fr', limit = 6)
    f = fc.get_forecast()
    print('Sunrise: '+str(sunrise))
    print('Weather: ')
    print(sts)
    print('Wind: ')
    print(wind)
    print('Temperature, Celcius: ')
    print(temp)
    print('Rain: ')
    print(rain)
    print('Humidity: ')
    print(humid)
    print('Pressure: ')
    print(pressure)
    print('Sunset: '+str(sunset))
    print("Forcast: ")
    for weather in f:
        print(weather.get_reference_time('iso'),weather.get_status())

        
    def forcast():
        for weather in f:
            print(weather.get_reference_time('iso'),weather.get_status())





    text = "1 Saint-Jean. Status:"+str(sts)+"Wind:"+str(wind)+',Temperature:'+str(temp)+',Rain:'+str(rain)+str(time) 
    text2 = '2 Saint-Jean. Humidity and pressure data for Saint-Jean. Humidity:'+str(humid)+',Pressure:'+str(pressure)+str(time)
    text3 = "3 Saint-Jean. Sunrise and sunset times: Sunrise:"+str(sunrise)+',Sunset:'+str(sunset)+str(time)
    text4 = "4 Saint-Jean. The 6 day forcast is: " +str(forcast)

    message = text
    twitter.update_status(status = message)

    message2 = text2
    twitter.update_status(status = message2)

    message3 = text3
    twitter.update_status(status = message3)
    sleep(43200)

