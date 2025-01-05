from huskypo import By, Element
from trying.huskypo_extension.page import Page


class Loading(Page):
    app_loading = Element(
        By.ACCESSIBILITY_ID,
        'SVProgressHUD',
        remark='app_loading_SVProgressHUD')

    app_progressing = Element(
        By.ACCESSIBILITY_ID,
        '進行中',
        remark='app_progressing_進行中')

    webview_redirecting = Element(
        By.ACCESSIBILITY_ID,
        'SuperRedirect',
        remark='webview_redirecting_SuperRedirect')

    webview_progressing = Element(
        By.XPATH,
        '//XCUIElementTypeButton[@name="webview close"]/preceding-sibling::XCUIElementTypeOther[1]',
        remark='webview_progressing_navi進度條')

    webview_loading = Element(
        By.IOS_PREDICATE,
        'name IN {"Loading", "LOADING"} OR name CONTAINS "讀取中"',
        remark='webview_loading_Loading或LOADING或讀取中')

    app_activity_indicator = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeActivityIndicator[-1]',
        remark='app_activity_indicator_**/XCUIElementTypeActivityIndicator[-1]')

    app_progress_indicator = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeProgressIndicator[-1]',
        remark='app_progress_indicator_**/XCUIElementTypeProgressIndicator[-1]')

    amount_gray_loading = Element(
        By.XPATH,
        '//XCUIElementTypeStaticText[@name="本月待繳金額 (TWD)"]/following::*[2]/child::*[1]',
        remark='灰色長條loading icon')
