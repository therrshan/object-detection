import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


log_path = os.path.join( 'log', LOG_FILE)

os.makedirs(log_path, exist_ok=True)

lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=lOG_FILE_PATH,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)