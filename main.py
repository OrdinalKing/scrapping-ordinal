from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    first = 0
    user_input = input("Please enter something: ")
    try:
        driver.get("https://www.ord.io/13058521")

        for i in range(20):
            connect_button = driver.find_elements(By.TAG_NAME, 'button')[2]
            driver.execute_script("arguments[0].click();",connect_button)
            time.sleep(1)
            unisat_button = driver.find_elements(By.TAG_NAME, 'button')[18]

            driver.execute_script("arguments[0].click();",unisat_button)
            
            if first == 0:
                time.sleep(10)
                first = 1
            else:
                time.sleep(2)
            favorite_button = driver.find_elements(By.TAG_NAME, 'button')[6]
            driver.execute_script("arguments[0].click();",favorite_button)
            time.sleep(1)

            address_button = driver.find_elements(By.TAG_NAME, 'button')[2]
            driver.execute_script("arguments[0].click();",address_button)
            time.sleep(1)
            signout_button = driver.find_elements(By.TAG_NAME, 'button')[3]
            driver.execute_script("arguments[0].click();",signout_button)
            time.sleep(1)

        # for i in range(len(unisat_button)):
        #     print(i)
        #     print(unisat_button[i].text)
        user_input = input("Please enter something: ")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
