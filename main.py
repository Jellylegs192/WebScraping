import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Ottma/OneDrive/Desktop/Year UP/Mod 3/CIS 403/Week 18/Project4/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.find_all(attrs='blog-card__content-wrapper'):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs='blog-card__date-wrapper'):
    date = b.find('p')
    if date not in results:
        other_results.append(name.text)
df = pd.DataFrame({'Names':results,'Dates':other_results})

df.to_csv('names.csv',index=False, encoding='utf-8')
