import os
import logging
from constants import *


class LoggerSetup():

    def __init__(self):
        self.logger = logging.getLogger(__name__)  
         
    def setup(self, level: str, path: str):
        self.logger.setLevel(level)
        file_handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.realpath(__file__)), path))
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        

