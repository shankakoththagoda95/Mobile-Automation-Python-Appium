from appium import webdriver

def get_driver(platform, app_path, device_name, version):
    desired_caps = {
        "platformName": platform,
        "platformVersion": version,
        "deviceName": device_name,
        "app": app_path,
        "automationName": "UiAutomator2" if platform == "Android" else "XCUITest",
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
