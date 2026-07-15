import sys

from logging import getLogger, DEBUG, StreamHandler, Logger, Formatter


def get_logger(name:str) -> Logger:


    logger = getLogger(name)

    if not logger.handlers:
        hdlr = StreamHandler(sys.stdout)
        hdlr.setLevel(DEBUG)

        fmt = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        hdlr.setFormatter(fmt)

        logger.addHandler(hdlr)
    
    return logger