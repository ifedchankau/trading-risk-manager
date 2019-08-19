import openapi_client
from openapi_client.rest import ApiException
import src.errors as errors


def fetch_candlestick_price_data(ticker, candles_properties):
    """Fetches candlestick market price data for given instrument on deribit.com

    :param str ticker: instrument ticker (required)
    :param (dict of str: int) candles_properties: properties of candles (resolution, amount, start_time, end_time)
    :return (dict of str: list): candlestick market price data
    :raises ApiException: deribit api response error
    """

    configuration = openapi_client.Configuration()
    api_instance = openapi_client.PublicApi(openapi_client.ApiClient(configuration))

    try:
        api_response = api_instance.public_get_tradingview_chart_data_get(
            ticker, candles_properties['start_time'], candles_properties['end_time'], candles_properties['resolution'])
        return {
            'length': len(api_response['result']['ticks']),
            'ticks': api_response['result']['ticks'],
            'volume': api_response['result']['volume'],
            'open': api_response['result']['open'],
            'low': api_response['result']['low'],
            'high': api_response['result']['high'],
            'close': api_response['result']['close']
        }
    except ApiException as error_code:
        errors.deribit_fetch_market_price_data_request_failed(error_code)
