import time
from bs4 import BeautifulSoup

#Carregando o arquivo
site_raw = open('site_compras.html', 'r', encoding='utf8').read()
attemps = 1000
time_average = 0

for _ in range(attemps):
    time_i = time.time()
    soup = BeautifulSoup(site_raw, 'html.parser')
    title = soup.h1.text
    time_f = time.time()
    time_average += (time_f-time_i)/attemps

print('Time with BeautifulSoap:', round(time_average, 4))