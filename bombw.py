#HELLO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')
driver.maximize_window()
sleep(3)
#sleep function sleeps for 3 milli seconds.
name = input("enter the username:")
mssg =input ('enter messg to send:')
number=int(input("enter the count:"))

input('Enter any key after scanning QR code')
user = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
user.click()

for i in range(number):
    msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    msg_box.send_keys(mssg)
    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button/span")
    button.click()
    
print("success")    
#driver.close()
