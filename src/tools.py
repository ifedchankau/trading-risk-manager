def find_price_ranges(market_price_data, period_size_bars):
    """Calculates historical price ranges for a given period duration.

    For one period of bars ranges counts as:
    1st range: (high price in period - first bar opening price) / first bar opening price - 1
    2nd range: (first bar opening price - low price in period) / first bar opening price - 1
    The next period is obtained by a shift of always 1 bar.

    :param (dict of str: list) market_price_data: candlestick market price data (required)
    :param int period_size_bars: size of one period in bars (required)
    :return (list of float) price_ranges: all price ranges in market price data
    """

    price_ranges = []
    return price_ranges


def find_order_levels(price_ranges, order_probabilities):
    """Calculates orders price levels with given filling probability depending on historical market volatility

    :param (list of float) price_ranges: historical price ranges (required)
    :param (list of float) order_probabilities: order filling probabilities (required)
    :return (list of float) price_levels: price levels of orders
    """

    price_levels = []
    return price_levels


def get_candle_properties(hold_time):
    """
    Todo: realize function (issue #11)
    """

    candle_properties = {
        'resolution': 0,
        'amount': 0,
        'start_time': 0,
        'end_time': 0
    }
    return candle_properties
