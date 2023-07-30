from funcpipe import Pipe, pattern_match
import pytest


def test_pipe() -> None:
    @Pipe
    def sum_one(x: int) -> int:
        return x + 1

    assert sum_one(1) == 2
    assert (sum_one >> sum_one >> sum_one)(1) == 4
    assert (sum_one.pipe(sum_one).pipe(sum_one))(1) == 4


def test_pattern_matching():

    def is_even(x: int) -> bool:
        return x % 2 == 0
    
    def is_odd(x: int) -> bool:
        return x % 2 == 1
    
    def is_zero(x: int) -> bool:
        return x == 0
    
    def is_positive(x: int) -> bool:

        return x > 0
    
    def double(x: int) -> int:
        return x * 2
    
    def triple(x: int) -> int:
        return x * 3
    
    def quadruple(x: int) -> int:
        return x * 4
    
    pattern = pattern_match(
        (
            (is_even, double),
            (is_odd, triple),
            (is_zero, lambda x: 0),
        ),
        default=lambda x: x,
    )

    assert pattern(1) == 3
    assert pattern(2) == 4
    assert pattern(0) == 0

def test_no_case_for_pattern_match():
    def is_even(x: int) -> bool:
        return x % 2 == 0
    
    def is_odd(x: int) -> bool:
        return x % 2 == 1
    
    def is_zero(x: int) -> bool:
        return x == 0
    
    def is_positive(x: int) -> bool:
        return x > 0
    
    def double(x: int) -> int:
        return x * 2
    
    def triple(x: int) -> int:
        return x * 3
    
    def quadruple(x: int) -> int:
        return x * 4
    
    pattern = pattern_match(
        (
            (is_even, double),
        ),
    )

    with pytest.raises(ValueError):
        pattern(1)

def test_pattern_matching_return_default():
    def is_even(x: int) -> bool:
        return x % 2 == 0
    
    def is_odd(x: int) -> bool:
        return x % 2 == 1
    
    def is_zero(x: int) -> bool:
        return x == 0
    
    def is_positive(x: int) -> bool:
        return x > 0
    
    def double(x: int) -> int:
        return x * 2
    
    def triple(x: int) -> int:
        return x * 3
    
    def quadruple(x: int) -> int:
        return x * 4
    
    pattern = pattern_match(
        (
            (is_even, double),
        ),
        default=lambda x: x,
    )

    assert pattern(1) == 1
    assert pattern(2) == 4
    assert pattern(0) == 0