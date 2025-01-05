# from huskypo import Page
from huskypo import Element, Elements
from huskypo import By
from huskypo import dynamic

# Using extended Page functions
from trying.huskypo_extension.page import Page


class WebPage(Page):

    search_field = Element(By.NAME, 'q', remark='搜尋輸入框')
    search_results = Elements(By.TAG_NAME, 'h3', remark='所有搜尋結果')
    search_result1 = Element(By.XPATH, '//h3[1]', remark='第一筆搜尋結果')

    @dynamic
    def search_result(self, order: int = 1):
        return Element(By.XPATH, f'//h3[{order}]', remark=f'第{order}筆搜尋結果')

    @dynamic
    def keyword_results(self, keyword: str):
        return Elements(By.XPATH, f'//*[contains(text(), "{keyword}")]')


class IframePage(Page):

    iframe1 = Element(By.TAG_NAME, 'iframe')


class ActionPage(Page):

    first = Element(By.XPATH, '//*[text()="焦點提要"]')
    second = Element(By.XPATH, '//*[text()="為你推薦"]')
    third = Element(By.XPATH, '//*[text()="您的主題"]')
