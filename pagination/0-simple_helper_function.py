#!/usr/bin/env python3
""" Range simple helper fun """

def index_range(page: int ,page_size: int) -> tuple[int, int]:
    """Return a tuple containing the start and end indexes for pagination based on the given page and page_size."""

    start = (page - 1) * page_size
    end = page * page_size
    return (start,end)
