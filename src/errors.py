def exchange_name_invalid(name):
    """Invalid exchange name"""
    raise ValueError(f'Exchange `{name}` is not supported now.')


def instrument_ticker_invalid(ticker):
    """Invalid ticker"""
    raise ValueError(f'Ticker `{ticker}` is not supported now.')


def market_data_type_invalid():
    """Invalid market price data type"""
    raise TypeError(f'Market price data is not a dictionary.')


def market_data_not_have_key(key_name):
    """Market price data don't have a key"""
    raise ValueError(f'Market price data don`t have a key `{key_name}`.')


def market_data_empty():
    """One or more keys of market price data are empty"""
    raise ValueError(f'One or more keys of market price data are empty.')


def market_data_key_size_invalid(key_name, expected, real):
    """Invalid market price data size in candles"""
    raise ValueError(f'Market price data key `{key_name}` have {real} candles, expected {expected}.')

