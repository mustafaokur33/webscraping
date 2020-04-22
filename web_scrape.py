# - Gather __all detail data__ of Netherlands municipalities from [wikipedia](https://en.wikipedia.org/wiki/List_of_municipalities_of_the_Netherlands)
# - Save them to CSV file


# importing the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# defining the url that I want to scrape
url='https://en.wikipedia.org/wiki/List_of_municipalities_of_the_Netherlands'
r=requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
table=soup.find('table',{'class':'wikitable plainrowheaders sortable'})
rows=table.find_all('tr')[1:]

# defining the lists that will be used to store the datas
municipalities=[]
cbs_codes=[]
provinces=[]
populations=[]
pop_densities=[]
land_areas=[]

# with a for loop I will try to get all the datas from the table 
for row in rows:
    municipality=row.find('th').text.strip()
    municipalities.append(municipality)

    cbs_code=row.find_all('td')[0].text.strip()
    cbs_codes.append(cbs_code)

    province=row.find_all('td')[1].text.strip()
    provinces.append(province)

    population=row.find_all('td')[2].text.strip()
    populations.append(population)

    pop_density=row.find_all('td')[3].text.strip()
    pop_densities.append(pop_density)
    
    land_area=row.find_all('td')[4].text.strip()
    land_areas.append(land_area)

#Creating the dataframe
df = pd.DataFrame({'Municipality':municipalities,'CBS Code':cbs_codes,'Province':provinces,
                   'Population':populations,'Population Density':pop_densities,'Land Area':land_areas})
df.head()

#Saving the scraped data to CSV file
df.to_csv('Municipalities_of_NL.csv')

