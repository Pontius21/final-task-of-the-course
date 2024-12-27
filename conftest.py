from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    # Создаем объект ChromeOptions для настройки языка
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Инициализируем браузер с заданными опциями
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()
