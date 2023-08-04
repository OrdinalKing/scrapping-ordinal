from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    #user_input = input("Please enter something: ")
    try:
        driver.get("https://www.ord.io/21316151")
        connect_button = driver.find_elements(By.TAG_NAME, 'button')[2]
        driver.execute_script("arguments[0].click();",connect_button)
        time.sleep(1)
        unisat_button = driver.find_elements(By.TAG_NAME, 'button')[18]
        # for i in range(len(unisat_button)):
        #     print(i)
        #     print(unisat_button[i].text)
        driver.execute_script("arguments[0].click();",unisat_button)
        
        #connect_button.click()
        user_input = input("Please enter something: ")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
