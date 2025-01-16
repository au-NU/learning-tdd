from main import is_even


def test_is_even_true_positive_small():
    assert is_even(8) == True


def test_is_even_true_positive_large():
    assert is_even(9042) == True


def test_is_even_false_positive_small():
    assert is_even(3) == False


def test_is_even_false_positive_large():
    assert is_even(9245) == False


def test_is_even_true_negative_small():
    assert is_even(-6) == True


def test_is_even_true_negative_large():
    assert is_even(-1003456) == True


def test_is_even_false_negative_small():
    assert is_even(-9) == False


def test_is_even_false_negative_large():
    assert is_even(-82409) == False
