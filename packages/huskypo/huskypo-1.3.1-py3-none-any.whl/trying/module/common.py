import time

from selenium.common.exceptions import TimeoutException

from huskypo import logstack, Element
from trying.huskypo_extension.page import Page

from trying.page.common.activate import *
from trying.page.common.border_object import BorderObject
from trying.page.common.bottom import Bottom
from trying.page.common.loading import Loading
from trying.page.common.two_factor_auth import *
from trying.page.home.home import HomePage
from trying.page.home.home_popup import HomePopup
from trying.page.login.login import LoginPage
from trying.page.login.login_popup import LoginPopup
from trying.page.more.more import MorePage
from trying.page.ios.panel.keyboard import Keyboard


class Common:

    def __init__(self, iphone):
        self.iphone = iphone
        self.page = Page(iphone)
        self.border_object = BorderObject(iphone)
        self.launch_page = LaunchPage(iphone)
        self.queue_popup = QueuePopup(iphone)
        self.queue_page = QueuePage(iphone)
        self.inform_popup = InformPopup(iphone)
        self.keyboard = Keyboard(iphone)
        self.loading = Loading(iphone)
        self.login_page = LoginPage(iphone)
        self.login_popup = LoginPopup(iphone)
        self.tfa_verify_popup = TFAActivatePopup(iphone)
        self.tfa_verify_page = TFAActivatePage(iphone)
        self.tfa_activate_page = TFAOTPVerifyPage(iphone)
        self.tfa_otp_page = TFAOTPCommonPage(iphone)
        self.home_page = HomePage(iphone)
        self.home_popup = HomePopup(iphone)
        self.bottom = Bottom(iphone)
        self.more_page = MorePage(iphone)

    def prelogin_process(self):
        # self.prelogin_gcp()
        self.prelogin_informs()
        # self.switch_to_zh()  # 7.6.2301 更新

    def switch_to_zh(self):
        if self.login_page.language.text == 'EN':
            logstack.info('🟢 目前是英文版，先切換成中文版')
            self.login_page.language.click()
            self.login_page.language_zh.click()
            self.login_page.language_save_button.click()
            if self.login_page.language.text == 'ZH':
                logstack.info('✅ 成功切換成中文版')
            else:
                logstack.error('❌ 尚未切換成中文版，請確認是否有其他問題。')

    def switch_to_en(self):
        if self.login_page.language.text == 'ZH':
            logstack.info('🟢 目前是中文版，先切換成英文版')
            self.login_page.language.click()
            self.login_page.language_en.click()
            self.login_page.language_save_button.click()
            if self.login_page.language.text == 'EN':
                logstack.info('✅ 成功切換成英文版')
            else:
                logstack.error('❌ 尚未切換成英文版，請確認是否有其他問題。')

    def prelogin_gcp(
            self,
            gcp_timeout: int = 1,
            login_timeout: int = 3,
    ):
        """
        處理 launching 與 informs 會同時出現的情況
        """
        if self.login_page.login_button.is_present(login_timeout):
            logstack.info(f'✅ 登入鈕於{login_timeout}秒內出現，略過排隊機制流程\n')
            return None
        elif self.queue_page.common_text.is_present(gcp_timeout):
            common_text = self.queue_page.common_text.text
            if '目前使用人數較多' in common_text:
                logstack.warning(f'🟡 GCP: 出現彈窗')
                self.queue_page.save_screenshot("GCP", "彈窗")
                self.queue_popup.confirm.click()
            logstack.warning(f'🟡 GCP: 出現頁面')
            self.queue_page.update_time_text.wait_visible()
            self.queue_page.save_screenshot("GCP", "頁面")
            rect = self.queue_page.get_window_rect()
            tx = int(rect['x'] + rect['width'] * 0.5)
            ty = int(rect['y'] + rect['height'] * 0.375)  # 圖像在25%~50%之間
            self.queue_page.tap([(tx, ty)])
            logstack.info('✅ GCP: 點擊排隊圖像略過排隊')
            return True
        else:
            logstack.info('✅ 無GCP，請接續確認是否出現通知彈窗。')
            return None

    def prelogin_informs(
            self,
            launch_etimeout: int = 3,
            launch_netimeout: int = 30,
            imforms_timeout: int = 1,
            login_timeout: int = 3,
    ):
        """
        處理 launching 與 informs 會同時出現的情況
        """
        if self.launch_page.logo.is_present(launch_etimeout):
            logstack.info(f'🟢 LAUNCHING於{launch_etimeout}秒內出現')
            self.skip_inform_popups(imforms_timeout)
            if self.launch_page.logo.wait_not_present(launch_netimeout, False):
                if self.login_page.login_button.is_present(login_timeout):
                    logstack.info(f'✅ LAUNCHING已結束，並於{login_timeout}秒內出現登入鈕。\n')
                    return True
                logstack.warning(f'🟡 LAUNCHING已結束，但未於{login_timeout}秒內出現登入鈕，請確認是否有其他流程。\n')
            else:
                logstack.warning(f'🟡 LAUNCHING未於{launch_netimeout}秒內結束。\n')
        else:
            if self.login_page.login_button.is_present(login_timeout):
                logstack.info(f'✅ LAUNCHING較快結束，且已出現登入鈕。\n')
                return True
            logstack.warning('🟡 LAUNCHING較快結束，但尚未出現登入鈕，請確認是否有其他流程。')

    def login(
            self,
            user: dict,
            select_remember: bool = True,
            real_password: bool = False,
            screenshot: bool = False
    ):
        """
        CUBE登入功能
        """
        logstack.info('⏳ login ⏳')

        # 先確認語言
        if self.login_page.language.text == 'EN':
            logstack.info('🟢 目前是英文版，先切換成中文版')
            self.login_page.language.click()
            self.login_page.language_zh.click()
            self.login_page.language_save_button.click()
            if self.login_page.language.text == 'ZH':
                logstack.info('✅ 成功切換成中文版')
            else:
                logstack.error('❌ 尚未切換成中文版，請確認是否有其他問題。')

        # 開始登入
        logstack.info(f'👤 使用者資訊: {user}')
        self.login_page.login_button.wait_present()
        if screenshot:
            self.login_page.save_screenshot('登入', '登入頁面')
        rmb_status = self.confirm_remember_status(select_remember)
        username = 'qatest123'
        password = '1111'
        if real_password:
            username = user['username_real']
            password = user['psw_real']
        self.login_page.userid_input.send_keys(user['id'])
        self.login_page.username_input.send_keys(username)
        self.login_page.userpsw_input.send_keys(password)
        self.keyboard.done.click()
        if screenshot:
            self.login_page.save_screenshot('登入', '登入頁面輸入帳密完畢')
        self.login_page.login_button.click()
        popup_result = self.skip_login_to_home_popups(real_password, rmb_status, 1, screenshot)
        if real_password:
            logstack.info('🟢 使用真實密碼，檢查至登入兩步驟前為止\n')
        else:
            logstack.info(f'✅ 結束登入並已顯示首頁內容\n')
        logstack.info('⌛️ login ⌛️\n')
        return popup_result

    def logout(self, screenshot: bool = False):
        """
        CUBE登出功能
        """
        logstack.info('⏳ logout ⏳')
        if screenshot:
            self.bottom.save_screenshot("登出確認", "開始登出")
        self.bottom.more.click()
        self.more_page.logout_button.click()
        # 注意此處現在可能有版本更新通通知彈窗，用共用登出文本判斷
        self.more_page.logout_popup_logout_button.click()
        self.login_page.login_button.wait_present()
        logstack.info('⌛️ logout ⌛️\n')

    def skip_inform_popups(self, timeout=1):
        """
        略過通知彈窗
        """
        if self.login_page.login_button.is_present(timeout):
            logstack.info('✅ 已出現登入按鈕 無任何通知彈窗')
            return True
        count = 0
        while self.inform_popup.scrollviews.quantity >= 2:
            count += 1
            accept = self.inform_popup.accept
            logstack.warning(f'🟡 出現第 {count} 個通知彈窗，準備點擊按鈕 {accept.text}')
            self.inform_popup.save_screenshot("略過通知彈窗", "略過通知彈窗")
            accept.click()
        logstack.warning(f'🟡 共略過 {count} 個通知彈窗')
        return count

    def wait_launching(self, etimeout=1, netimeout=60):
        """
        等待 cube launching 頁面消失
        """
        return self.wait_loading_by(self.launch_page.logo, etimeout, netimeout)

    def wait_app_loading(self, etimeout=1, netimeout=60):
        """
        等待 cube 原生的 loading icon 消失
        ACCESSIBILITY_ID: 'SVProgressHUD'
        """
        return self.wait_loading_by(self.loading.app_loading, etimeout, netimeout)

    def wait_app_progressing(self, etimeout=1, netimeout=60):
        """
        等待 accessibility id = "進行中" 的元素消失
        ACCESSIBILITY_ID: '進行中'
        """
        return self.wait_loading_by(self.loading.app_progressing, etimeout, netimeout)

    def wait_app_activity_indicator_loading(self, etimeout=1, netimeout=60):
        """
        等待 XCUIElementTypeActivityIndicator 類別的元素消失
        IOS_CLASS_CHAIN: '**/XCUIElementTypeActivityIndicator[-1]'
        """
        return self.wait_loading_by(self.loading.app_activity_indicator, etimeout, netimeout)

    def wait_app_progress_indicator_loading(self, etimeout=1, netimeout=60):
        """
        等待 XCUIElementTypeProgressIndicator 類別的元素消失
        IOS_CLASS_CHAIN: '**/XCUIElementTypeProgressIndicator[-1]'
        """
        return self.wait_loading_by(self.loading.app_progress_indicator, etimeout, netimeout)

    def wait_webview_redirecting(self, etimeout=3, netimeout=60):
        """
        等待 cube webview 內嵌頁面的 redirect 消失
        ACCESSIBILITY_ID: 'SuperRedirect'
        """
        return self.wait_loading_by(self.loading.webview_redirecting, etimeout, netimeout)

    def wait_webview_progressing(
        self,
        timeout: int = 60,
        poll: int = 1,
        tolerance: int = 99,
    ):
        """
        確認webview進度條和當前視窗寬度一致
        """
        # 設定等待與通過門檻
        element = self.loading.webview_progressing
        window_width = self.page.get_window_size()['width']
        passing_width = int(window_width * tolerance / 100)

        # 開始執行等待
        end_time = time.monotonic() + timeout
        while True:
            element_width = element.size['width']
            logstack.info(f'🟢 視窗寬度: {window_width}')
            logstack.info(f'🟢 通過閥率: {tolerance}%')
            logstack.info(f'🟢 通過閥値: {passing_width}')
            logstack.info(f'---------------------------')
            logstack.info(f'🕛 目前閥値: {element_width}')
            logstack.info(f'🕛 目前進度: {int(element_width / window_width * 100)}%')
            if element_width < passing_width:
                logstack.info(f'🟡 尚未完成 webview progressing，繼續等待。\n')
                time.sleep(poll)
                if time.monotonic() > end_time:
                    error_message = f'❌ 已達 timeout {timeout} 秒，尚未完成 webview loading。\n'
                    raise TimeoutException(error_message)
            else:
                logstack.info(f'✅ 已於 {timeout} 秒內完成 webview progressing。\n')
                return True

    def wait_webview_loading(self, etimeout=3, netimeout=60):
        """
        等待 cube webview 內嵌頁面的 loading 消失
        IOS_PREDICATE: 'name IN {"Loading", "LOADING"} OR name CONTAINS "讀取中"'
        """
        return self.wait_loading_by(self.loading.webview_loading, etimeout, netimeout)

    def wait_webview_all_loading(self, start: int = 3, end: int = 60):
        """
        執行webview所有等待狀況

        wait_app_loading
        wait_webview_progressing
        wait_webview_loading
        """
        self.wait_app_loading(start, end)
        self.wait_webview_progressing(end)
        self.wait_webview_loading(start, end)

    def wait_loading_by(self, element: Element, etimeout: int = 1, netimeout: int = 30):
        """
        等待指定的 loading 元素消失
        """
        result = None
        remark = element.remark
        if element.is_present(etimeout):
            logstack.info(f'🟢 {etimeout}秒內 出現 {remark}')
            if element.wait_not_present(netimeout, False):
                logstack.info(f'✅ {netimeout}秒內 完成 {remark}\n')
                result = True
            else:
                logstack.warning(f'🟡 {netimeout}秒內 未完成 {remark}\n')
                result = False
        else:
            logstack.info(f'✅ 無任何 {remark}\n')
            result = True
        return result

    def confirm_remember_status(self, select: bool | None = None):
        """
        確保記住我的勾選狀態
        """
        if not isinstance(select, (bool, type(None))):
            raise TypeError('❌ 參數 "select" 應為 bool 或 None')

        current_status = self.login_page.remember_radio.is_selected()
        current_status_text = '已勾選' if current_status else '未勾選'
        logstack.info(f'🟢 目前記住我狀態為: {current_status_text}')

        if select is None:
            logstack.info('✅ 不執行任何動作')
            return current_status

        if select != current_status:
            select_action = '勾選' if select else '取消勾選'
            logstack.info(f'🟢 開始執行 {select_action}記住我')
            self.login_page.remember_radio.click()
            new_status = self.login_page.remember_radio.is_selected()
            if select == new_status:
                logstack.info(f'✅ 成功執行 {select_action}記住我')
            else:
                logstack.error(f'❌ 未成功執行 {select_action}記住我')
            return new_status

        logstack.info(f'✅ 當前狀態已符合預期，無需執行任何動作')
        return current_status

    def skip_login_to_home_popups(
            self,
            real_password: bool = False,
            remember_status: bool = True,
            timeout: int = 1,
            screenshot: bool = False,
    ):
        """
        略過從登入到首頁會出現的彈窗
        """
        self.wait_app_loading()
        login_popups = self.skip_login_popups(real_password, remember_status, timeout, screenshot)
        if login_popups['tfa']:
            return login_popups
        self.wait_launching()
        home_popups = self.skip_upgrade_password_popup(timeout, screenshot)
        return {**login_popups, **home_popups}

    def skip_login_popups(
            self,
            real_password: bool = False,
            remember_status: bool = True,
            timeout: int = 1,
            screenshot: bool = False,
            assert_content: bool = False):
        """
        略過點擊登入按鈕後到進入首頁前所有可能彈窗
        """
        abnormal = remember = fido = tfa = password = False
        while self.login_popup.common_text.is_present(timeout):
            popup_text = self.login_popup.common_text.text
            if screenshot:
                self.login_popup.save_screenshot('略過登入彈窗', popup_text)
            if '未正常登出' in popup_text:
                logstack.info('🟢 出現 未正常登出 彈窗')
                abnormal = True
                self.login_popup.abnormal_accept.click()
            elif remember_status and ('裝置記住我' in popup_text):
                logstack.info('🟢 出現 裝置記住我 彈窗')
                remember = True
                self.login_popup.remember_accept.click()
            elif '生物辨識' in popup_text:
                logstack.info('🟢 出現 生物辨識 彈窗')
                fido = True
                self.login_popup.fido_dismiss.click()
            elif real_password and '兩步驟驗證' in popup_text:
                logstack.info('🟢 出現 兩步驟驗證 彈窗')
                tfa = True
                self.login_popup.tfa_confirm.click()
                break
            # TODO 此處先保留，如果後續有case會觸發則啟用
            # elif real_password and ('變更密碼' in popup_text):
            #     logstack.info('🟢 出現 變更密碼 彈窗')
            #     password = True
            #     self.login_popup.psw_accept.click()
            else:
                raise ValueError('❌ 無對應彈窗，請再次確認彈窗文本')
            self.wait_app_loading()
        if screenshot:
            self.login_popup.save_screenshot('略過登入彈窗', '結束略過登入彈窗')
        return {'abnormal': abnormal, 'remember': remember, 'fido': fido, 'tfa': tfa, 'password': password}

    def skip_upgrade_password_popup(self, timeout: int = 1, screenshot: bool = False):
        """
        略過變更密碼彈窗並顯示首頁
        """
        upgrade = False
        if not self.home_page.title_.is_visible():
            upgrade = self.skip_popup(self.home_popup.upgrade_psw_title,
                                      self.home_popup.upgrade_psw_dismiss,
                                      timeout,
                                      screenshot)
        if self.home_page.title_.wait_visible():
            logstack.info('✅ 已顯示首頁標題')
        else:
            logstack.warning('🟡 尚未顯示首頁標題，請接續確認 home_page_wait_screenshot 流程是否成功')
        # 主流程還是要看到首頁截圖，因此不在此處截圖
        return {'upgrade': upgrade}

    def skip_popup(
            self,
            reference_element: Element,
            button_element: Element,
            timeout: int = 3,
            screenshot: bool = True):
        """
        判斷如何執行顯示的彈窗
        :param reference_element: 欲等待的彈窗元素
        :param button_element: 欲執行的彈窗按鈕
        """
        reference_element_remark = reference_element.remark
        button_element_remark = button_element.remark
        result = False
        logstack.info(f'reference element: {reference_element_remark}')
        if reference_element.is_present(timeout):
            logstack.info(f'button element: {button_element_remark}')
            if screenshot:
                self.page.save_screenshot('不定彈窗', reference_element_remark)
            button_element.click()
            result = True
        result_text = '✅ 有出現' if result else '❎ 未出現'
        logstack.info(f'{result_text}彈窗\n')
        return result

    def verify_otp(self, otp: str = '555666', confirm: bool = True, screenshot: bool = True):
        """
        共用輸入OTP流程
        """
        self.tfa_otp_page.input_field.click()
        for n in otp:
            self.keyboard.number(n).click()
        self.keyboard.done.click()
        if screenshot:
            self.tfa_otp_page.save_screenshot("輸入otp", "輸入otp完成", 1)
        if confirm:
            self.tfa_otp_page.confirm_button.click()

    def login_tfa_flow(self, otp: str = '555666'):
        """
        判斷是否有登入並啟用兩步驟驗證流程
        """
        flow = '登入兩步驟驗證'

        if self.tfa_verify_popup.title_.is_present(3):
            logstack.info('🟡 需要登入兩步驟驗證')

            # 登入兩步驟驗證彈窗
            self.tfa_verify_popup.title_.wait_present()
            self.tfa_verify_popup.save_screenshot(flow, "登入兩步驟驗證彈窗")
            self.tfa_verify_popup.confirm.click()

            self.wait_app_loading()

            # 登入兩步驟驗證頁 立即啟用
            self.tfa_verify_page.image.wait_present(3)
            self.tfa_verify_page.save_screenshot(flow, "登入兩步驟驗證頁")
            self.tfa_verify_page.accept.click()

            self.wait_app_loading()

            # 啟用兩步驟驗證頁 輸入otp
            self.verify_otp(otp)

            self.wait_app_loading()

            # 啟用兩步驟驗證頁 設定裝置名稱
            self.tfa_activate_page.device_image.wait_present()
            self.tfa_activate_page.save_screenshot(flow, "設定裝置名稱")
            self.tfa_activate_page.activate_confirm_button.click()

            # 啟用兩步驟驗證頁 啟用成功
            self.tfa_activate_page.activate_success.wait_visible()
            self.tfa_activate_page.save_screenshot(flow, "啟用結果")
            self.tfa_activate_page.activate_done_button.click()

        else:
            logstack.info('✅ 無需登入兩步驟驗證')

        # 等待 launching 結束
        self.wait_launching(3, 30)

    def get_border(self, others_timeout: int = 1):
        """
        注意：更多功能頁因為多了登出框，請用 get_table_border 就好，否則 table bottom 會是錯的。

        判斷 Table 或 ScrollView 類別元素的邊界
        先以 Table 為準，沒有時再用 ScrollView 判斷
        """
        try:
            table_border = self.border_object.table.border
            if self.border_object.tabbar.is_present(others_timeout):
                table_border['bottom'] = self.border_object.tabbar.border['top']
            return table_border
        except Exception:
            return self.border_object.scrollview.border

    def get_table_border(self, order: int = 1):
        """
        取得 XCUIElementTypeTable 類別元素的邊界，
        order 即為索引值，利用 IOS_CLASS_CHAIN **/XCUIElementTypeTable[{order}] 定位
        """
        q_tables = self.border_object.tables.quantity
        if q_tables == 0:
            logstack.warning('🟡 無任何 Table，先以目前視窗為邊界。如不符合需求，請改用其他元素取得邊界')
            border = self.page.get_window_border()
        elif q_tables == 1:
            logstack.info('✅ 只有一個 Table，取其作為邊界。')
            border = self.border_object.table_order(1).border
        else:
            logstack.info(f'✅ 有多個 Table，指定第 {order} 個 Table 作為邊界。')
            border = self.border_object.table_order(order).border
        return border

    def get_scrollview_border(self):
        """
        取得 XCUIElementTypeScrollView 類別元素的邊界
        """
        return self.border_object.scrollview.border

    def go_to_login_page(self, case: str, name: str = '登入頁'):
        """
        此處將斷言登入頁是否依條件顯示，並將此流程放到登入前的每個測案的第一步
        """
        self.login_page.login_button.wait_clickable()
        self.save_screenshot(case, name)

    def go_to_home_page(self, case: str, name: str = '登入到首頁', screenshot: bool = True, skip_errors: bool = False):
        """
        此處將斷言首頁是否依條件顯示，並將此流程放到登入後的每個測案的第一步
        """
        self.home_page.wait_amounts.wait_any_visible()
        if screenshot:
            self.save_screenshot(case, name, skip_errors=skip_errors)

    def save_screenshot(
            self,
            case: str = 'case',
            name: str = 'name',
            sleep: int = 0.5,
            to_jpg: bool = True,
            jpg_ratio: int = 50,
            jpg_quality: int = 50,
            attach: bool = True,
            attach_jpg: bool = True,
            remove: bool = True
    ):
        """
        save_screenshot 後斷言頁面是否有錯誤訊息
        可先在前面斷言 assume.wait() 等待條件後再使用 save_screenshot
        不需再用 wait_screenshot 放入 waits 的方式了
        """
        self.page.save_screenshot(
            case,
            name,
            sleep,
            to_jpg,
            jpg_ratio,
            jpg_quality,
            attach,
            attach_jpg,
            remove)
