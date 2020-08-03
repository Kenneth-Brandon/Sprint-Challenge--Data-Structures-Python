class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    class __Full:
        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur + 1) % self.capacity

        def get(self):
            return self.data[:self.cur] + self.data[self.cur:]

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data
