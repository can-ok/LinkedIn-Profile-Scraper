from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url="https://www.linkedin.com/login"

link="https://www.linkedin.com/in/sumnulu/"

driver = webdriver.Chrome()
driver.get(url)

username = driver.find_element_by_id("username")
#phone number or email
username.send_keys("0536561xxxx") #your phone/e-mail

#type password
password=driver.find_element_by_id("password") #password
password.send_keys("xxx")

#Submit button
username.submit()

# link
driver.get(link)

for i in range(2):#do it twice(why not)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #wait till load page
    time.sleep(2)#2sc


#ortalamak için
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2-100);")
time.sleep(2)

#click for show more skills
driver.execute_script("""var buttons=document.getElementsByClassName('pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid'); 
                    buttons[0].click();""")

#get page source
src=driver.page_source

#print(str(src))


#class: pv-skill-category-entity__name-text t-16 t-black t-bold

soup=BeautifulSoup(src,"html5lib")

skills=soup.find_all('span',{"class":"pv-skill-category-entity__name-text"})

for i in skills:
    print(i.text)