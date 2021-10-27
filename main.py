import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.nacionalquiniela.com/quiniela-nacional.php?del-dia=2021-10-25'
myfile = requests.get(url)
#open('./lot.html', 'wb').write(myfile.content)
html = BeautifulSoup(myfile.text, 'html.parser')

quotes_html = html.find_all('table', class_="table table-condensed")
#print(html)
#print(quotes_html)
table=html.find("table")
f=open('./lot.html', 'wb');
rows=list()
for row in table.findAll("tr"):
   rows.append(row)
   print(row)
   f.write(print(row))




div_main = html.div
tabla=html.find("table").find_all("tr")
#for i in range(2,21):
    #f.write(print(tabla[i]))

f.close()