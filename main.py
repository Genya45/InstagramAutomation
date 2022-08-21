from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

#Данные логин и пароль
USERNAME = 'your_login'
PASSWORD = 'your_password'



#создаем объект браузера
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
options.add_argument("--headless")  #для работы в безоконном режиме, необходимо для удаленного сервера
#options.add_argument("--no-sandbox")

browser = webdriver.Chrome(options=options)

print("Start...")

browser.get('https://www.instagram.com/accounts/edit/')

sleep(3)   

#вводим логин
try:        
    username = browser.find_element(By.NAME, "username")
    username.send_keys(USERNAME)  
except:
    print("error login")

#вводим пароль
try:            
    password = browser.find_element(By.NAME, "password")
    password.send_keys(PASSWORD)
except:
    print("error password")

sleep(2)   

try:     
    #кликаем по кнопке входа    
    submit = browser.find_element(By.XPATH, "//*[@type='submit']")
    submit.click()
except:
    print("error button") 
submit = browser.find_element(By.XPATH, "//*[@type='submit']")
 
sleep(5)    
browser.get('https://www.instagram.com/accounts/edit/')
sleep(5)

#заполняем биографию
try:            
    username = browser.find_element(By.ID, "pepBio")
    username.clear()
    username = browser.find_element(By.ID, "pepBio")
    username.send_keys("*test message*")    #место для цитаты
    print(44)
    
except:
    print("error BIO")
sleep(5)   

#кликаем по кнопке BIO
try:            
    submit = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/article/form/div[10]/div/div/button')
    submit.click()
except:
    print("error button change BIO")    
