import pytest
import time
import src.exchange_api.deribit as deribit
import src.validator as validator


class TestFetchCandlestickPriceData:
    """Tests for fetch_candlestick_price_data function"""
    ticker_default = 'BTC-PERPETUAL'
    candle_properties_default = {
        'resolution': 15,
        'amount': 100,
        'start_time': (int(time.time()) - 99 * 15 * 60) * 1000,
        'end_time': (int(time.time())) * 1000
    }

    def test_valid(self):
        """Passing test. Expected: successful request with not empty response"""
        price_data = deribit.fetch_candlestick_price_data(self.ticker_default, self.candle_properties_default)
        assert type(price_data) is dict and price_data['length'] == self.candle_properties_default['amount']

    def test_invalid_ticker(self):
        """Invalid ticker. Expected: request failed with RuntimeError"""
        ticker = 'INVALID-TICKER'
        with pytest.raises(RuntimeError):
            deribit.fetch_candlestick_price_data(ticker, self.candle_properties_default)

    def test_invalid_candle_resolution(self):
        """Invalid candle resolution. Expected: request failed with RuntimeError"""
        candle_properties = self.candle_properties_default.copy()
        candle_properties['resolution'] = 9
        with pytest.raises(RuntimeError):
            deribit.fetch_candlestick_price_data(self.ticker_default, candle_properties)

    def test_invalid_candle_time(self):
        """Invalid candle start or/and end time. Expected: empty response"""
        candle_properties = self.candle_properties_default.copy()
        candle_properties['start_time'] = 1500
        candle_properties['end_time'] = 1000
        price_data = deribit.fetch_candlestick_price_data(self.ticker_default, candle_properties)
        assert type(price_data) is dict and price_data['length'] == 0

    def test_invalid_candles_amount(self):
        """Invalid candles amount. Expected: successful request with not empty response"""
        candle_properties = self.candle_properties_default.copy()
        candle_properties['amount'] = -1
        expected_candles_amount = 100
        price_data = deribit.fetch_candlestick_price_data(self.ticker_default, candle_properties)
        assert type(price_data) is dict and price_data['length'] == expected_candles_amount

    def test_response_validation(self):
        """Response validation test. Expected: validation passing"""
        price_data = deribit.fetch_candlestick_price_data(self.ticker_default, self.candle_properties_default)
        assert validator.validate_candlestick_price_data(price_data)
