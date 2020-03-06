import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome(executable_path='/Applications/Python 3.7/codes/chromedriver')
browser.set_page_load_timeout(30)
browser.implicitly_wait(30)

def login():
    try:
        browser.get('https://www.trainwithmeapp.com/home')
        WebDriverWait(browser, 10).until(EC.title_is(("TrainWithMe")))
  
        wait = WebDriverWait(browser, 10)
        men_menu = wait.until(EC.visibility_of_element_located((By.ID, "email-login-input")))
        ActionChains(browser).move_to_element(men_menu).perform()
        
        login = browser.find_element_by_id("email-login-input")
        password = browser.find_element_by_id("password-input")
        login.send_keys("selenium@trainwithmeapp.com")
        password.send_keys("password")
        browser.find_element_by_id("email-login-button").click()
    except:
        print("fail to login")
        browser.quit()


def openProgram():
    try:
        wait = WebDriverWait(browser, 10)
        men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-id='program-name']")))
        ActionChains(browser).move_to_element(men_menu).perform()
        
        openButton = browser.find_elements_by_xpath("//*[@data-id='program-name']")
        openButton[0].click()
    except:
        print("fail to open a program")



def programsCancel():
    try:
        wait = WebDriverWait(browser, 10)
        men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-id='program-options-icon']")))
        ActionChains(browser).move_to_element(men_menu).perform()

        button = browser.find_elements_by_xpath("//*[@data-id='program-options-icon']")
        button[0].click()
        button = browser.find_elements_by_xpath("//*[@data-id='cancel-program-menu-item']")
        button[0].click()
        button = browser.find_element_by_xpath("//*[@data-id='cancel-program-modal']//*[@placeholder='Enter client name...']")
    except:
        print("fail to open cancel modal")
    try:
        button.send_keys("Selenium Coelho")
        button.send_keys(Keys.ENTER)
        
        button = browser.find_elements_by_xpath("//*[@data-id='cancel-program-modal']//*[@data-id='assigned-program-check']")
        button[0].click()
    except:
        print("fail to select client")
    try:
        button = browser.find_elements_by_xpath("//*[@data-id='cancel-program-modal']//*[@data-id='remove-button']")
        button[0].click()
        
        button = browser.find_elements_by_xpath("//*[@data-ix='close-modal']")
        button[0].click()
    except:
        print("fail to cancel")
    try:
        button = browser.find_elements_by_xpath("//*[@data-id='program-options-icon']")
        button[0].click()
        button = browser.find_elements_by_xpath("//*[@data-id='cancel-program-menu-item']")
        button[0].click()
        
        
        button = browser.find_element_by_xpath("//*[@data-id='cancel-program-modal']//*[@placeholder='Enter client name...']")
        button.send_keys("Selenium Coelho")
        button.send_keys(Keys.ENTER)
        time.sleep(1)
        
        isdDleted = browser.find_element_by_xpath(("//*[@data-id='cancel-program-modal']//*[@data-id='empty-assignment-list']"))
        
        if(isdDleted.is_displayed()):
            print("Cancel program working")
        else:
            print("Cancel program not working")
    except:
        print("fail verify cancel")



def assignProgram():
    wait = WebDriverWait(browser, 10)
    men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-id='assign-button']")))
    ActionChains(browser).move_to_element(men_menu).perform()
    
    button = browser.find_elements_by_xpath("//*[@data-id='assign-button']")
    button[0].click()
    
    wait = WebDriverWait(browser, 10)
    men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-id='assign-modal']//*[@placeholder='Add client or group name...']")))
    ActionChains(browser).move_to_element(men_menu).perform()
    
    button = browser.find_element_by_xpath("//*[@data-id='assign-modal']//*[@placeholder='Add client or group name...']")
    button.send_keys("Selenium Coelho")
    button.send_keys(Keys.ENTER)
    button = browser.find_element_by_xpath("//*[@data-id='assign-modal']//*[@data-id='assign-button']")
    button.click()
    
    

login()
assignProgram()
time.sleep(5)
programsCancel()
browser.quit()











