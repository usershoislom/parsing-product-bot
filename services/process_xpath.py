import time

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_price_from_xpath(url: str, xpath: str):
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        element = driver.find_element(By.XPATH, xpath)

        if not element:
            print("Цена не найдена")
            return None

        return element.text
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return None
    finally:
        driver.quit()