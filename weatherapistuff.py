#KEY = a2b19d469385f5622a185e5098e679a3
#
#
# https://openweathermap.org/price
# https://stackoverflow.com/questions/64192319/openweathemap-api-saying-temperature-is-like-282
#
#
import requests
#
#
#location = input("location: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q=Southampton&appid=a2b19d469385f5622a185e5098e679a3'
r = requests.get(url)
data = r.json()
print(data)
#

temp = data['main']
# use the key
print(temp)
