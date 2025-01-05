from huskypo import Element, Elements
from huskypo import By
from huskypo import dynamic
from trying.huskypo_extension.page import Page


class BorderObject(Page):

    table = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable[1]', timeout=3)
    scrollview = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]', timeout=3)
    collectionview = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeCollectionView[1]', timeout=3)
    tabbar = Element(By.ACCESSIBILITY_ID, '標籤頁列', timeout=3)

    tables = Elements(By.CLASS_NAME, 'XCUIElementTypeTable')

    @dynamic
    def table_order(self, order: int = 1):
        return Element(By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeTable[{order}]')
