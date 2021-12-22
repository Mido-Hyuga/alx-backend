#!/usr/bin/env python3
""" caching system
    """

BasicCachey = __import__("base_caching").BaseCaching


class LRUCache(BasicCachey):
    """ caching system:
    Args:
        LRUCache ([class]): [basic caching]
    """

    def __init__(self) -> None:
        """ initialize of class """
        self.temp_list = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            self.temp_list.append(key)
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = self.temp_list[0]
                self.temp_list = list(
                    filter(
                        lambda x: x != self.temp_list[0],
                        self.temp_list))
                self.cache_data.remove(pop)
                print(f"DISCARD: {pop}")

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.temp_list.insert(-1,
                              self.temp_list.pop(self.temp_list.index(key)))
        return self.cache_data.get(key)
