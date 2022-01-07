import pytest


def test_succeed():
    assert True


@pytest.mark.xfail(strict=False)
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
