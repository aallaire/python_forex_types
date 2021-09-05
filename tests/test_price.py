from decimal import Decimal
from forex_types import Price, FracPips
from forex_types.price import BasePrice, NinjaPrice
import pytest


class TestPrice:
    @pytest.mark.parametrize(
        "value,subclass,pips,frac_pips",
        (
            ("1.223", Price, Decimal(12230), 122300),
            ("100.223", NinjaPrice, Decimal("10022.3"), 100223),
            ("100000", ValueError, None, None),
        ),
    )
    def test_price(self, value, subclass, pips, frac_pips):
        if subclass is ValueError:
            with pytest.raises(ValueError):
                Price(value)
        else:
            price = Price(value)
            assert price.pips == pips
            assert FracPips.from_price(price) == frac_pips
            assert isinstance(price, BasePrice)
            assert isinstance(price, subclass)

    @pytest.mark.parametrize(
        "v1,v2",
        [
            (Price("123.22"), Price("123.22")),
            (Price("1.2322"), Price("1.2322")),
            (Price("0.9938"), Price("0.9938")),
            (Price("99.382"), Price("99.382")),
        ],
    )
    def test_equal_prices(self, v1, v2):
        assert v1 == v2
        assert v1 <= v2
        assert v1 >= v2
        assert v2 == v1
        assert v2 <= v1
        assert v2 >= v1
        assert not (v1 != v2)
        assert not (v1 < v2)
        assert not (v1 > v2)
        assert not (v2 != v1)
        assert not (v2 < v1)
        assert not (v2 > v1)

    @pytest.mark.parametrize(
        "low,high",
        [
            (Price("123.12"), Price("123.22")),
            (Price("1.2322"), Price("1.23222")),
            (Price("0.9838"), Price("0.9938")),
            (Price("98.382"), Price("99.382")),
        ],
    )
    def test_unequal_prices(self, low, high):
        assert low < high
        assert low <= high
        assert low != high
        assert high > low
        assert high >= low
        assert high != low
        assert not (low == high)
        assert not (low > high)
        assert not (low >= high)
        assert not (high == low)
        assert not (high < low)
        assert not (high <= low)
