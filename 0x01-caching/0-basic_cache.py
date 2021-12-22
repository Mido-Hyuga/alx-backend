#!/usr/bin/python3
""" caching system
    """

BasicCachey = __import__("base_caching").BaseCaching


class BasicCache(BasicCachey):
    """ caching system:

    Args:
        BasicCachey ([class]): [basic caching]
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)