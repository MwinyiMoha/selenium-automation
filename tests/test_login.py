from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_faru_login(driver, cfg):
    url = f"{cfg.base_url}/login"
    driver.get(url)
    assert "Faru" in driver.title

    email_input = driver.find_element(By.ID, "qa-login-email")
    password_input = driver.find_element(By.ID, "qa-login-password")
    login_button = driver.find_element(By.ID, "qa-login-submit")

    email_input.send_keys(cfg.valid_email)
    password_input.send_keys(cfg.valid_password)
    login_button.click()

    user_icon = None
    try:
        user_icon = WebDriverWait(driver, cfg.default_wait_time).until(ec.element_to_be_clickable((By.CLASS_NAME, "anticon-user")))
    except TimeoutException as e:
        raise(e)

    user_icon.click()

    logout_item = None
    try:
        logout_item = WebDriverWait(driver, cfg.default_wait_time).until(ec.element_to_be_clickable((By.ID, "qa-logout")))
    except TimeoutException as e:
        raise(e)

    logout_item.click()
    sleep(2)
