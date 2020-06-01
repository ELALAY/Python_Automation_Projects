from selenium import webdriver
from Insta_Func_Modules import logIn
from time import sleep

driver = webdriver.Chrome()
driver.get('https://instagram.com')

sleep(2)
logIn(driver)

homeBtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')
homeBtn.click()

notNow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notNow.click()
