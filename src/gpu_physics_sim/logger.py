import sys

import logging


def setup_logger():

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    if root.handlers:
        return

    hdlr = logging.StreamHandler(sys.stdout)
    
    fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(name)s: %(message)s")
    hdlr.setFormatter(fmt)

    root.addHandler(hdlr)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
