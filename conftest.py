import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1200")
    firefox_options.add_argument("--height=900")
    firefox_options.set_preference("browser.privatebrowsing.autostart", True)
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()
