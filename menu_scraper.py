from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import json
import os
import pandas as pd

wines = pd.DataFrame(columns = ['wine_name','winery','grape_type','region']) 

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver_91")

driver = webdriver.Chrome(DRIVER_BIN)

driver.get('https://www.vivino.com/')

def search_for_wine(wine_name):
    """
    Search for wine in vivino.
    """
    search_wine = driver.find_element_by_xpath('//*[@id="navigation-container"]/div/nav/div[1]/div/div/div[1]/form/input')
    search_wine.send_keys(wine_name,Keys.ENTER)

    time.sleep(0.5)

def first_wine_extract_info(wines):
    """
    Extract wine information from the first wine on the search list.
    """
    wine_element = driver.find_element_by_xpath('/html/body/div[3]/section[1]/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/span[1]/a/span')
    wine_name = wine_element.text

    driver.find_element_by_xpath('/html/body/div[3]/section[1]/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/span[1]/a/span').click()
    time.sleep(0.5)

    y = 1000
    for timer in range(0,8):
        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        y += 1000  
        time.sleep(1)

    light_bold = driver.find_element_by_xpath('//*[@id="wine-page-lower-section"]/div[1]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/div/span')
    percentage = light_bold.value_of_css_property('left')
    print(percentage)

def main():
    search_for_wine('cloudy bay souvignon blanc')
    first_wine_extract_info(wines)

if __name__ == "__main__":
    main()
