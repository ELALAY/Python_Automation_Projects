from instaAcc import USERNAME, PW

def logIn(driver):
    logUser = driver.find_element_by_xpath('//*[@id="react-root"]'
    +'/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    logUser.send_keys(USERNAME)

    logPw = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/'
        +'article/div[2]/div[1]/div/form/div[3]/div/label/input')
    logPw.send_keys(PW)

    logBtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/'
        +'article/div[2]/div[1]/div/form/div[4]/button')
    logBtn.click()