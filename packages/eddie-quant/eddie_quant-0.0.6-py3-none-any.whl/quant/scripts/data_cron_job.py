import threading
import time

from loguru import logger

from quant.app.init import init_app_service
from quant.app.service import AppService


def run():
    app = init_app_service()
    update_tickers_data(app=app)


def update_tickers_data(app: AppService):
    tickers = app.get_ticker_info(symbols=None)
    threads = []

    for ticker in tickers:
        t = threading.Thread(target=update_ticker_data, args=(app, ticker.symbol,))
        threads.append(t)
        t.start()
        logger.info(f"start to update ticker data for {ticker.symbol}")
        time.sleep(1)

    for t in threads:
        t.join()

    logger.info(f"finish updating ticker data for {tickers}")


def update_ticker_data(app: AppService, symbol: str):
    latest_date = app.get_history_latest_date(symbol=symbol)
    if latest_date is None:
        app.update_full_history_data(symbols=[symbol])
    else:
        app.update_latest_history_data(symbols=[symbol])
    logger.info(f"finish updating ticker data for {symbol}")
