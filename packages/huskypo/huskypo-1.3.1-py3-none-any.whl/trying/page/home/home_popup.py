from huskypo import By, Element
from trying.huskypo_extension.page import Page


class HomePopup(Page):

    pp = '首頁彈窗'

    # 立即升級您的網銀密碼彈窗
    upgrade_psw_title = Element(By.ACCESSIBILITY_ID, '立即升級您的網銀密碼', remark=f'{pp}_立即升級您的網銀密碼_標題')
    upgrade_psw_dismiss = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "下次再說"`]', remark=f'{pp}_立即升級您的網銀密碼_下次再說按鈕'
    )

    # 信任這台裝置彈窗
    trust_device_title = Element(By.IOS_PREDICATE, 'name CONTAINS "信任" AND name CONTAINS "裝置"')
    trust_device_content = Element(By.IOS_PREDICATE, 'name CONTAINS "信任後"')
    trust_device_accept = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "信任"`]')
    trust_device_dismiss = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "不信任"`]')

    # 登入安全再升級彈窗(手勢登入後)
    login_security_title = Element(By.IOS_PREDICATE, 'label BEGINSWITH "登入安全再升級"', remark=f'{pp}_登入安全再升級_標題')
    login_security_content = Element(By.IOS_PREDICATE, 'label BEGINSWITH "透過簡訊"', remark=f'{pp}_登入安全再升級_內文')
    login_security_dismiss = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "暫時不用"`]', remark=f'{pp}_登入安全再升級_暫時不用按鈕'
    )
    login_security_accept = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "增加安全防護"`]', remark=f'{pp}_登入安全再升級_增加安全防護按鈕'
    )
