import time
import re

#Carregando o arquivo
site_raw = open('site_governo.html', 'r', encoding='utf8').read()
attemps = 1000
time_average = 0

for _ in range(attemps):
    time_i = time.time()
    regex = re.search(
        r'<h1[^>]+>(?P<title>[^<]+)', site_raw, 
        flags=re.DOTALL|re.IGNORECASE
    ).group('title')
    time_f = time.time()
    time_average += (time_f-time_i)/attemps

print('Time with regex:', round(time_average, 4))