"""
Logging means tracking the events or steps during the execution of programm or software

Log levels
==========
Critical
Error
Warning
Info
Debug

"""
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.critical("This is critical msg")
logging.error("This is an error msg")
logging.warning("This is a warning msg")
logging.info("This is an info msg")
logging.debug("This is a debug msg")