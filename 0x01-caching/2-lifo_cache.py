#!/usr/bin/env python3
""" caching system
    """

BasicCachey = __import__("base_caching").BaseCaching


class LIFOCache(BasicCachey):
    """ caching system:

    Args:
        LIFOCache ([class]): [basic caching]
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        temp_list = [x for x in self.cache_data.keys()]
        self.cache_data[key] = item
        temp_list.append(key)
        if len(temp_list) > self.MAX_ITEMS:
            if temp_list.count(key) > 1:
                pop = key
            else:
                pop = temp_list[-2]
            self.cache_data.pop(pop)
            print(f"DISCARD: {pop}")

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
