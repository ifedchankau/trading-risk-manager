from src.exchange_api.deribit import fetch_market_price_data as deribit_fetch_prices
import src.errors as errors


def fetch_market_price_data(exchange, instrument_ticker, candle_properties):
    """Calls appropriate function for given exchange and instrument

    :param str exchange: exchange name (required)
    :param str instrument_ticker: instrument ticker on exchange (required)
    :param (dict of str: int) candle_properties: properties of fetched candles (required)
    :return (dict of str: list) market_price_data: candlestick market price data
    """

    if exchange == 'deribit':
        return deribit_fetch_prices(instrument_ticker, candle_properties)
    else:
        errors.exchange_name_invalid(exchange)
