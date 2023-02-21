import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


def main():
    """defining main function"""
    get_driver()


def get_driver():
    """getting driver"""
    try:
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument('--window-size=1920,1080')
        chromeoptions.headless = False
        chromeoptions.add_argument('--no-sandbox')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeoptions)
        get_teamwise_url(driver)
    except NoSuchElementException:
        pass


def get_teamwise_url(driver):
    """ Using url for scrapping team wise player Info"""
    try:
        driver.get("https://247sports.com/college/football/recruiting/")  # website path
        time.sleep(5)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[text()='Team Rankings']").click()  # team Ranking path
        driver.find_element(By.XPATH, "/html/body/section[1]/section/div/section/header/div/div[1]/a[1]").click()
        driver.find_element(By.XPATH,
                            "/html/body/section[1]/section/div/section/header/div/div[1]/div[1]/ul/li[4]/a").click()
        global team
        team = driver.find_elements(By.XPATH,
                                    "/html/body/section[1]/section/div/section/section/div/ul/li[*]/div[1]/div[3]/a")  # team path
        templist = []
        for n in range(0, 50):
            team = driver.find_elements(By.XPATH,
                                        "/html/body/section[1]/section/div/section/section/div/ul/li[*]/div[1]/div[3]/a")  # team path
            print(n)
            driver.implicitly_wait(10)
            team[n].click()
            time.sleep(2)
            driver.find_element(By.XPATH,
                                "/html/body/section[1]/section/div[1]/section[2]/header/div/div[1]/a[3]").click()  # team select
            driver.find_element(By.XPATH, "//a[contains(@class,'yr_plldwn tltp_click tltp_bm')]").click()  # dropdown
            driver.find_element(By.XPATH,
                                "/html/body/section[1]/section/div[1]/section[2]/header/div/div[1]/a[3]").click()  # Select team
            driver.find_element(By.XPATH,
                                "/html/body/section[1]/section/div[1]/section[2]/header/div/div[1]/div[3]/ul/li[1]/a").click()  # commit
            link = driver.find_elements(By.XPATH,
                                        '/html/body/section[1]/section/div[1]/section[2]/section/div/ul/li[*]/div[1]/div[2]/a')  # player
            """Iterating Player List"""
            for info in link[0:50]:
                info.click()
                time.sleep(2)
                window2 = driver.window_handles[1]
                driver.switch_to.window(window2)
                data = get_teamwise_player_attributes(driver)
                templist.append(data)
                driver.close()
                window3 = driver.window_handles[0]
                driver.switch_to.window(window3)
            df = pd.DataFrame(templist)
            df.to_csv('final_output_file.csv', mode='a', index=False, encoding='utf-8', header=False)
            driver.back()
            driver.back()
            time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.quit()
    except NoSuchElementException:
        pass


def get_teamwise_player_attributes(driver):
    '''defining function to scrapping team wise player attributes'''
    name_data = []
    try:
        # this is name scrapping using the name Xpath
        name = driver.find_elements(By.XPATH, "/html/body/section[1]/section/div/section/header/div[1]/h1")
        name_data = [p.text for p in name]
        print(name_data)
        time.sleep(5)

        # image scraping using the image Xpath
        image_data = []
        try:
            image = driver.find_elements(By.XPATH,
                                         "/html/body/section[1]/section/div/section/header/div[1]/div[1]/div/img")
            image_data = [k.get_attribute('src') for k in image]
            print(image_data)
            time.sleep(5)
        except NoSuchElementException:
            pass

            # prospect info scraping
            prospect_info_data = []
        try:
            prospect_info = driver.find_elements(By.XPATH,
                                                 "/html/body/section[1]/section/div/section/header/div[1]/ul[1]/li[*]/span[2]")
            prospect_info_data = [k.text for k in prospect_info]
            print(prospect_info_data)
            time.sleep(5)
        except NoSuchElementException:
            pass

            # School data scraping
        try:
            junior_college = driver.find_element(By.XPATH,
                                                 "/html/body/section[1]/section/div/section/header/div[1]/ul[3]/li[1]/div/span[2]").text

            school = driver.find_elements(By.XPATH,
                                          "/html/body/section[1]/section/div/section/header/div[1]/ul[3]/li[*]/span[2]")
            school_data = [k.text for k in school]
            school_data.insert(0, junior_college)
            print(school_data)

        except NoSuchElementException:
            school = driver.find_elements(By.XPATH,
                                          "/html/body/section[1]/section/div/section/header/div[1]/ul[3]/li[*]/span[2]")
            school_data = [k.text for k in school]
            print(school_data)
            time.sleep(5)
            # offers scraping
            offers_data = []
        try:
            offers = driver.find_element(By.XPATH,
                                         "/html/body/section[1]/section/div/section/section/footer/div/span[1]")
            offers_data = [offers.get_attribute('textContent')]
            time.sleep(5)
        except NoSuchElementException:
            pass



    except NoSuchElementException:
        pass


if __name__ == "__main__":
    main()
