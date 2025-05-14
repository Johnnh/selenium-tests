import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.mark.test
def test_google_homepage():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.wecreatedesign.co.uk")
    assert "Web design & web development in Reading, Berkshire. WeCreate." in driver.title
    print("Hello John")
    driver.quit()
