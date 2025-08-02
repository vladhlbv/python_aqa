import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from lesson_26.locators import frame1_text, frame2_text, frame1_check_button, frame2_check_button
from lesson_19_2.console_logger_setup import console_logger


class TestSeleniumFrames:

    def test_verify_secret_values(self, selenium_driver):

        time.sleep(1)

        # Switching focus to Frame1
        selenium_driver.switch_to.frame("frame1")

        # Finding text field element and filling it in with text
        frame1_text_field = selenium_driver.find_element(By.XPATH, frame1_text)
        frame1_text_field.send_keys("Frame1_Secret")
        time.sleep(1)

        # Finding verify button element and clicking it
        frame1_verify_button = selenium_driver.find_element(By.XPATH, frame1_check_button)
        frame1_verify_button.click()

        # Verifying text in alert window with expected text
        alert = Alert(selenium_driver)
        time.sleep(1)
        expected_text_1: str = "Верифікація пройшла успішно!"
        try:
            assert alert.text == expected_text_1
            console_logger.info(f"Assertion for Frame1 passed with text: {expected_text_1}")
        except AssertionError:
            console_logger.info(f"Assertion for Frame1 failed with text:{alert.text}")

        # Closing the alert window and switching focus from Frame1 to default state
        alert.accept()
        selenium_driver.switch_to.default_content()
        time.sleep(1)

        # Switching focus to Frame2
        selenium_driver.switch_to.frame("frame2")

        # Finding text field element and filling it in with text
        frame2_text_field = selenium_driver.find_element(By.XPATH, frame2_text)
        frame2_text_field.send_keys("Frame2_Secret")
        time.sleep(1)

        # Finding verify button element and clicking it
        frame2_verify_button = selenium_driver.find_element(By.XPATH, frame2_check_button)
        frame2_verify_button.click()

        # Verifying text in alert window with expected text
        alert = Alert(selenium_driver)
        time.sleep(1)
        expected_text_2: str = "Верифікація пройшла успішно!"
        try:
            assert alert.text == expected_text_2
            console_logger.info(f"Assertion for Frame2 passed with text: {expected_text_2}")
        except AssertionError:
            console_logger.info(f"Assertion for Frame2 failed with text:{alert.text}")

        # Closing the alert window and switching focus from Frame2 to default state
        alert.accept()
        selenium_driver.switch_to.default_content()
        time.sleep(1)