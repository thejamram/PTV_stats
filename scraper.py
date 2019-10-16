from bs4 import BeautifulSoup 
import requests 
import re 
#import csv
#import pandas as pd

df = pd.DataFrame(columns=['Date','% delivered', '% on time'])

url = "https://www.ptv.vic.gov.au/footer/data-and-reporting/network-performance/daily-performance/" 
res = requests.get(url) 
soup = BeautifulSoup(res.text, 'html.parser') 
data = [] 
tableRows = soup.find_all('table')[0].find_all('tr') 

for row in tableRows[1:]:
  day = row.find_all(['td','th']) 
  ptv_date = day[0].text  
  ptv_pct_deliv = day[1].text
  ptv_ontime = day[2].text

  #df = df.append({'Date': ptv_date, '% delivered': ptv_pct_deliv, '% on time': ptv_ontime}, ignore_index = True)

  titles=['Date','% delivered', '% on time']
  data={'Date': ptv_date, '% delivered': ptv_pct_deliv, '% on time': ptv_ontime}
