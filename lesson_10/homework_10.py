"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

logger = logging.getLogger("log_event")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('login_system.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s -  %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_event(username: str, status: str) -> None:
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    # print(f"Logging username {username} with status {status}")

    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    # logging.basicConfig(
    #     filename='login_system.log',
    #     level=logging.INFO,
    #     format='%(asctime)s - %(levelname)s -  %(message)s'
    # )
    # logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)