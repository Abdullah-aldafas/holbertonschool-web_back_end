#!/usr/bin/env python3
"""function named index_range that takes two integer arguments page and page_size """

def index_range(page ,page_size):
    start = (page - 1) * page_size
    end = page * page_size
    return (start,end)
