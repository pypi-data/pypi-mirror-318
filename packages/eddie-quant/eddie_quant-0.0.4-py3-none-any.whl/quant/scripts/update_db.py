from quant.app.init import init_app_service


def main():
    tickers = [
        "AAPL",
    ]

    app = init_app_service()
    app.update_ticker_info(tickers)
