"""
Basic test
"""
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_smoke():
    """
    SMK-1. Smoke test
    """
    
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    #chrome_options.add_argument("--headless")
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service()
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://testqastudio.me/"
    driver.get(url=url)
		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    # чтобы просмотреть детали
    element = driver.find_element(by=By.CSS_SELECTOR, value='[class="tab-best_sellers "]')
    element.click()
    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]')
    element.click()
    sku = driver.find_element(by=By.CSS_SELECTOR, value='[class="sku"]')
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"
    
		