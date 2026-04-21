import pytest


@pytest.mark.smoke
def test_mark_1():
    assert True

@pytest.mark.regress
def test_mark_2():
    assert 1 == 1

@pytest.mark.regress
def test_mark_3():
    assert "hello" == "hello"

@pytest.mark.regress
def test_mark_4():
    assert [] == []