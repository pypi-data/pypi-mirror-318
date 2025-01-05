from huskypo import By, Element
from trying.huskypo_extension.page import Page


class Bottom(Page):

    # 此處因為可能出現在各個頁面中，元素不一定唯一，用button type定位

    finance = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "帳務總覽"`]', remark='帳務總覽')
    invest = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "投資"`]', remark='投資')
    loan = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "貸款"`]', remark='貸款')
    insurance = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "保險"`]', remark='保險')
    more = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "更多"`]', remark='更多')
