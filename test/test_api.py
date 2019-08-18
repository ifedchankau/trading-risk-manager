import pytest
import time
import src.api as api


class TestFetchCandlestickPriceData:
    """Tests for fetch_candlestick_price_data function"""

    def test_valid(self):
        """Passing test. Expected: successful request with not empty response"""
        exchange = 'deribit'
        ticker = 'BTC-PERPETUAL'
        candle_properties = {
            'resolution': 15,
            'amount': 100,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }
        price_data = api.fetch_candlestick_price_data(exchange, ticker, candle_properties)
        assert type(price_data) is dict and len(price_data['ticks']) == candle_properties['amount']

    def test_invalid_exchange(self):
        """Invalid ticker. Expected: request failed with RuntimeError"""
        exchange = 'invalid-exchange'
        ticker = 'BTC-PERPETUAL'
        candle_properties = {
            'resolution': 15,
            'amount': 100,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }
        with pytest.raises(ValueError):
            api.fetch_candlestick_price_data(exchange, ticker, candle_properties)
