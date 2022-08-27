import json 
import requests

from bs4 import BeautifulSoup
responce=requests.get('https://www.imdb.com/title/tt0066763/')
soup=BeautifulSoup(responce.content,'html.parser')
con=soup.find('script',type='application/ld+json').text
a=json.loads(con)
dic={}
for key in a:
    if key=='url':
        b=a[key].strip('/title/')
        dic['id']=b
with open('8th_task.json','w')as f:
    json.dump(dic,f)
        
        
