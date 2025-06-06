import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.mark.develop
def test_google_homepage():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
