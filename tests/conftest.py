import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from settings import Settings


config = Settings()

@pytest.fixture(scope="module")
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.headless = config.ci_env
    driver_options.set_capability("loggingPrefs", dict(performance="ALL"))

    _driver = webdriver.Chrome(options=driver_options)
    yield _driver

    _driver.quit()

@pytest.fixture(scope="module")
def cfg() -> Settings:
    return config
