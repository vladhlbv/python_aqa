import pytest
import time
from lesson_19_2.console_logger_setup import console_logger
from lesson_27.page_objects.nova_post_page_object import NovaPostPageObject

class TestNovaPost:

    def test_parcel_track_status(self, nova_post_track_page: NovaPostPageObject):

        nova_post_track_page.open()

        time.sleep(1)

        nova_post_track_page.input_track_number("20451211207022")

        time.sleep(1)

        nova_post_track_page.click_on_search_button()

        time.sleep(1)

        nova_post_track_page.click_on_agree_button()

        time.sleep(1)

        nova_post_track_page.check_parcel_status("Отримана")

        time.sleep(1)