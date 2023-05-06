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
# print(weather.text)
week_weather = soup.find('ul',{'class':'week_list'})
week_weather_text = week_weather.text.strip()
print(week_weather_text)
# week_text = []
# for i in range(len(week_weather_text)):
#     if week_weather_text[i] != '':
#         week_text.append(week_weather_text[i])
# weekly_temp = []
# daily_temp = []
# for i in range(len(week_text)):
#     daily_temp = []
#     if "최고기온" in week_text[i]:
#         daily_temp.append(week_text[i][5:-2])
#     elif "최저기온" in week_text[i]:
#         daily_temp.append(week_text[i][5:-2])

#     weekly_temp.append(daily_temp)
#     if len(daily_temp) == 2:
#         daily_temp = []

# print(weekly_temp)