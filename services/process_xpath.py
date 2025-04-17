import time

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config.logger import logger


def get_price_from_xpath(url: str, xpath: str):
    try:
        driver = uc.Chrome()
        driver.get(url)

        element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

        price = element.text.strip()
        if not price:
            return None

        return price
    except Exception as e:
        logger.error(f"Error while parsing: {e}")
        return None
    finally:
        driver.quit()