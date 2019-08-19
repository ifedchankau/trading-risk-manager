import src.errors as errors
import os
import json


def validate_candlestick_price_data(data):
    """Validates candlestick market price data

    :param (dict of str: list) data: candlestick market price data
    :raises TypeError: market price data type is not a dictionary
    :raises ValueError: invalid market price data
    """

    required_keys = ['ticks', 'open', 'high', 'low', 'close', 'length']
    price_keys = ['ticks', 'open', 'high', 'low', 'close']
    if type(data) is not dict:
        errors.market_data_type_invalid()
    for field in required_keys:
        if field not in data:
            errors.market_data_not_have_key(field)

    length = data['length']
    for field in price_keys:
        if len(data[field]) == 0:
            errors.market_data_empty(field)
        if len(data[field]) != length:
            errors.market_data_key_size_invalid(field, length, len(data[field]))
    return True


def validate_exchange_name(exchange):
    """Validates exchange name by dictionary

    :param str exchange: exchange name
    :raises ValueError: invalid exchange name
    """

    # TODO: fix
    exchanges = json.load(open(os.path.dirname(__file__) + '/exchanges.json'))
    if exchange not in exchanges:
        errors.exchange_name_invalid(exchange)
    return True


def validate_instrument_ticker(exchange, ticker):
    """Validates ticker by dictionary

    :param str exchange: exchange name
    :param str ticker: instrument ticker
    :raises ValueError: invalid or unsupported instrument ticker
    """

    # TODO: fix
    exchanges = json.load(open(os.path.dirname(__file__) + '/exchanges.json'))
    if exchange not in exchanges:
        errors.exchange_name_invalid(exchange)
    if ticker not in exchanges[exchange]['tickers']['supported']:
        errors.instrument_ticker_invalid(ticker)
    return True
