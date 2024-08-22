#!/usr/bin/env python3
"""
class BasicCache that inherits from BaseCaching and is a caching system:
This caching system doesn’t have limit with these methods below
- def put(self, key, item)
- def get(self, key)
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Uses self.cache_data - dictionary from the parent class BaseCaching
    """
    def put(self, key, item):
        """
        - Assigns to the dictionary self.cache_data the item value for
         the key key.
        - If key or item is None, this method should not do anything.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        - Returns the value in self.cache_data linked to key.
        - If key is None or if the key doesn’t exist in self.cache_data,
         return None.
        """
        return self.cache_data.get(key, None)
