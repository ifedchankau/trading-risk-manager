def find_price_ranges(candlestick_data, period_size):
    """Calculates historical price ranges for a given period duration.

    For one period of bars ranges counts as:
    1st range: (high price in period - first bar opening price) / first bar opening price - 1
    2nd range: (first bar opening price - low price in period) / first bar opening price - 1
    The next period is obtained by a shift of always 1 bar.

    :param (dict of str: list) candlestick_data: candlestick market price data (required)
    :param int period_size: size of one period in bars (required)
    :return (list of float) price_ranges: all price ranges in market price data
    """

    price_ranges = []
    for candle_index in range(candlestick_data['length'] - period_size + 1):
        period_open = candlestick_data['open'][candle_index]
        max_high = max(candlestick_data['high'][candle_index: candle_index + period_size])
        min_low = min(candlestick_data['low'][candle_index: candle_index + period_size])
        price_ranges.append(max_high / period_open - 1)
        price_ranges.append(1 - min_low / period_open)
    print(sorted(price_ranges))
    return sorted(price_ranges)


def find_order_relative_levels(price_ranges, order_probabilities):
    """Calculates orders relative levels with given filling probability depending on historical market volatility

    :param (list of float) price_ranges: historical price ranges (required)
    :param (list of float) order_probabilities: order filling probabilities (required)
    :return (list of float) order_levels: relative levels of orders
    """

    probability_step = 1 / len(price_ranges)
    order_levels = []
    for fill_probability in order_probabilities:
        if fill_probability < probability_step:
            order_levels.append(0)
            continue
        range_index = len(price_ranges) - fill_probability / probability_step
        range_index_int_part = int(range_index)
        range_index_double_part = range_index - range_index_int_part
        level = price_ranges[range_index_int_part] + (price_ranges[range_index_int_part + 1] -
                                                      price_ranges[range_index_int_part]) * range_index_double_part
        order_levels.append(level)
    return order_levels


def find_order_price_levels(base_price, relative_levels, direction):
    """Calculates order price levels by base price and relative order levels

    :param float base_price: base price for order price level calculating (f.e. current market price)
    :param (list of float) relative_levels: relative order levels
    :param str direction: `higher` for orders above base_price or `lower` for orders below base_price
    :return (list of float) price_levels: price levels of orders
    """

    direction_int = 1 if direction == 'higher' else -1
    price_levels = []
    for level in relative_levels:
        price_levels.append(base_price * (1 + level * direction_int))
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


def get_range_period_size(hold_time):
    """
    Todo: realize function (issue #11)
    """

    period_size = 0
    return period_size
