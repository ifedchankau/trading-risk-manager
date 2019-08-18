import pytest
import time
import src.exchange_api.deribit as deribit
import src.validator as validator


class TestFetchCandlestickPriceData:
    """Tests for fetch_candlestick_price_data function"""

    def test_valid(self):
        """Passing test. Expected: successful request with not empty response"""
        ticker = 'BTC-PERPETUAL'
        candle_properties = {
            'resolution': 15,
            'amount': 100,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }
        price_data = deribit.fetch_candlestick_price_data(ticker, candle_properties)
        assert type(price_data) is dict and len(price_data['ticks']) == candle_properties['amount']

    def test_invalid_ticker(self):
        """Invalid ticker. Expected: request failed with RuntimeError"""
        ticker = 'INVALID-TICKER'
        candle_properties = {
            'resolution': 15,
            'amount': 100,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }
        with pytest.raises(RuntimeError):
            deribit.fetch_candlestick_price_data(ticker, candle_properties)

    def test_invalid_candle_resolution(self):
        """Invalid candle resolution. Expected: request failed with RuntimeError"""
        ticker = 'BTC-PERPETUAL'
        candle_properties = {
            'resolution': 9,
            'amount': 100,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }
        with pytest.raises(RuntimeError):
            deribit.fetch_candlestick_price_data(ticker, candle_properties)

    def test_invalid_candle_time(self):
        """Invalid candle start or/and end time. Expected: empty response"""
        ticker = 'BTC-PERPETUAL'
        candle_properties = {
            'resolution': 15,
            'amount': 100,
            'start_time': 1500,
            'end_time': 1000
        }
        price_data = deribit.fetch_candlestick_price_data(ticker, candle_properties)
        assert type(price_data) is dict and len(price_data['ticks']) == 0

    def test_invalid_candles_amount(self):
        """Invalid candles amount. Expected: successful request with not empty response"""
        ticker = 'BTC-PERPETUAL'
        candle_properties = {
            'resolution': 15,
            'amount': -1,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }
        expected_candles_amount = 100
        price_data = deribit.fetch_candlestick_price_data(ticker, candle_properties)
        assert type(price_data) is dict and len(price_data['ticks']) == expected_candles_amount

    def test_response_validation(self):
        """Response validation test. Expected: validation passing"""
        ticker = 'BTC-PERPETUAL'
        candle_properties = {
            'resolution': 15,
            'amount': 100,
            'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
            'end_time': (int(time.time())) * 1000
        }
        price_data = deribit.fetch_candlestick_price_data(ticker, candle_properties)
        assert validator.validate_candlestick_price_data(price_data, candle_properties['amount'])
