import time
from appium.webdriver.common.appiumby import AppiumBy
import allure
from configs.config import driver
from utils.utils import login_app, logout_app


def test_authorization_app():
    login_app()
    with allure.step('Проверка авторизации'):
        user = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Пользователь"]').text
        assert (user is not None, "No such element")
    driver.save_screenshot("/Users/hudyakov/Desktop/app7/screenshot/screenshotAuthorization.png")
    allure.attach.file('screenshot.png', attachment_type=allure.attachment_type.PNG)


def test_code():
    with allure.step('Открытие сканера'):
        scanner = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Сканер"]')
        scanner.click()
        time.sleep(5)
    with allure.step('Нажатие на кнопку ввести в ручную'):
        manuallybutton = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Ввести в ручную"]')
        manuallybutton.click()
        time.sleep(5)
    with allure.step('Ввод штрихкода'):
        manuallyscanner = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Штрихкод"]')
        manuallyscanner.click()
        manuallyscanner.send_keys("2000000061375")
    with allure.step('Нажатие кнопки получить данные '):
        getdatabutton = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Получить данные"]')
        getdatabutton.click()
        time.sleep(30)
    with allure.step('Проверка наличия штрихкода'):
        checkbutton = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Проверить наличие"]')
        assert (checkbutton is not None, "No such element")
    driver.save_screenshot("/Users/hudyakov/Desktop/app7/screenshot/screenshotCode.png")
    allure.attach.file('screenshot.png', attachment_type=allure.attachment_type.PNG)


def test_history():
    with allure.step('Переход в историю'):
        history = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="История"]')
        history.click()
        time.sleep(10)
    with allure.step('Проверка наличия ранне введенного кода'):
        numbercode = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="2000000061375"]')
        assert (numbercode is not None, "No such element")
    driver.save_screenshot("/Users/hudyakov/Desktop/app7/screenshot/screenshotHistory.png")
    allure.attach.file('screenshot.png', attachment_type=allure.attachment_type.PNG)


def test_delete_history():
    with allure.step('Нажатие на кнопку очистить историю'):
        deletebutton = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Очистить историю"]')
        deletebutton.click()
        time.sleep(10)
    with allure.step('Проверка отсутствия истории'):
        historyclear = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="История отсутствует"]')
        assert (historyclear is not None)
    driver.save_screenshot("/Users/hudyakov/Desktop/app7/screenshot/screenshotDeleteHistory.png")
    allure.attach.file('screenshot.png', attachment_type=allure.attachment_type.PNG)


def test_logout():
    logout_app()
    with allure.step('Проверка выхода из личного кабинета'):
        authorization = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Авторизация"]')
        assert (authorization is not None, "No such element")
    driver.save_screenshot("/Users/hudyakov/Desktop/app7/screenshot/screenshotLogout.png")
    allure.attach.file('screenshot.png', attachment_type=allure.attachment_type.PNG)