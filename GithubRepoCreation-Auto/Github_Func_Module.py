from selenium import webdriver
import time 

#Python_Automation_Projects
#GITHUB Login
def log_in_Github(driver, GIT_USERNAME, GIT_PASSWORD):
    username_field_login = driver.find_element_by_xpath('//*[@id="login_field"]')
    username_field_login.send_keys(GIT_USERNAME)

    paaword_field_login = driver.find_element_by_xpath('//*[@id="password"]')
    paaword_field_login.send_keys(GIT_PASSWORD)

    time.sleep(1)
    LoginFinalSubmition = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
    LoginFinalSubmition.click()

    return


def Create_New_Rep_Github(driver, repName):
    inpRepName = driver.find_element_by_xpath('//*[@id="repository_name"]')
    inpRepName.send_keys(repName)

    initReadMeCheck = driver.find_element_by_xpath('//*[@id="repository_auto_init"]')
    initReadMeCheck.click()
   
    return

def Submit_Creation(driver):
    time.sleep(1)
    createRepBtn = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
    createRepBtn.click()

    return

