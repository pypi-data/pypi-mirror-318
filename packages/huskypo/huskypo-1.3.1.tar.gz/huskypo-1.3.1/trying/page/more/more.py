from huskypo import By, Element, Elements, dynamic
from trying.huskypo_extension.page import Page


class MorePage(Page):

    table = Element(By.CLASS_NAME, 'XCUIElementTypeTable')

    wait_securities = Elements(By.IOS_PREDICATE, 'name CONTAINS "安全"')
    wait_finance = Element(By.ACCESSIBILITY_ID, '金融商品')

    def wait_securities_and_finance(self) -> list:
        waits = []
        waits.append(self.wait_finance.wait_present(reraise=False))
        waits.append(self.wait_securities.wait_all_present(reraise=False))
        return waits

    # 頂部導覽列
    navi_window = Element(By.CLASS_NAME, 'XCUIElementTypeNavigationBar', remark='導覽窗口')
    title_ = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label=="更多功能"`]',
        remark='標題文本')
    small_bell_button = Element(By.ACCESSIBILITY_ID, 'icNavbarNotificationDarkgrey', remark='小鈴鐺')
    search_button = Element(By.ACCESSIBILITY_ID, 'icNavbarSearchDarkgrey', remark='更多功能_搜尋按鈕')

    # 個人資訊
    profile_image = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[1]', remark='頭像圖標')
    profile_name = Element(
        By.XPATH, '//XCUIElementTypeStaticText[@name="查看個人資料"]/preceding-sibling::XCUIElementTypeStaticText[1]',
        remark='姓名文本')
    profile_access_info_button = Element(By.ACCESSIBILITY_ID, '查看個人資料')
    profile_tree_icon = Element(By.ACCESSIBILITY_ID, 'leafIcon')
    profile_tree_point = Element(
        By.XPATH, '//XCUIElementTypeImage[@name="leafIcon"]/following-sibling::XCUIElementTypeStaticText[1]',
        remark='小數點數值')

    # 帳戶安全區塊
    security_texts = Elements(By.IOS_PREDICATE, 'name CONTAINS "安全"', 60)
    security_list = ['未檢測', '基本防護', '進階防護', '高階防護']  # TODO 還需確認完全防護字樣
    security_title = Element(By.IOS_PREDICATE, 'name CONTAINS "安全健檢"')
    security_status = Element(By.IOS_PREDICATE, 'name CONTAINS "安全設定" OR name CONTAINS "安全狀態"')
    security_action = Element(By.IOS_PREDICATE, 'name ENDSWITH "檢測" OR name ENDSWITH "設定"')

    # 金融商品區塊
    finance = Element(By.ACCESSIBILITY_ID, '金融商品', remark='金融商品文本')

    finance_twd = Element(By.ACCESSIBILITY_ID, '臺幣')
    finance_frd = Element(By.ACCESSIBILITY_ID, '外幣')
    finance_cdc = Element(By.ACCESSIBILITY_ID, '信用卡')
    finance_dbc = Element(By.ACCESSIBILITY_ID, '簽帳金融卡')
    finance_fund = Element(By.ACCESSIBILITY_ID, '基金')
    finance_exchange_rate = Element(By.ACCESSIBILITY_ID, '利匯率')
    finance_insurance = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label=="保險"`]', remark='保險')
    finance_personal = Element(By.ACCESSIBILITY_ID, '個人年度回顧')

    # 金融商品區塊_臺幣子列表
    fin_twd_tx = Element(By.ACCESSIBILITY_ID, '臺幣轉帳')
    fin_twd_dmd_stmt = Element(By.ACCESSIBILITY_ID, '臺幣帳戶明細')
    fin_twd_sd_qry = Element(By.ACCESSIBILITY_ID, '預約轉帳查詢')
    fin_twd_epass = Element(By.ACCESSIBILITY_ID, '匯出臺幣電子存摺')
    fin_twd_app_record = Element(By.ACCESSIBILITY_ID, 'App 轉帳紀錄')

    # 金融商品區塊_外幣子列表
    fin_frd_fx = Element(By.ACCESSIBILITY_ID, '外幣買賣')
    fin_frd_out = Element(By.ACCESSIBILITY_ID, '外幣轉出')
    fin_frd_dmd_stmt = Element(By.ACCESSIBILITY_ID, '外幣活存交易明細')
    fin_frd_epass = Element(By.ACCESSIBILITY_ID, '匯出外幣電子存摺')
    fin_frd_remit = Element(By.ACCESSIBILITY_ID, '外匯匯入匯款查詢及解匯')
    fin_frd_fx_rcd = Element(By.ACCESSIBILITY_ID, 'App 換匯紀錄')
    fin_frd_qry = Element(By.ACCESSIBILITY_ID, '轉至他行帳戶明細及進度查詢')

    # 外幣轉出彈窗
    remind_frd_out_popup_content = Element(
        By.IOS_PREDICATE, 'name CONTAINS "提醒您" AND name CONTAINS "外幣約定帳號"',
        remark='外幣轉出提醒彈窗')
    remind_frd_out_popup_dismiss = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "返回"`]',
        remark='外幣轉出提醒彈窗_返回按鈕')

    # 金融商品區塊_信用卡子列表
    fin_cdc_statement = Element(By.ACCESSIBILITY_ID, '刷卡消費明細')
    fin_cdc_payment = Element(By.ACCESSIBILITY_ID, '信用卡帳單與繳款')
    fin_cdc_single_and_installment = Element(By.ACCESSIBILITY_ID, '單筆及帳單分期')
    fin_cdc_installment_details = Element(By.ACCESSIBILITY_ID, '分期剩餘明細')
    fin_cdc_list = Element(By.ACCESSIBILITY_ID, '我的信用卡清單')
    fin_cdc_auto = Element(By.ACCESSIBILITY_ID, '自動扣繳設定')
    fin_cdc_activation = Element(By.ACCESSIBILITY_ID, '信用卡開卡')
    fin_cdc_quota = Element(By.ACCESSIBILITY_ID, '臨時額度調整')
    fin_cdc_binding = Element(By.ACCESSIBILITY_ID, '一鍵綁卡')
    fin_cdc_single_cash_advance = Element(By.ACCESSIBILITY_ID, '單筆預借現金')
    fin_cdc_installment_cash_advance = Element(By.ACCESSIBILITY_ID, '分期預借現金')
    fin_cdc_etag = Element(By.ACCESSIBILITY_ID, '代扣繳eTag申請')
    fin_cdc_lost = Element(By.ACCESSIBILITY_ID, '信用卡掛失')
    # fin_cdc_bill_installment = Element(By.ACCESSIBILITY_ID, '帳單分期')
    # fin_cdc_single_installment = Element(By.ACCESSIBILITY_ID, '單筆分期')

    # 金融商品區塊_簽帳金融卡子列表
    fin_dbc_overview = Element(By.ACCESSIBILITY_ID, '簽帳卡總覽')

    # 金融商品區塊_基金子列表
    fin_fund_trust = Element(By.ACCESSIBILITY_ID, '信託帳戶交易明細')
    fin_fund_serve = Element(By.ACCESSIBILITY_ID, '預約服務單')
    fin_fund_sbsc = Element(By.ACCESSIBILITY_ID, '基金申購')
    fin_fund_redemp = Element(By.ACCESSIBILITY_ID, '基金贖回')
    fin_fund_modify = Element(By.ACCESSIBILITY_ID, '定期(不)定額管理')
    fin_fund_qry = Element(By.ACCESSIBILITY_ID, '基金查詢')

    # 金融商品區塊_基金_基金贖回彈窗
    fnd_redemp_pp_cnt = Element(By.ACCESSIBILITY_ID, '您尚未簽署信託契約（FUND001）', remark=f'基金贖回彈窗_內文文本')
    fnd_redemp_pp_dis = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeButton[`label=="暫時不要"`]',
        remark=f'基金贖回彈窗_暫時不要按鈕')
    fnd_redemp_pp_acc = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeButton[`label=="立即簽署"`]',
        remark=f'基金贖回彈窗_立即簽署按鈕')

    # 金融商品區塊_利匯率子列表
    fin_ir_twd = Element(By.ACCESSIBILITY_ID, '臺幣存放款利率')
    fin_ir_frd = Element(By.ACCESSIBILITY_ID, '外幣存款利率')
    fin_ir_fxr = Element(By.ACCESSIBILITY_ID, '外幣匯率')
    fin_ir_est = Element(By.ACCESSIBILITY_ID, '換匯試算')

    # 金融商品區塊_保險子列表
    fin_ins_life = Element(By.ACCESSIBILITY_ID, '人壽保單查詢')
    fin_ins_prop = Element(By.ACCESSIBILITY_ID, '產險保單查詢')
    fin_ins_auto = Element(By.ACCESSIBILITY_ID, '汽車險')
    fin_ins_moto = Element(By.ACCESSIBILITY_ID, '機車險')

    # 設定區塊
    set = Element(By.ACCESSIBILITY_ID, '設定')
    set_gen = Element(By.ACCESSIBILITY_ID, '一般設定')
    set_txn = Element(By.ACCESSIBILITY_ID, '交易設定')

    # 設定/一般設定子項目
    set_gen_fast = Element(By.ACCESSIBILITY_ID, '快速登入')
    set_gen_tfa = Element(By.ACCESSIBILITY_ID, '登入兩步驟驗證')
    set_gen_psw = Element(By.ACCESSIBILITY_ID, '代號密碼變更')
    set_gen_noti = Element(By.ACCESSIBILITY_ID, '推播管理')
    set_gen_fh = Element(By.ACCESSIBILITY_ID, '國泰金控資料共享')
    set_gen_trend = Element(By.ACCESSIBILITY_ID, '漲跌顯示色')
    set_gen_verify = Element(By.ACCESSIBILITY_ID, '授權驗證管理')
    set_gen_closure = Element(By.ACCESSIBILITY_ID, '帳戶銷戶')

    # 設定/交易設定子項目
    set_txn_bind = Element(By.ACCESSIBILITY_ID, '裝置綁定')
    set_txn_verify = Element(By.ACCESSIBILITY_ID, '交易驗證方式')
    set_txn_bidir = Element(By.ACCESSIBILITY_ID, '本人國泰世華帳戶互轉')
    set_txn_desig = Element(By.ACCESSIBILITY_ID, '常用與約定帳號管理')
    set_txn_cert = Element(By.ACCESSIBILITY_ID, '國泰世華憑證管理')
    set_txn_mobile = Element(By.ACCESSIBILITY_ID, '手機號碼連結帳號')
    set_txn_nocard = Element(By.ACCESSIBILITY_ID, '手機提款')

    # 用戶服務區塊
    user_serve = Element(By.ACCESSIBILITY_ID, '用戶服務')

    user_queue = Element(By.IOS_PREDICATE, 'label BEGINSWITH "服務據點"', remark=f'服務據點取號按鈕')
    user_online = Element(By.ACCESSIBILITY_ID, '線上業務申辦')
    user_custom = Element(By.ACCESSIBILITY_ID, '客服中心')
    user_faq = Element(By.ACCESSIBILITY_ID, '常見問題')

    # 其他區塊
    others = Element(By.ACCESSIBILITY_ID, '其他')
    others_invite = Element(By.ACCESSIBILITY_ID, '邀請好友')
    others_offers = Element(By.ACCESSIBILITY_ID, '專屬優惠')
    others_wvcube = Element(By.ACCESSIBILITY_ID, '前往網銀')
    others_robo = Element(By.ACCESSIBILITY_ID, '前往智能投資')

    # 底部區塊
    user_policy = Element(By.IOS_PREDICATE, 'label CONTAINS "使用者隱私條款"')

    # 版本資訊
    version_info = Element(By.IOS_PREDICATE, 'label BEGINSWITH "版本"')

    # 登出
    logout_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "登出"`]', remark='主登出按鈕')

    # 登出確認彈窗 須依照appium inspector排列的順序設置index
    logout_popup_logout_button = Element(
        By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name CONTAINS "登出"`][1]', remark='登出彈窗_包含登出文本的按鈕')

    logout_popup_content = Element(By.IOS_PREDICATE, 'label CONTAINS "離開應用程式"', remark='登出彈窗_內文文本')
    logout_popup_dismiss = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "取消"`]', remark='登出彈窗_取消按鈕')
    logout_popup_accept = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeButton[`name == "登出"`][1]',
        remark='登出彈窗_確認按鈕')

    logout_inform_logout_button = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeButton[`name == "立即登出"`]',
        remark='登出新版本通知_立即登出')
    logout_inform_update_button = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeButton[`name == "前往更新"`]',
        remark='登出新版本通知_前往更新')

    close_button = Element(By.ACCESSIBILITY_ID, 'webview close', remark='webview關閉鈕')
    back_button1 = Element(By.ACCESSIBILITY_ID, 'icon arrow left black', remark='原生app返回紐')
    back_button2 = Element(By.ACCESSIBILITY_ID, 'btn arrowleft n', remark='一般app返回紐')

    # 信用卡預借現金 / 分期預借現金
    fin_cdc_installment_cash_advance_text = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeOther[`label == "互補"`]/XCUIElementTypeOther/XCUIElementTypeStaticText',
        remark='導向頁_信用卡預借現金分期文本')

    # 信用卡開卡
    fin_cdc_issuance_title = Element(By.IOS_PREDICATE, 'label == "我的開卡清單"', remark='我的開卡清單標題')

    # 一鍵綁卡
    fin_cdc_binding_title = Element(By.ACCESSIBILITY_ID, '一鍵綁卡', remark='一鍵綁卡標題')
    fin_cdc_binding_btn = Elements(By.IOS_PREDICATE, 'name == "立即綁定"', remark='一鍵綁卡按鈕')

    # 單筆預借現金
    fin_cdc_single_cash_advance_title = Element(By.ACCESSIBILITY_ID, '預借現金申請', remark='預借現金申請標題')
    fin_cdc_single_cash_advance_home_btn = Element(By.ACCESSIBILITY_ID, '回首頁', remark='預借現金申請_回首頁按鈕')
    sys_info = Element(By.ACCESSIBILITY_ID, '系統訊息', remark='系統訊息文本')

    # 代扣繳eTag申請
    fin_cdc_etag_title = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label == "eTag自動儲值/eTag智慧停車"`]',
        remark='代扣繳eTag申請標題')

    # infos = Elements(By.IOS_PREDICATE, 'name CONTAINS "資料"')
    # communication_address_text = Element(By.ACCESSIBILITY_ID, '通訊資料：', remark='通訊資料文本')

    # 信用卡掛失
    fin_cdc_lost_title = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label == "信用卡掛失"`]',
        remark='信用卡掛失標題')
    fin_cdc_lost_terms = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label == "信用卡掛失補發約定條款"`]',
        remark='信用卡掛失條款')

    # 預約服務單
    my_service_title = Element(By.ACCESSIBILITY_ID, '預約服務單', remark='預約服務單標題')
    fund_claim_btn = Element(By.ACCESSIBILITY_ID, '基金申購', remark='基金申購按鈕')

    # 定期(不)定額管理
    regular_installment_title = Element(By.ACCESSIBILITY_ID, '定期(不)定額管理', remark='定期(不)定額管理標題')
    payment_date = Element(By.ACCESSIBILITY_ID, '每月設定扣款日', remark='每月設定扣款日文本')
    system_maintain_text = Element(By.IOS_PREDICATE, 'name CONTAINS "系統維護中"', remark='系統維護中文本')

    # 裝置綁定
    bind_title = Element(By.ACCESSIBILITY_ID, '裝置綁定', remark='裝置綁定標題')
    bind_img = Element(By.ACCESSIBILITY_ID, 'img_ally_devicebinding', remark='裝置綁定圖')
    no_need_btn = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "暫時不用"`]', remark='暫時不用按鈕')

    # 交易驗證管理
    set_txn_verify_title = Element(By.ACCESSIBILITY_ID, '設定交易驗證', remark='設定交易驗證標題')
    face_auth_btn = Element(By.ACCESSIBILITY_ID, '立即註冊人臉辨識', remark='立即註冊人臉辨識按鈕')

    # 本人國泰世華帳戶互轉
    set_txn_bidir_title = Element(By.ACCESSIBILITY_ID, '本人國泰世華帳戶互轉', remark='本人國泰世華帳戶互轉標題')
    txn_bidir_status = Element(By.IOS_PREDICATE, 'name == "已啟用" OR name = "未啟用"', remark='互轉設定已啟用字串或未啟用字串')

    change_txn_verify_code_button = Element(By.ACCESSIBILITY_ID, 'ic settings 80 n', remark='變更交易驗證碼按鈕')

    origin_verify_code_input_box = Element(
        By.XPATH,
        '//XCUIElementTypeStaticText[@name="舊交易認證碼"]/following::XCUIElementTypeSecureTextField[1]',
        remark='舊交易認證碼輸入匡')  # 不能直接使用XCUIElementTypeSecureTextField的值定位 因為輸入匡有輸入後 就無法定位了
    new_verify_code_input_box = Element(
        By.XPATH,
        '//XCUIElementTypeStaticText[@name="新交易認證碼"]/following::XCUIElementTypeSecureTextField[1]',
        remark='新交易認證碼輸入匡')
    second_verify_code_input_box = Element(
        By.XPATH,
        '//XCUIElementTypeStaticText[@name="確認新交易認證碼"]/following::XCUIElementTypeSecureTextField[1]',
        remark='確認新交易認證碼輸入匡')
    next_step_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "下一步"`]', remark='下一步按鈕')

    origin_verify_code_error_popup = Element(By.IOS_PREDICATE, 'name CONTAINS "舊密碼驗證錯誤"', remark='舊交易驗證碼錯誤彈窗')
    new_verify_code_should_be_different_text = Element(
        By.IOS_PREDICATE, 'name CONTAINS "密碼不得與前一次相同"', remark='新舊交易驗證碼相同提醒')
    second_verify_code_is_different_text = Element(
        By.IOS_PREDICATE, 'name CONTAINS "需和新密碼一樣"', remark='再次輸入新交易驗證碼不一致提醒')
    limited_times_popup = Element(By.IOS_PREDICATE, 'name CONTAINS "已達上限"', remark='交易認證碼輸入次數已達上限')

    accept_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "確認"`]', remark='彈窗確認按鈕')

    changed_successfully_title = Element(By.ACCESSIBILITY_ID, '變更成功', remark='變更成功標題')
    finish_button = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "完成"`]', remark='完成按鈕')

    # 設定約定帳號

    set_txn_desig_title = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label == "常用與約定帳號管理"`]',
        remark='常用與約定帳號管理標題')

    # 國泰世華憑證管理
    set_txn_cert_title = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeNavigationBar[`name == "國泰世華憑證管理"`]',
        remark='國泰世華憑證管理標題')

    # 手機號碼連結帳號
    set_txn_mobile_title = Element(By.ACCESSIBILITY_ID, '手機號碼連結帳號', remark='手機號碼連結帳號標題')

    # 手機提款
    set_txn_nocard_title = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeNavigationBar[`name == "手機提款"`]',
        remark='手機提款標題')
    set_txn_nocard_account_text = Element(By.IOS_PREDICATE, 'name CONTAINS "帳號："', remark='手機提款帳號')

    # 線上業務申辦
    user_online_title = Element(By.ACCESSIBILITY_ID, '線上服務', remark='線上服務標題')

    # 客服中心
    user_custom_title = Element(By.IOS_PREDICATE, 'label == "客服中心"', remark='客服中心標題')
    user_custom_24h_text = Element(By.ACCESSIBILITY_ID, '24 小時客服中心', remark='24小時客服中心文本')
    user_customer_service_image = Element(By.ACCESSIBILITY_ID, 'img_cube_customerservice')

    # 常見問題
    user_faq_title = Element(By.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "常見問題"`]', remark='常見問題標題')
    user_faq_remark = Element(
        By.IOS_CLASS_CHAIN,
        '**/XCUIElementTypeStaticText[`label CONTAINS "更進一步的協助"`]',
        remark='常見問題備註')

    # 邀請好友
    QR = Element(By.CLASS_NAME, 'XCUIElementTypeImage', remark='邀請好友QR code')

    # 前往網銀
    others_offers_title = Element(By.ACCESSIBILITY_ID, '專屬優惠', remark='專屬優惠標題')
    no_offers_text = Element(By.ACCESSIBILITY_ID, '您尚無專屬優惠', remark='您尚無專屬優惠文本')
