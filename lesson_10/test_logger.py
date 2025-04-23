import pytest
from lesson_10.homework_10 import log_event, get_last_username, get_last_status, get_last_log_level


class TestLogger:

    def test_log_status_success(self):
        """
        Creating a new log message in file with Success status,
        checking if username, status in a message equals to expected username and status,
        also checking if log level used in a message equals to Info log level
        """
        username: str = "Cody"
        status: str = "success"
        level: str = "INFO"
        log_event(username=username, status=status)

        assert status == get_last_status(), f"Actual status:{status} does not equal to expected status:{get_last_status()}"
        assert username == get_last_username(), f"Actual username:{username} does not equal to expected username:{get_last_username()}"
        assert level == get_last_log_level(), f"Actual log level:{level} does not equal to expected log level:{get_last_log_level()}"


    def test_log_status_expired(self):
        """
        Creating a new log message in file with Expired status,
        checking if username, status in a message equals to expected username and status,
        also checking if log level used in a message equals to Warning log level
        """
        username: str = "David"
        status: str = "expired"
        level: str = "WARNING"
        log_event(username=username, status=status)

        assert status == get_last_status(), f"Actual status:{status} does not equal to expected status:{get_last_status()}"
        assert username == get_last_username(), f"Actual username:{username} does not equal to expected username:{get_last_username()}"
        assert level == get_last_log_level(), f"Actual log level:{level} does not equal to expected log level:{get_last_log_level()}"


    def test_log_status_failed(self):
        """
        Creating a new log message in file with Failed status,
        checking if username, status in a message equals to expected username and status,
        also checking if log level used in a message equals to Error log level
        """
        username: str = "Max"
        status: str = "failed"
        level: str = "ERROR"
        log_event(username=username, status=status)

        assert status == get_last_status(), f"Actual status:{status} does not equal to expected status:{get_last_status()}"
        assert username == get_last_username(), f"Actual username:{username} does not equal to expected username:{get_last_username()}"
        assert level == get_last_log_level(), f"Actual log level:{level} does not equal to expected log level:{get_last_log_level()}"