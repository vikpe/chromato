def assert_all(func: callable, values: list, expected_result) -> None:
    for v in values:
        assert (
            func(v) is expected_result
        ), f"assert {func.__name__}({v}) is {str(expected_result)}"


def assert_all_true(func: callable, values: list) -> None:
    assert_all(func, values, True)


def assert_all_false(func: callable, values: list) -> None:
    for v in values:
        assert func(v) is False
