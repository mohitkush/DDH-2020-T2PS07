import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
import json
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://go.drugbank.com/covid-19#clinical-trials")
drugs = []
phase = []
time.sleep(10)
i=0
for i in range(0,278):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    que = soup.find_all('table',{'aria-describedby':'DataTables_Table_1_info'})
    co = que[0].find('tbody').find_all('tr')
    for x in co:
        name=x.find_all('td')[1].text
        ph = x.find_all('td')[4].text
        drugs.append(name)
        phase.append(ph)
    i+=1
    try:
        driver.find_element_by_xpath('/html/body/main/div/div[2]/dl/dd[3]/div[2]/div[3]/div[2]/div/ul/li[9]').click()
    except ElementClickInterceptedException:
        time.sleep(8)
        driver.find_element_by_xpath('/html/body/main/div/div[2]/dl/dd[3]/div[2]/div[3]/div[2]/div/ul/li[9]').click()
        
d={'Drug':drugs, 'Phase': phase}
df=pd.DataFrame(data=d, columns = ['Drug', 'Phase'])
df.to_csv(r"C:\Users\hp\Desktop\drugsANDphase.csv", index=False)