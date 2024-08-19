#!/usr/bin/env python3
"""
The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a
list for those particular pagination parameters.
"""
from typings import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Page numbers are `1-indexed`, the first page is page 1
    Returns a pagination of data
    """
    # start = (page - 1) * page_size
    # end = start + page_size
    # return (start, end)
    start = page * page_size
    return start - page_size, start
