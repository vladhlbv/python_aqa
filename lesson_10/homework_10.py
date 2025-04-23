"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str) -> None:
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """

    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logger = logging.getLogger("log_event")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler('login_system.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


def get_log_lastline() -> list:
    """

    :return:
    """
    with open("login_system.log", "r") as f:
        lines: list= f.readlines()
        if lines:
            last_line: str = lines[-1]
        split_last_line: list = last_line.split(" - ")
        return split_last_line

def get_last_username() -> str:
    """
    Returns username value used in last log row
    :return: Username value
    """
    last_line: list = get_log_lastline()
    last_line_split: list = last_line[3].split(", ")
    username_split: list = last_line_split[0].split(": ")
    username_value: str = username_split[-1]
    return username_value


def get_last_status() -> str:
    """
    Returns status value used in last log row
    :return: Status value
    """
    last_line: list = get_log_lastline()
    last_line_split: list = last_line[3].split(": ")
    status_split: list = last_line_split[-1].split("\n")
    status_value: str = status_split[0]
    return status_value


def get_last_log_level() -> str:
    """
    Returns value log level used in last log row
    :return: Log level value
    """
    last_line: list = get_log_lastline()
    log_level: str = last_line[1]
    return log_level

if __name__ == "__main__":
    print(get_log_lastline())