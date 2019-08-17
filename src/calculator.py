def calculate_position(
        direction, min_hold_time, max_hold_time, stop_loss_probabilities,
        take_profit_probabilities, exchange, instrument_ticker):
    """Calculate stop-loss and take-profit levels for position, depending on current market volatility

    :param str direction: position direction ('long' or 'short') (required)
    :param str min_hold_time: minimal estimated position holding time (to calculate stop-loss level)
        in minutes (int) or string format (12h for hours) (required)
    :param str max_hold_time: maximal estimated position holding time (to calculate take-profit level)
        in minutes (int) or string format (12h for hours) (required)
    :param (list of float) stop_loss_probabilities: stop-losses triggering probabilities (required)
    :param (list of float) take_profit_probabilities: take-profits filling probabilities (required)
    :param str exchange: exchange name (required)
    :param str instrument_ticker: instrument ticker on exchange (required)
    :return (dict of str: list) position: position data
    """

    position = {
        'stop-loss': [],
        'take-profit': [],
    }
    return position
