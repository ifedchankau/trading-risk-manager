import pytest
import time
import src.validator as validator


class TestValidateCandlestickPriceData:
    """Tests for validate_candlestick_price_data function"""

    def test_valid(self):
        """Passing test. Expected: successful validation"""
        price_data = {
            'ticks': [1566086400000, 1566090000000, 1566093600000, 1566097200000, 1566100800000],
            'open': [40.11, 40.21, 40.31, 40.01, 40.41],
            'high': [40.16, 40.26, 40.36, 40.06, 40.46],
            'low': [40.06, 40.16, 40.26, 39.96, 40.366],
            'close': [40.10, 40.20, 40.31, 39.99, 40.41]
        }
        candles_amount = 5
        assert validator.validate_candlestick_price_data(price_data, candles_amount)

    def test_additional_key(self):
        """Additional optional key in data. Expected: successful validation"""
        price_data = {
            'ticks': [1566086400000, 1566090000000, 1566093600000, 1566097200000, 1566100800000],
            'volume': [10.21, 11.22, 9.23, 3.24, 20.25],
            'open': [40.11, 40.21, 40.31, 40.01, 40.41],
            'high': [40.16, 40.26, 40.36, 40.06, 40.46],
            'low': [40.06, 40.16, 40.26, 39.96, 40.366],
            'close': [40.10, 40.20, 40.31, 39.99, 40.41]
        }
        candles_amount = 5
        assert validator.validate_candlestick_price_data(price_data, candles_amount)

    def test_invalid_type(self):
        """Price data invalid type. Expected: validation failed with TypeError"""
        price_data = [
            [1566086400000, 1566090000000, 1566093600000, 1566097200000, 1566100800000],
            [40.11, 40.21, 40.31, 40.01, 40.41],
            [40.16, 40.26, 40.36, 40.06, 40.46],
            [40.06, 40.16, 40.26, 39.96, 40.366],
            [40.10, 40.20, 40.31, 39.99, 40.41]
        ]
        candles_amount = 5
        with pytest.raises(TypeError):
            validator.validate_candlestick_price_data(price_data, candles_amount)

    def test_missing_key(self):
        """One key is missing. Expected: validation failed with ValueError"""
        price_data = {
            'open': [40.11, 40.21, 40.31, 40.01, 40.41],
            'high': [40.16, 40.26, 40.36, 40.06, 40.46],
            'low': [40.06, 40.16, 40.26, 39.96, 40.366],
            'close': [40.10, 40.20, 40.31, 39.99, 40.41]
        }
        candles_amount = 5
        with pytest.raises(ValueError):
            validator.validate_candlestick_price_data(price_data, candles_amount)

    def test_empty_key(self):
        """One key is empty. Expected: validation failed with ValueError"""
        price_data = {
            'ticks': [],
            'open': [40.11, 40.21, 40.31, 40.01, 40.41],
            'high': [40.16, 40.26, 40.36, 40.06, 40.46],
            'low': [40.06, 40.16, 40.26, 39.96, 40.366],
            'close': [40.10, 40.20, 40.31, 39.99, 40.41]
        }
        candles_amount = 5
        with pytest.raises(ValueError):
            validator.validate_candlestick_price_data(price_data, candles_amount)

    def test_invalid_candles_amount(self):
        """One key has fewer or more candles than expected. Expected: validation failed with ValueError"""
        price_data = {
            'ticks': [1566086400000, 1566090000000, 1566093600000, 1566097200000, 1566100800000],
            'open': [40.11, 40.21, 40.31, 40.01, 40.41],
            'high': [40.16, 40.26, 40.36, 40.06, 40.46],
            'low': [40.06, 40.16, 40.26, 39.96, 40.366],
            'close': [40.10, 40.20, 40.31, 39.99, 40.41]
        }
        candles_amount = 4
        with pytest.raises(ValueError):
            validator.validate_candlestick_price_data(price_data, candles_amount)


class TestValidateExchangeName:
    """Tests for validate_exchange_name function"""

    def test_valid(self):
        """Passing test. Expected: successful validation"""
        exchange = 'deribit'
        assert validator.validate_exchange_name(exchange)

    def test_invalid_exchange(self):
        """Invalid exchange. Expected: validation failing"""
        exchange = 'invalid-exchange'
        with pytest.raises(ValueError):
            validator.validate_exchange_name(exchange)


class TestValidateInstrumentTicker:
    """Tests for validate_instrument_ticker function"""

    def test_valid(self):
        """Passing test. Expected: successful validation"""
        exchange = 'deribit'
        ticker = 'BTC-PERPETUAL'
        assert validator.validate_instrument_ticker(exchange, ticker)

    def test_invalid_exchange(self):
        """Invalid exchange. Expected: validation failing"""
        exchange = 'invalid-exchange'
        ticker = 'BTC'
        with pytest.raises(ValueError):
            validator.validate_instrument_ticker(exchange, ticker)

    def test_invalid_ticker(self):
        """Invalid ticker. Expected: validation failing"""
        exchange = 'deribit'
        ticker = 'INVLD-TCKR'
        with pytest.raises(ValueError):
            validator.validate_instrument_ticker(exchange, ticker)
