import logging
from datetime import datetime


class logGen:
    @staticmethod
    def loggen():
        #generate the file name with current date & time and convert to string
        currnt_time=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_filename=f".\\Logs\\SwageLab_{currnt_time}.log"
        #f stands for formatted string literal

        logging.basicConfig(filename=log_filename,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %H:%M:%S',
                            force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger