import pytest


class TestClassTuple:
    def test_basic(self):
        assert tuple('hello, world!') == ('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')

    @pytest.mark.parametrize(
        "term1, term2, expected",
        [((1, 2, 3), (4, 5), (1, 2, 3, 4, 5)),
         ((3, "abc"), (-7.22, ['a', 5]), (3, 'abc', -7.22, ['a', 5]))])
    def test_sum(self, term1, term2, expected):
        assert term1 + term2 == expected

    def test_as_func(self):
        tuple1 = ('a', 'b', 'c')
        try:
            tuple1(1)
        except TypeError:
            pass


class TestClassInt:
    def test_basic(self):
        assert 2 + 2 == 4

    @pytest.mark.parametrize(
        "mult1, mult2, expected",
        [(3, 4, 12),
         (5, -7, -35),
         (1001, 0, 0)])
    def test_multiplication(self, mult1, mult2, expected):
        assert mult1 * mult2 == expected

    def test_sum_with_string(self):
        try:
            2 + '2'
        except TypeError:
            pass
