from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            value = self.array[key]
            # Remove first
            del self.array[key]
            # Add back in
            self.array[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            # Delete existing key before refreshing it
            del self.array[key]
        elif len(self.array) >= self.capacity:
            # Delete oldest
            k, v = self.array.iteritems().next()#This is python 2 item, for python 3 import six, six.iteritems(self.array)
            del self.array[k]
        self.array[key] = value