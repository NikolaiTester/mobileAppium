from appium import webdriver
from appium.options.android import UiAutomator2Options



capabilities = dict(
    platformName='Android',
    automationName='uiautomator2'
)

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))