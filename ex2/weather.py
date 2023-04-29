import requests
from bs4 import BeautifulSoup
print("test")
url = "https://weather.naver.com"
response=requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
temperature = soup.find('strong',{'class':'current'})
temperature = float(temperature.text[6:-2])
print(temperature)
weather = soup.find('p',{'class':'summary'})
print(weather.text)
week_weather = soup.find('ul',{'class':'week_list'})
week_weather_text = week_weather.text.strip().split('\n')
week_text = []
for i in range(len(week_weather_text)):
    if week_weather_text[i] != '':
        week_text.append(week_weather_text[i])
print(week_text)