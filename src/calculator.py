import src.api as api
import src.tools as tools
import src.validator as validator


def calculate_position(
        direction, min_hold_time, max_hold_time, stop_loss_probabilities,
        take_profit_probabilities, exchange, instrument_ticker):
    """Calculate stop-loss and take-profit levels for position, depending on current market volatility

    :param str direction: position direction ('long' or 'short') (required)
    :param int min_hold_time: minimal estimated position holding time (to calculate stop-loss level)
        in minutes (required)
    :param int max_hold_time: maximal estimated position holding time (to calculate take-profit level)
        in minutes (required)
    :param (list of float) stop_loss_probabilities: stop-losses triggering probabilities (required)
    :param (list of float) take_profit_probabilities: take-profits filling probabilities (required)
    :param str exchange: exchange name (required)
    :param str instrument_ticker: instrument ticker on exchange (required)
    :return (dict of str: list) position: position data
    """

    validator.validate_exchange_name(exchange)
    validator.validate_instrument_ticker(exchange, instrument_ticker)

    candle_properties = tools.get_candle_properties(min_hold_time)
    market_data = api.fetch_market_price_data(exchange, instrument_ticker, candle_properties)

    candle_properties = tools.get_candle_properties(max_hold_time)
    market_data = api.fetch_market_price_data(exchange, instrument_ticker, candle_properties)

    position = {
        'stop-loss': [],
        'take-profit': [],
    }
    return position
