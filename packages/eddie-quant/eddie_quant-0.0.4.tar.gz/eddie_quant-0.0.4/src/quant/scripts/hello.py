from loguru import logger

from quant.app.init import init_app_service


def main():
    init_app_service()
    logger.info("Hello World")
    logger.warning("Hello World")
    logger.error("Hello World")
