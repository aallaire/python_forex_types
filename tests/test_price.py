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
