import logging


class Base:

    def __init__(self):
        pass

    def run(self):
        pass


def loggingSetting():
    logger = logging.getLogger("slagManMoniotr")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("slagManMoniotr.log")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(levelname)s - %(message)s - %(lineno)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


logger = loggingSetting()
