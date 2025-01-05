from huskypo import By, Element, Elements
from trying.huskypo_extension.page import Page


class LaunchPage(Page):

    logo = Element(By.ACCESSIBILITY_ID, 'img_cube_launch_cublogo', remark='LAUNCHING')


class QueuePopup(Page):

    title_ = Element(By.ACCESSIBILITY_ID, '目前使用人數較多')
    confirm = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name CONTAINS "排隊"`]', remark='前往排隊按鈕')


class QueuePage(Page):

    title_ = Element(By.IOS_PREDICATE, 'label CONTAINS "安排您登入"', remark='我們正在安排您登入建議停留在本畫面等待')

    common_text = Element(By.IOS_PREDICATE, 'name CONTAINS "更新時間" OR name CONTAINS "目前使用人數較多"', remark='排隊機制共用文本')

    update_time_text = Element(By.IOS_PREDICATE, 'name CONTAINS "更新時間"')


class InformPopup(Page):

    # icon = Element(By.ACCESSIBILITY_ID, 'ic_popup_graphicCal', describe='啟動app時的測試彈窗icon')
    # confirm = Element(
    #     By.XPATH, '//XCUIElementTypeImage[@name="ic_popup_graphicCal"]/following::XCUIElementTypeButton[1]',
    #     describe='啟動app時的測試彈窗確認鈕'
    # )

    scrollviews = Elements(By.CLASS_NAME, 'XCUIElementTypeScrollView', remark='所有scrollview_用來判斷是否有通知彈窗')

    # 此處每版需注意元素位置，有可能會誤按到另外一個
    # 2024/03/11 1601:
    # ScrollView[1] 為最外層; ScrollView[2] 是彈窗內部
    # accept: -1, dismiss: -2
    accept = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]/**/XCUIElementTypeButton[-1]',
        timeout=3,
        remark='通知彈窗確認按鈕')
    dismiss = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]/**/XCUIElementTypeButton[-2]',
        timeout=3,
        remark='通知彈窗取消按鈕')
