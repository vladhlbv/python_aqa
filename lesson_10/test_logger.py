from lesson_10.homework_10 import log_event

class TestLogger:

    def test_log_username(self):
        """
        Creating a new log message in file and checking if username in a message equals to expected username
        """
        username: str = "Vlad"
        status: str = "success"
        log_event(username=username, status=status)

        with open("login_system.log", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]

        assert username in last_line, f"{username} does not contain in {last_line}"


    def test_log_status(self):
        """
        Creating a new log message in file and checking if status in a message equals to expected status
        """
        username: str = "Dmytro"
        status: str = "expired"
        log_event(username=username, status=status)

        with open("login_system.log", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]

        assert status in last_line, f"{status} does not contain in {last_line}"


    def test_log_level_info(self):
        """
        Creating a new log message in file with Success status and checking if log level used in a message equals to expected log level
        """
        username: str = "Cody"
        status: str = "success"
        level: str = "INFO"
        log_event(username=username, status=status)

        with open("login_system.log", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]

        assert level in last_line, f"{level} does not contain in {last_line}"


    def test_log_level_warning(self):
        """
        Creating a new log message in file with Warning status and checking if log level used in a message equals to expected log level
        """
        username: str = "David"
        status: str = "expired"
        level: str = "WARNING"
        log_event(username=username, status=status)

        with open("login_system.log", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]

        assert level in last_line, f"{level} does not contain in {last_line}"


    def test_log_level_error(self):
        """
        Creating a new log message in file with Error status and checking if log level used in a message equals to expected log level
        """
        username: str = "Max"
        status: str = "failed"
        level: str = "ERROR"
        log_event(username=username, status=status)

        with open("login_system.log", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]

        assert level in last_line, f"{level} does not contain in {last_line}"