import pytest

from forex_types import FracPips, Pair, Price, BasePrice


class TestFracPips:
    @pytest.mark.parametrize(
        "frac_pips,pair,price",
        (
            (FracPips(112345), Pair.AUD_USD, Price("1.12345")),
            (FracPips(100123), Pair.USD_JPY, Price("100.123")),
        ),
    )
    def test_frac_pips(self, frac_pips: FracPips, pair: Pair, price: Price):
        p1 = frac_pips.to_ratio_price(pair.quote.rounder)
        p2 = frac_pips.to_quote_price(pair.quote)
        p3 = frac_pips.to_pair_price(pair)
        fp = FracPips.from_price(price)
        assert isinstance(p1, BasePrice)
        assert isinstance(p2, BasePrice)
        assert isinstance(p3, BasePrice)
        assert isinstance(fp, FracPips)
        assert price == p1 == p2 == p3
        assert frac_pips == fp
