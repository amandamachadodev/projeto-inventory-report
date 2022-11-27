from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.number = 0

    def __next__(self):
        try:
            itera = self.data[self.number]
        except IndexError:
            raise StopIteration()
        self.number += 1
        return itera
