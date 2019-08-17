import openapi_client
from openapi_client.rest import ApiException
import src.validator as validator


def fetch_market_price_data(instrument_ticker, candle_properties):
    """Fetches market price data for given instrument on deribit.com

    :param str instrument_ticker: instrument ticker (required)
    :param (dict of str: int) candle_properties: properties of fetching candles (resolution, amount,
     start_time, end_time)
    :return (dict of str: list) market_price_data: candlestick market price data
    :raises ApiException: deribit api response error
    :raises TypeError: received market price data from deribit type is not a dictionary
    :raises ValueError: invalid received from deribit market price data
    """

    configuration = openapi_client.Configuration()
    api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))
    market_price_data = {}

    try:
        api_response = api_instance.public_get_tradingview_chart_data_get(
            instrument_ticker, candle_properties['start_time'], candle_properties['end_time'],
            candle_properties['resolution'])
        market_price_data = api_response['result']
    except ApiException as e:
        print("Exception when calling deribit API: PublicApi->public_get_tradingview_chart_data_get: %s\n" % e)

    if validator.validate_market_price_data(market_price_data, candle_properties['amount']):
        return market_price_data
