
# # install all the necessary libraries before running the program

import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm
import urllib.request
from bs4 import BeautifulSoup
import http.client


# In[ ]:


min_rnk = []
max_rnk = []
for z in range(1,10000000, 100):
    min_rnk.append(z)
    max_rnk.append(z+99)


# # Below Cell can take upto 1 hour to get and filter the whole data. Please insure a proper internet connection. Avarage time to extract 100 fields is 80-90 sec 

# In[4]:


disease_name = input("Enter the Disease name: \n")
df_covid = pd.DataFrame()
df = pd.DataFrame()
i=0
for i in tqdm(range(len(min_rnk))):
    CDC_BASE_URL = 'https://clinicaltrials.gov/api/query/full_studies?expr='+disease_name+'&min_rnk='+str(min_rnk[i])+'&max_rnk='+str(max_rnk[i])+'&fmt=xml'
    try:
        response = urllib.request.urlopen(CDC_BASE_URL)
        source_code = response.read()
    except http.client.InvalidURL:
        disease_name1 = disease_name.replace(' ','%20')
        CDC_BASE_URL = 'https://clinicaltrials.gov/api/query/full_studies?expr='+disease_name1+'&min_rnk='+str(min_rnk[i])+'&max_rnk='+str(max_rnk[i])+'&fmt=xml'
        response = urllib.request.urlopen(CDC_BASE_URL)
        source_code = response.read()
    soup = BeautifulSoup(source_code, 'html.parser')
    studies = soup.find_all('fullstudy')
    no_of_studies = soup.find('nstudiesreturned')
    if int(no_of_studies.text) != 0:
        for study in studies:
            fields=study.find_all('field')
            trial = {}
            for field in fields:
                trial[field.attrs['name']] = field.text
                df  = pd.DataFrame(trial,index=[i])
            i=i+1

            df_covid = pd.concat([df_covid, df])
    else:
        print("number of studies found:",len(df_covid))
        break


# # IMPORTANT: set innodb_strict_mode = 0 in my.ini file in MySQL or run "SET GLOBAL innodb_strict_mode = 0;" in MYSQL shell before running the next cell

# # DELETE DATABASE AND TABLE FROM MYSQL DATABASE with SAME NAME BEFORE RUNNING BELOW CODE


tableName   = str(disease_name)
# # Change "root" to your mysql username and "2486" with your mysql password
sqlEngine = create_engine('mysql://root:2486@localhost:3306/clinicaltrials?charset=utf8')

frame = df_covid.to_sql(tableName, sqlEngine, index=False, if_exists='replace')














# # Faster way to get csv file but the data type may require more filtering of the data before uploading to SQL database (Uncomment the below code before running)


"""disease_name = input("Enter the Disease name: \n")
data = []
file = []
for i in tqdm(range(len(min_rnk))):
    CDC_BASE_URL = 'https://clinicaltrials.gov/api/query/full_studies?expr='+disease_name+'&min_rnk='+str(min_rnk[i])+'&max_rnk='+str(max_rnk[i])+'&fmt=json'
    r = requests.get(CDC_BASE_URL)
    r.status_code
    j = json.loads(r.content)
    try:
        data.append(j['FullStudiesResponse']['FullStudies'])
    except KeyError:
        print("end of resuts:",i)
        break
for x in range(0,len(data)):
    for y in range(0,len(data[x])):
        file.append(data[x][y]) 
work = pd.json_normalize(file)
df_new = work.rename(columns=lambda s: s.split('.')[-1])
df_new1 = df_new.applymap(str)"""






