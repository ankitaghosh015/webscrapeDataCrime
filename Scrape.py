import csv
import requests
from bs4 import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
response=requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
#print(html)

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'stripe'})
#print(soup.prettify())
#print(table.prettify())

list_of_rows = []
#to convert the table rows to list so that data can be traversed
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '') #to replace &nbsp (non breaking space)
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
#print(list_of_rows)

outfile = open("./try.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)  #handy tool it has called writerows to dump out our list of lists