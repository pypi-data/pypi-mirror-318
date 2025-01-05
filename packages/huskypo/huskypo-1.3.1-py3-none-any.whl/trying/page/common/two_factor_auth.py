from huskypo import By, Element, Elements
from trying.huskypo_extension.page import Page


class TFASettingPage(Page):

    title_ = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeNavigationBar/XCUIElementTypeStaticText[`name == "登入兩步驟驗證"`]',
        remark='登入兩步驟驗證title')

    tfa_image = Element(By.ACCESSIBILITY_ID, 'imgCubeManage2Falogin')

    back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black')

    current_status = Element(By.IOS_PREDICATE, 'name IN {"已開啟"}', remark='登入兩步驟驗證啟用狀態')

    modify_status_button = Element(By.IOS_PREDICATE, 'name IN {"確定關閉"}', remark='登入兩步驟驗證變更狀態')

    trust_devices = Element(By.ACCESSIBILITY_ID, '已加入的信任裝置')


class TFADevicesPage(Page):

    title_ = Element(By.IOS_PREDICATE, 'label == "信任裝置"')
    back_button = Element(By.ACCESSIBILITY_ID, 'icon arrow left black')
    delete_button = Element(By.ACCESSIBILITY_ID, '刪除')

    iphone = Element(By.ACCESSIBILITY_ID, 'iPhone')

    delete_devices_button = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name BEGINSWITH "刪除"`]', remark='刪除裝置按鈕')

    delete_devices_popup_title = Element(By.IOS_PREDICATE, 'name BEGINSWITH "確定要刪除信任裝置"')
    delete_devices_popup_accept = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "刪除"`]')


class TFAActivatePopup(Page):

    title_ = Element(By.ACCESSIBILITY_ID, '登入兩步驟驗證')
    confirm = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "立即驗證"`]')


class TFAActivatePage(Page):

    title_ = Element(By.ACCESSIBILITY_ID, '登入兩步驟驗證')

    image = Element(By.ACCESSIBILITY_ID, 'imgCube2Falogin')

    dismiss = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "暫時不用"`]')
    accept = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "立即驗證"`]')

    all_infos = Elements(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView/**/XCUIElementTypeStaticText')


class TFAOTPVerifyPage(Page):

    title_ = Element(By.IOS_PREDICATE, 'label == "啟用兩步驟驗證"')

    otp_field = Element(By.CLASS_NAME, 'XCUIElementTypeTextField', remark='otp輸入框')

    next_set_device_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name BEGINSWITH "下一步"`]')

    device_image = Element(By.ACCESSIBILITY_ID, 'img_cube_editdevicename')

    activate_confirm_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "確定加入"`]')

    activate_success = Element(By.ACCESSIBILITY_ID, '啟用成功')

    activate_done_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "完成"`]')


class TFAOTPCommonPage(Page):

    verify_text = Element(By.IOS_PREDICATE, 'name CONTAINS "驗證碼"', remark='共用驗證碼文本')

    input_field = Element(By.CLASS_NAME, 'XCUIElementTypeTextField', remark='共用OTP輸入框')

    confirm_button = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeButton[`name BEGINSWITH "確定" OR name BEGINSWITH "確認" OR name BEGINSWITH "下一步" OR name == "登入"`]',
        remark='共用確定按鈕')
