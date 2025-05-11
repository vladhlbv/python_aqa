import logging

console_logger = logging.getLogger("log_event_console")
console_logger.setLevel(logging.INFO)

if not console_logger.handlers:
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    console_logger.addHandler(console_handler)