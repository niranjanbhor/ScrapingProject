import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


def main():
    """defining main function"""
    get_driver()


def get_driver():
    """getting driver"""
    try:
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument('--window-size=1920,1080')
        chromeoptions.headless = True
        chromeoptions.add_argument('--no-sandbox')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeoptions)
        get_ranking_wise_url(driver)
    except NoSuchElementException:
        pass


def get_ranking_wise_url(driver):
    pass


if __name__=="__main__":
    main()