import src.tools as tools


class TestFindPriceRanges:
    """Tests for find_price_ranges function"""
    candlestick_data_default = {
        'length': 5,
        'ticks': [1566183600000, 1566187200000, 1566190800000, 1566194400000, 1566198000000],
        'open': [10401.5, 10404.0, 10376.0, 10363.5, 10471.5],
        'low': [10352.0, 10367.5, 10347.0, 10357.0, 10468.5],
        'high': [10415.0, 10415.0, 10392.5, 10486.0, 10745.0],
        'close': [10406.0, 10376.0, 10363.5, 10470.5, 10731.0]
    }
    period_size_default = 3
    expected_ranges = [0.0012978897274431578, 0.0027949113338473497, 0.005239628899677884, 0.005478662053056471,
                       0.007881584006151465, 0.03556283731688503]

    def test_valid(self):
        """Passing test. Expected: real ranges == expected ranges"""
        assert self.expected_ranges == tools.find_price_ranges(self.candlestick_data_default, self.period_size_default)


class TestFindOrderLevels:
    """Tests for find_order_levels function"""
    price_ranges_default = [0.001, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.06, 0.08, 0.09]
    probabilities_default = [0.00001, 0.101, 0.2, 0.999, 0.44]
    expected_price_levels = [0, 0.0899, 0.08, 0.00109, 0.056]

    def test_valid(self):
        """Passing test. Expected: real price levels == expected levels"""
        real_price_levels = [round(level, 5) for level in
                             tools.find_order_levels(self.price_ranges_default, self.probabilities_default)]
        assert self.expected_price_levels == real_price_levels

