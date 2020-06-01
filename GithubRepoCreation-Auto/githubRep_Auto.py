from selenium import webdriver
from Github_Func_Module import log_in_Github, Create_New_Rep_Github, Submit_Creation

repName = input('Enter the name of your Repository >> ')

GIT_USERNAME = input('Github Username >> ')
GIT_PASSWORD = input('Github Password >> ')

driver = webdriver.Chrome()
driver.get('https://github.com')

sandwichBtn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/button')
sandwichBtn.click()

signimBtnForm = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
signimBtnForm.click()

#Log In Form
log_in_Github(driver, GIT_USERNAME, GIT_PASSWORD)

#New Repository
NewRepoBtn = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
NewRepoBtn.click()

#opened new Rep Name
Create_New_Rep_Github(driver, repName)

#Submit Creation
Submit_Creation(driver)
    