# Write a program to log messages with timestamps into a file
#Logging
# Python's built-in logging module provides a flexible framework for tracking events during program execution, which is crucial for debugging and monitoring application behavior. 
import logging

# Configure logging to write to a file with timestamps
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Example log messages
logging.info("Program started")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.info("Program finished")
