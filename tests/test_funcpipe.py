from funcpipe import Pipe


def test_pipe() -> None:
    @Pipe
    def sum_one(x: int) -> int:
        return x + 1

    assert sum_one(1) == 2
    assert (sum_one >> sum_one >> sum_one)(1) == 4
    assert (sum_one.pipe(sum_one).pipe(sum_one))(1) == 4
