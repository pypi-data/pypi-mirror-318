import finance_core as fc
import pytest


def test_init():

    with pytest.raises(ValueError, match="Period cannot be 0."):
        fc.MovingAverageConvergenceDivergence(0, 12)

    with pytest.raises(ValueError, match="Period cannot be 0."):
        fc.MovingAverageConvergenceDivergence(26, 0)


def test_next():

    macd = fc.MovingAverageConvergenceDivergence(26, 12)

    assert macd.next(3.0) == 0.0
    assert round(macd.next(4.0), 4) == 0.0798
    assert round(macd.next(5.0), 4) == 0.2211
    assert round(macd.next(6.0), 4) == 0.4091


def test_reset():

    macd = fc.MovingAverageConvergenceDivergence(26, 12)

    assert macd.next(3.0) == 0.0
    assert round(macd.next(4.0), 4) == 0.0798

    macd.reset()
    assert macd.next(3.0) == 0.0
    assert round(macd.next(4.0), 4) == 0.0798

    macd.reset()
    assert macd.next(3.0) == 0.0
    assert round(macd.next(4.0), 4) == 0.0798
