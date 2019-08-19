import pytest
import time
import src.api as api


class TestFetchCandlestickPriceData:
    """Tests for fetch_candlestick_price_data function"""
    exchange_default = 'deribit'
    ticker_default = 'BTC-PERPETUAL'
    candle_properties_default = {
            'resolution': 15,
            'amount': 100,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }

    def test_valid(self):
        """Passing test. Expected: successful request with not empty response"""
        price_data = api.fetch_candlestick_price_data(self.exchange_default, self.ticker_default,
                                                      self.candle_properties_default)
        assert type(price_data) is dict and price_data['length'] == self.candle_properties_default['amount']

    def test_invalid_exchange(self):
        """Invalid exchange. Expected: request failed with RuntimeError"""
        exchange = 'invalid-exchange'
        with pytest.raises(ValueError):
            api.fetch_candlestick_price_data(exchange, self.ticker_default, self.candle_properties_default)
