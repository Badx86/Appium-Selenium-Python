"""
10/10/2023 01:01:01 PM Sunday: INFO: Text Entered in edit box
10/10/2023 01:01:01 PM Sunday: ERROR: Enable to click 'Search' button

"""
import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename='test2.log',
    datefmt='%d/%m/%y %I:%M:%S %p %A', level=logging.DEBUG, filemode='a')  # %H:%M:%S -24h format, 'w' - overwrite
logging.critical("This is critical msg")
logging.error("This is an error msg")
logging.warning("This is a warning msg")
logging.info("This is an info msg")
logging.debug("This is a debug msg")
