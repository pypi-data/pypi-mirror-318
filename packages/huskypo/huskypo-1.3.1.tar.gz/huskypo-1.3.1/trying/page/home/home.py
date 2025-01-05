from huskypo import By, Element, Elements
from trying.huskypo_extension.page import Page


class HomePage(Page):
    # ios_class_chain: 此頁面注意有些text和icon有重疊，以clickable者為最優先，並遵守appium查詢順序作為index
    # 如果是利用xpath尋找則無以上現象，[]或index都是正常的，不用依賴appium查詢順序

    # page 帳務總覽頁
    page = '首頁'

    # 共用
    cc_plan_list = ['日本賞', '玩數位', '趣旅行', '集精選', '樂饗購', '過生日']

    # waiting
    wait_amounts = Elements(By.IOS_PREDICATE, 'label CONTAINS "$"')

    # 導覽列
    title_ = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "帳務總覽"`]', remark="帳務總覽_標題文本")
    navi_afa = Element(By.ACCESSIBILITY_ID, 'ic cube navbar afa', remark="帳務總覽_導覽列_阿發按鈕")
    navi_scan = Element(By.ACCESSIBILITY_ID, 'ic cube navbar scan gray', remark="帳務總覽_導覽列_掃描QR按鈕")
    navi_personal = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar[`name == "帳務總覽"`]/XCUIElementTypeButton[3]',
        remark="帳務總覽_導覽列_個人資料"
    )

    # TODO 個人化 banner 板塊
    personal_banner = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]',
        remark='個人化banner區塊')

    # deposit
    no_frd_account_message = Element(By.IOS_PREDICATE, 'name CONTAINS "無外幣帳戶"')

    # table
    table = Element(By.IOS_PREDICATE, 'type == "XCUIElementTypeTable"', remark='首頁_table元素')

    # 快捷鍵區塊
    hotkey_tx_icon = Element(By.ACCESSIBILITY_ID, 'ic cube action transfer', remark="轉帳icon")
    hotkey_tx_text = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "轉帳"`]', remark="轉帳文本")
    hotkey_fx_icon = Element(By.ACCESSIBILITY_ID, 'ic cube action forex', remark="外幣買賣icon")
    hotkey_fx_text = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "外幣買賣"`]', remark="外幣買賣文本")
    hotkey_pay_icon = Element(By.ACCESSIBILITY_ID, 'ic cube action payselect', remark="繳費icon")
    hotkey_pay_text = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "繳費"`]', remark="繳費文本")
    hotkey_nocard_icon = Element(By.ACCESSIBILITY_ID, 'ic cube action nocard', remark="手機提款icon")
    hotkey_nocard_text = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "手機提款"`]',
                                 remark="手機提款文本")

    # cpin 存款推播
    cpin_noti_cell = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]', remark=f'{page}_推播區塊')
    cpin_noti_info = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeTable[1]/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]',
        remark=f'{page}_推播通知'
    )

    # apin 存款
    depo_title = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "存款"`]/XCUIElementTypeStaticText[`label == "存款"`]',
        remark=f'{page}_apin_存款文本')
    depo_eye = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeOther[`name == "存款"`]/XCUIElementTypeButton[`label == "ic cube eye open"`]',
        remark=f'{page}_apin_存款眼睛')
    deposit_financial_calendar_button = Element(
        By.IOS_PREDICATE, 'name == "查看帳務行事曆" AND visible == true',
        remark='存款_查看帳務行事曆')

    deposit_twd_column = Element(By.ACCESSIBILITY_ID, '臺幣總額', remark=f'{page}_存款_臺幣總額文本')
    deposit_twd_amount = Element(
        By.XPATH, '//XCUIElementTypeStaticText[@name="臺幣總額"]/../XCUIElementTypeStaticText[contains(@name, "$")]',
        remark=f'{page}_apin_存款_臺幣總額金額')

    depo_frd_no_account = Element(By.IOS_PREDICATE, 'label CONTAINS "無外幣帳戶"',
                                  remark=f'{page}_apin_存款_無外幣帳戶通知')

    depo_frd_column = Element(By.ACCESSIBILITY_ID, '外幣總額', remark=f'{page}_存款_外幣總額文本')
    depo_frd_amount = Element(
        By.XPATH, '//XCUIElementTypeStaticText[@name="外幣總額"]/../XCUIElementTypeStaticText[contains(@name, "$")]',
        remark=f'{page}_apin_存款_外幣總額金額')

    # apin 信用卡 此處注意定位比較複雜
    cdc_title = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "信用卡"`]/XCUIElementTypeStaticText[`label == "信用卡"`]',
        remark=f'{page}_apin_信用卡文本'
    )

    cdc_info_button = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "信用卡"`]/XCUIElementTypeButton[`label == "查看完整資訊"`]',
        remark=f'{page}_apin_信用卡_查看完整資訊按鈕'
    )

    cdc_nocard_banner = Element(
        By.XPATH,
        '//XCUIElementTypeOther[@name="信用卡"]/following-sibling::XCUIElementTypeCell[1]/XCUIElementTypeOther[2]/XCUIElementTypeImage[1]',
        remark=f'{page}_apin_無信用卡的banner')

    # 重整信用卡區塊 assert的主要元素
    cdc_statement_column = Element(By.IOS_PREDICATE, 'label ENDSWITH "帳單"', remark=f'{page}_apin_信用卡_帳單標題')

    cdc_statement_amount = Element(
        By.XPATH,
        '//XCUIElementTypeStaticText[contains(@name, "帳單")]/following-sibling::XCUIElementTypeStaticText[contains(@name, "$")]',
        remark=f'{page}_帳單金額')

    cdc_statement_deadline = Element(By.IOS_PREDICATE, 'label BEGINSWITH "繳款截止日"', remark=f'{page}_apin_信用卡_繳款截止日')

    cdc_statement_paynow_button = Element(
        By.IOS_CLASS_CHAIN, f'**/XCUIElementTypeButton[`label == "立即繳費"`]',
        remark=f'{page}_立即繳費按鈕')

    cdc_statement_no_payment = Element(By.ACCESSIBILITY_ID, '無需繳款', remark=f'{page}_無需繳款')

    cc_statement_payed = Element(By.ACCESSIBILITY_ID, '已繳款', remark=f'{page}_已繳款')

    cdc_plan_column = Element(By.ACCESSIBILITY_ID, 'CUBE權益方案')

    cdc_plan_type = Element(
        By.XPATH, '//XCUIElementTypeStaticText[@name="CUBE權益方案"]/following-sibling::XCUIElementTypeStaticText[1]',
        remark=f'{page}_apin_信用卡_CUBE權益方案項目'
    )

    cc_plan_switch_btn = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "切換方案"`]', remark=f'{page}_apin_信用卡_切換方案按鈕'
    )

    cdc_txn_column = Element(By.ACCESSIBILITY_ID, '刷卡消費明細')
    cdc_txn_amount = Element(
        By.XPATH, '//XCUIElementTypeStaticText[@name="刷卡消費明細"]/../XCUIElementTypeStaticText[contains(@name, "$")][1]',
        remark='刷卡消費明細總額')
    cdc_quota_column = Element(By.ACCESSIBILITY_ID, '剩餘可用額度')
    cdc_quota_amount = Element(
        By.XPATH, '//XCUIElementTypeStaticText[@name="剩餘可用額度"]/../XCUIElementTypeStaticText[contains(@name, "$")][2]',
        remark='剩餘可用額度總額')

    # 匯率區塊
    fxr_title = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "匯率"`][2]', remark='匯率title')
    more_fxr_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "更多匯率"`]', remark='更多匯率按鈕')
