from huskypo import Element, Elements
from huskypo import By
from huskypo import dynamic
from trying.huskypo_extension.page import Page


class SelectPage(Page):

    fruit_list = Element(By.ID, 'favoriteFruits')

    submit = Element(By.CLASS_NAME, 'submit-btn')

    @dynamic
    def fruit_value(self, value: str):
        return Element(By.XPATH, f'//option[@value="{value}"]')

    @property
    @dynamic
    def fruit_date(self):
        return Element(By.XPATH, f'//option[@value="date"]')

    @property
    @dynamic
    def fruit_apple(self):
        return Element(By.XPATH, f'//option[@value="apple"]')

    static_fruit = Element()

    def dynamic_fruit(self, fruit: str) -> Element:
        self.static_fruit = (By.XPATH, f'//option[@value="{fruit}"]')
        return self.static_fruit
