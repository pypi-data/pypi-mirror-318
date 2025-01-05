from huskypo import By, Element, dynamic
from trying.huskypo_extension.page import Page


class Keyboard(Page):

    earth = Element(By.ACCESSIBILITY_ID, '下一個鍵盤')

    space = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name IN {"space", "空格"}`]')
    space_zh = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "空格"`]')
    space_en = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "space"`]')

    a = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "a"`]')

    @dynamic
    def alphabet(self, alphabet_: str = 'a'):
        return Element(By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeKey[`name == "{alphabet_}"`]', f'鍵盤英文字母{alphabet_}')

    done = Element(By.IOS_PREDICATE, 'name IN {"Done", "完成"}', remark="完成按鍵")
    search = Element(By.ACCESSIBILITY_ID, 'Search', remark="搜尋按鍵")

    one = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "1"`]')
    two = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "2"`]')
    three = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "3"`]')
    four = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "4"`]')
    five = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "5"`]')
    six = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "6"`]')
    seven = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "7"`]')
    eight = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "8"`]')
    nine = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "9"`]')
    zero = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name == "0"`]')

    delete = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeKey[`name IN {"刪除", "delete"}`]')

    @dynamic
    def number(self, number_: str = '0'):
        return Element(By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeKey[`name == "{number_}"`]', f'鍵盤數字{number_}')
