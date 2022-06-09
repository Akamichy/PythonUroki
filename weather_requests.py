import requests
from bs4 import BeautifulSoup as BS

hdr = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.0.0 Mobile Safari/537.36'}
url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
r = requests.get(url, headers=hdr, timeout=10)
soup = BS(r.content, 'html.parser')
table = soup.find('tbody').find_all('tr')
result = {}

for tr in table:
    table_cell = tr.find_all('td')
    result[table_cell[0].text] = [x.text for x in table_cell[1:]]
stations = '''
Heltermaa	
Jõgeva	
Jõhvi	
Kihnu	
Kunda
Kuressaare linn		
Kuusiku
Lääne-Nigula
Narva
Pakri
Pärnu
Ristna
Roomassaare
Ruhnu
Sõrve
Tallinn-Harku
Tartu-Tõravere
Tiirikoja
Tooma
Türi
Valga
Viljandi
Vilsandi
Virtsu	
Võru
Väike-Maarja
Peipsi poijaam	
'''
print('Hello, here is the list of all stations available!\n' + stations)

station_name = input('Please, enter the station name: ')

def city():
    # global station_name
    print(station_name, 'average air temperature is', (result[station_name][1]) + '°C. \n'
'Minimum ground temperature is', (result[station_name][3]) + '°C. \n'
'Minimum temperature 2cm above the ground is', (result[station_name][4]) + '°C. \n'
'Average relative humidity is', (result[station_name][5]) + '%. \n'
'Average wind speed is', (result[station_name][7]), 'm/s \n'
'Precipitation is about', (result[station_name][9]) ,'mm \n'
'Duration of sunshine is', (result[station_name][10]),'h')
city()





# 1st try, it did'nt work
# user_choice = None
# while True:
#     if not user_choice:
#         while True:
#             user_choice=input('Please, choose:\n'
#                         '1.Air temperature (° C)\n'
#                         '2.Minimum ground temperature (° C)\n'
#                         '3.Minimum temperature 2cm above the ground (° C)\n'
#                         '4.Relative humidity (%)\n'
#                         '5.Wind speed (m / s)\n'
#                         '6.Precipitation (mm)\n'
#                         '7.Duration of sunshine (h)\n'
#                         '8.Exit\n'
#                         '--->')
#             if user_choice == 1:
#                 match1 = soup.find('td', 'Vilsandi').text
#                 print(match1)
