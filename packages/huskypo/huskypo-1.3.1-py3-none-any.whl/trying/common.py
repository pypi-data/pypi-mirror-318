import os
import time

import allure

from selenium.webdriver.remote.webdriver import WebDriver


class Path:
    REPORTS_DIR = os.path.abspath('./reports')
    SCREENSHOT_DIR = os.path.abspath('./screenshot')


class Screenshot:
    COUNT = 1


def save_screenshot(
        driver: WebDriver, image_dir: str, image_name: str, wait: int = 3):
    """
    取得截圖
    :param image_dir: 截圖欲存放在screenshot資料夾底下的某個資料夾路徑或名稱
    :param image_name: 截圖名稱，如欲附加檔案類型只能為.png
    """
    time.sleep(wait)
    image_dir = os.path.join(Path.SCREENSHOT_DIR, image_dir)
    os.makedirs(image_dir, exist_ok=True)
    if '.png' not in image_name:
        image_name = image_name + '.png'
    elif '.' in image_name and 'png' not in image_name:
        raise ValueError
    image_name = f'{Screenshot.COUNT}_{image_name}'
    image_path = os.path.join(image_dir, image_name)
    driver.save_screenshot(image_path)
    allure.attach.file(image_path, image_path, allure.attachment_type.JPG)
    Screenshot.COUNT += 1
