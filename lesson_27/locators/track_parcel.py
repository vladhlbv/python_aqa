from enum import Enum
from selenium.webdriver.common.by import By

class NovaPostLocators(Enum):

    TRACK_NUM_TXT: tuple[str, str] = (By.XPATH, "//input[@id='en']")
    SEARCH_BTN: tuple[str, str] = (By.XPATH, "//input[@id='np-number-input-desktop-btn-search-en']")
    PARCEL_STATUS_FLD: tuple[str, str] = (By.XPATH, "//div[@class='header__status-text']")
    AGREE_BTN: tuple[str, str] = (By.XPATH, "//button[@class='button v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default']")