from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_27.locators.track_parcel import NovaPostLocators
from lesson_19_2.console_logger_setup import console_logger


class NovaPostPageObject:
    def __init__(self, web_driver):
        self.__web_driver = web_driver
        self.__wait = WebDriverWait(self.__web_driver, 5)

    @property
    def track_text_field(self):
        return self.__wait.until(EC.element_to_be_clickable(NovaPostLocators.TRACK_NUM_TXT.value))

    @property
    def search_button(self):
        return self.__wait.until(EC.element_to_be_clickable(NovaPostLocators.SEARCH_BTN.value))

    @property
    def parcel_status_field(self):
        return self.__wait.until(EC.element_to_be_clickable(NovaPostLocators.PARCEL_STATUS_FLD.value))

    @property
    def agree_button(self):
        return self.__wait.until(EC.element_to_be_clickable(NovaPostLocators.AGREE_BTN.value))

    def open(self):
        self.__web_driver.get('https://tracking.novaposhta.ua/#/uk')
        return self

    def input_track_number(self, track_num: str):
        self.track_text_field.send_keys(track_num)
        return self

    def click_on_search_button(self):
        self.search_button.click()
        return self

    def click_on_agree_button(self):
        self.agree_button.click()
        return self

    def check_parcel_status(self, expected_status: str):
        try:
            assert self.parcel_status_field.text == expected_status
            console_logger.info(f"Assertion passed with text: {expected_status}")
        except AssertionError:
            console_logger.info(f"Assertion failed with text: {self.parcel_status_field.text}")

        return self