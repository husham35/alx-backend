#!/usr/bin/env python3
"""
class LRUCache that inherits from BaseCaching and is a caching system:
This caching system doesn’t have limit with these methods below
- def put(self, key, item)
- def get(self, key)
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns to the dictionary `self.cache_data` the `item`
        value for the key `key`.
        If key or item is None, this method should not do anything
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in `self.cache_data` linked to `key`
        If `key` is `None` or if key doesn't exist in `self.cache_data`,
        return `None`
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
