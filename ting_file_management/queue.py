class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        # if 0 > index or index > self._data[-1]:
        if int(index) > (len(self._data) - 1) or int(index) < 0:
            raise IndexError
        else:
            return self._data[index]
