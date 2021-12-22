#!/usr/bin/env python3
"""
caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCachey class
    """

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
