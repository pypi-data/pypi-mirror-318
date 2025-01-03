import logging

global FORCE
FORCE = False


def create_logger(name='objwatch', output=None, level=logging.DEBUG, simple=False):
    if level == "force":
        global FORCE
        FORCE = True
        return

    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        if simple:
            formatter = logging.Formatter('%(levelname)s: %(message)s')
        else:
            formatter = logging.Formatter(
                '[%(asctime)s] [%(levelname)s] %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
            )
        logger.setLevel(level)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        if output:
            file_handler = logging.FileHandler(output)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    logger.propagate = False


logger = logging.getLogger('objwatch')


def get_logger():
    return logger


def log_info(msg, *args, **kwargs):
    global FORCE
    if FORCE:
        print(msg, flush=True)
    else:
        logger.info(msg, *args, **kwargs)


def log_debug(msg, *args, **kwargs):
    global FORCE
    if FORCE:
        print(msg, flush=True)
    else:
        logger.debug(msg, *args, **kwargs)


def log_warn(msg, *args, **kwargs):
    global FORCE
    if FORCE:
        print(msg, flush=True)
    else:
        logger.warning(msg, *args, **kwargs)
