def fetch_market_price_data(exchange, instrument_ticker):
    """Calls appropriate function for given exchange and instrument

    :param str exchange: exchange name (required)
    :param str instrument_ticker: instrument ticker on exchange (required)
    :return (dict of str: list) market_price_data: candlestick market price data
    """

    market_price_data = {
        'volume': [],
        'ticks': [],
        'open': [],
        'low': [],
        'high': [],
        'close': []
    }
    return market_price_data
