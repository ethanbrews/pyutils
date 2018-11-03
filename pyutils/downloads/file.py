from typing import Any, Callable, NamedTuple


class Download(NamedTuple):
    url: str
    location: str
    method: str = 'GET'
    data: Any = None
    # url, location
    on_start: Callable[[str, str], None] = lambda s1, s2: None
    # url, location, size
    on_complete: Callable[[str, str, int], None] = lambda s1, s2, i1: None
    # url, location, exception
    on_fail: Callable[[str, str, Exception], None] = lambda s1, s2, e1: None
    verify_response_code: Callable[[int], bool] = lambda r: 200 <= r < 300

