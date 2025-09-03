import logging.config

logger = logging.getLogger("my_app")
logging_config = {
    "version" : 1,
    "disable_existing_loggers" : False,
    "formatters" : {},
    "handlers" : {},
    "loggers" : {}
}

def main():
    logging.config.dictConfig(config=logging_config)
    logger.addHandler(logging.StreamHandler(...))
    