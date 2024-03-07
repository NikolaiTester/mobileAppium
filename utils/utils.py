import time
from configs.config import driver
from appium.webdriver.common.appiumby import AppiumBy


def login_app():
    login = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Логин"]')
    login.click()
    login.send_keys("ross")
    password = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Пароль"]')
    password.click()
    password.send_keys("wa7kggbj")
    loginbuttor = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Войти"]')
    loginbuttor.click()
    time.sleep(15)

def logout_app():
    logoutbutton = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Выход"]')
    logoutbutton.click()
    time.sleep(5)