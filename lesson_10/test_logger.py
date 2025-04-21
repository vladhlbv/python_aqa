import pytest
from lesson_10.homework_10 import log_event, get_last_username, get_last_status, get_last_log_level


class TestLogger:

    def test_log_username(self):
        """
        Creating a new log message in file and checking if username in a message equals to expected username
        """
        username: str = "Vlad"
        status: str = "success"
        log_event(username=username, status=status)

        assert username == get_last_username(), f"Actual username:{username} does not equal to expected username:{get_last_username()}"


    def test_log_status(self):
        """
        Creating a new log message in file and checking if status in a message equals to expected status
        """
        username: str = "Dmytro"
        status: str = "expired"
        log_event(username=username, status=status)

        assert status == get_last_status(), f"Actual status:{status} does not equal to expected status:{get_last_status()}"


    def test_log_level_info(self):
        """
        Creating a new log message in file with Success status and checking if log level used in a message equals to expected log level
        """
        username: str = "Cody"
        status: str = "success"
        level: str = "INFO"
        log_event(username=username, status=status)

        assert level == get_last_log_level(), f"Actual log level:{level} does not equal to expected log level:{get_last_log_level()}"


    def test_log_level_warning(self):
        """
        Creating a new log message in file with Warning status and checking if log level used in a message equals to expected log level
        """
        username: str = "David"
        status: str = "expired"
        level: str = "WARNING"
        log_event(username=username, status=status)

        assert level == get_last_log_level(), f"Actual log level:{level} does not equal to expected log level:{get_last_log_level()}"


    def test_log_level_error(self):
        """
        Creating a new log message in file with Error status and checking if log level used in a message equals to expected log level
        """
        username: str = "Max"
        status: str = "failed"
        level: str = "ERROR"
        log_event(username=username, status=status)

        assert level == get_last_log_level(), f"Actual log level:{level} does not equal to expected log level:{get_last_log_level()}"