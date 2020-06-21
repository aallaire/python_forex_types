from forex_types import Pair, Currency
import pytest


ORDERED_PAIRS = (
    Pair.EUR_GBP,
    Pair.EUR_AUD,
    Pair.GBP_AUD,
    Pair.EUR_NZD,
    Pair.GBP_NZD,
    Pair.AUD_NZD,
    Pair.EUR_USD,
    Pair.GBP_USD,
    Pair.AUD_USD,
    Pair.NZD_USD,
    Pair.EUR_CAD,
    Pair.GBP_CAD,
    Pair.AUD_CAD,
    Pair.NZD_CAD,
    Pair.USD_CAD,
    Pair.EUR_CHF,
    Pair.GBP_CHF,
    Pair.AUD_CHF,
    Pair.NZD_CHF,
    Pair.USD_CHF,
    Pair.CAD_CHF,
    Pair.EUR_JPY,
    Pair.GBP_JPY,
    Pair.AUD_JPY,
    Pair.NZD_JPY,
    Pair.USD_JPY,
    Pair.CAD_JPY,
    Pair.CHF_JPY,
)


class TestPair:
    @pytest.mark.parametrize("pair", ORDERED_PAIRS)
    def test_basics(self, pair):
        assert isinstance(pair, Pair)
        assert isinstance(pair.base, Currency)
        assert isinstance(pair.quote, Currency)
        assert isinstance(pair.name, str)
        pair2 = Pair(f"{pair.base}-{pair.quote}")
        pair3 = Pair(f"{pair.base}/{pair.quote}")
        pair4 = Pair(f"{pair.base}{pair.quote}")
        pair5 = Pair(pair.name)
        pair6 = Pair(str(pair))
        pair7 = Pair.from_currency(pair.base, pair.quote)
        assert pair == pair2 == pair3 == pair4 == pair5 == pair6 == pair7

    def test_iter(self):
        pair_set = set([_ for _ in Pair.iter_pairs()])
        assert len(pair_set) == 28
        for pair in ORDERED_PAIRS:
            assert pair in pair_set

    def test_cmp(self):
        pair_list = [_ for _ in Pair.iter_pairs()]
        pair_list.sort()
        assert tuple(pair_list) == ORDERED_PAIRS

    @pytest.mark.parametrize(
        "class_attr,name",
        (
            (Pair.EUR_GBP, "EUR_GBP"),
            (Pair.EUR_AUD, "EUR_AUD"),
            (Pair.GBP_AUD, "GBP_AUD"),
            (Pair.EUR_NZD, "EUR_NZD"),
            (Pair.GBP_NZD, "GBP_NZD"),
            (Pair.AUD_NZD, "AUD_NZD"),
            (Pair.EUR_USD, "EUR_USD"),
            (Pair.GBP_USD, "GBP_USD"),
            (Pair.AUD_USD, "AUD_USD"),
            (Pair.NZD_USD, "NZD_USD"),
            (Pair.EUR_CAD, "EUR_CAD"),
            (Pair.GBP_CAD, "GBP_CAD"),
            (Pair.AUD_CAD, "AUD_CAD"),
            (Pair.NZD_CAD, "NZD_CAD"),
            (Pair.USD_CAD, "USD_CAD"),
            (Pair.EUR_CHF, "EUR_CHF"),
            (Pair.GBP_CHF, "GBP_CHF"),
            (Pair.AUD_CHF, "AUD_CHF"),
            (Pair.NZD_CHF, "NZD_CHF"),
            (Pair.USD_CHF, "USD_CHF"),
            (Pair.CAD_CHF, "CAD_CHF"),
            (Pair.EUR_JPY, "EUR_JPY"),
            (Pair.GBP_JPY, "GBP_JPY"),
            (Pair.AUD_JPY, "AUD_JPY"),
            (Pair.NZD_JPY, "NZD_JPY"),
            (Pair.USD_JPY, "USD_JPY"),
            (Pair.CAD_JPY, "CAD_JPY"),
            (Pair.CHF_JPY, "CHF_JPY"),
        ),
    )
    def test_class_attr_match(self, class_attr: Pair, name: str):
        assert class_attr == Pair(name)
