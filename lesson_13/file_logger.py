import logging

file_logger = logging.getLogger("log_event_file")
file_logger.setLevel(logging.INFO)

if not file_logger.handlers:
    handler = logging.FileHandler('logged_events.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    file_logger.addHandler(handler)