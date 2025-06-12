from Helper.helper import Helper
from selenium.webdriver.common.by import By


class Pracice(Helper):

    title = ((By.XPATH, "//title[text()='Practice Page']"), "title")
    btn_alert = ((By.ID, "alertbtn"), "btn_alert")
    btn_hide = ((By.ID, "hide-textbox"), "btn_hide")
    inp_example = ((By.ID, "displayed-text"), "inp_example")
    btn_mousehover = ((By.ID, 'mousehover'), "btn_mousehover")
    btn_top = ((By.XPATH, "//button[@id='mousehover']//following::a[text()='Top']"), "btn_top")
    footer = ((By.XPATH, "//div[contains(@class, 'footer')]//p"), "footer")
    btn_sign_in = ((By.XPATH, "//h1[text()='Practice Page']//preceding::a[text()='Sign In']"), "btn_sign_in")

    def save_alert_text(self):
        self.find_element_and_click(self.btn_alert)
        alert = self.driver.switch_to.alert
        self.write_in_file(f' Alert text is - {alert.text}')
        self.logger.info(f'Alert text is - {alert.text}')
        alert.accept()

    def hide_element_check(self):
        hide_el = self.find_element(self.inp_example)
        self.find_element_and_click(self.btn_hide)
        hide_attr = hide_el.get_attribute('style')
        self.write_in_file(f'Hidden attribute is - {hide_attr}')
        self.logger.info(f'Hidden attribute is - {hide_attr}')

    def mouse_hover_check(self):
        self.find_element_and_click(self.btn_mousehover)
        self.find_element_and_click(self.btn_top)

    def footer_text(self):
        self.find_element(self.footer)
        footer_text = self.find_element(self.footer).text
        self.write_in_file(f'Footer text is - {footer_text}')
        self.logger.info(f'Footer text is - {footer_text}')

