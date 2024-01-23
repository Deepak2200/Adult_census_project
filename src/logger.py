import logging
import os
from datetime import datetime
import sys


# here we make our path in our current working directory
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(log_path,exist_ok=True)

# here we make final full path of our log file(complete path)
LOG_FILE_PATH=os.path.join(log_path,log_file)


# log file formate by basicConfig
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)