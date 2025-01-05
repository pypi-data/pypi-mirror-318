import os
import time

import allure
from huskypo import Page as HuskyPOPage

from trying.common import Path, Screenshot


class Page(HuskyPOPage):

    def save_screenshot(self, image_dir: str, image_name: str, image_count: bool = True, wait: int = 1):
        """
        取得截圖
        :param image_dir: 截圖欲存放在screenshot資料夾底下的某個資料夾路徑或名稱
        :param image_name: 截圖名稱，如欲附加檔案類型只能為.png
        """
        time.sleep(wait)
        image_dir = os.path.join(Path.SCREENSHOT_DIR, image_dir)
        os.makedirs(image_dir, exist_ok=True)
        if '.png' not in image_name:
            image_name += '.png'
        if '.' in image_name and 'png' not in image_name:
            raise ValueError('image name should be "image_name" or "image_name.png"')
        if image_count:
            image_name = f'{Screenshot.COUNT}_{image_name}'
        image_path = os.path.join(image_dir, image_name)
        self.driver.save_screenshot(image_path)
        allure.attach.file(image_path, image_path, allure.attachment_type.JPG)
        Screenshot.COUNT += 1
        return image_path
