import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config.logger import logger

import uuid


def get_price_from_xpath(url: str, xpath: str):
    driver = None
    try:
        options = uc.ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-application-cache")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--lang=ru-RU,ru")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )

        driver = uc.Chrome(options)
        driver.get(url)
        driver.save_screenshot(f"screens/{url[:10]}_{str(uuid.uuid4())[:8]}.png")
        element = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath))
        )

        price = element.text.strip()
        if not price:
            return None

        return price
    except Exception as e:
        import traceback

        logger.error(traceback.format_exc())
        return None
    finally:
        if driver:
            driver.quit()
