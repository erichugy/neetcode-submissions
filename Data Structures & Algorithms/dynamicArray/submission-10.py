class DynamicArray:
    
    def __init__(self, capacity: int):
        self.list = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.list[i]

    def set(self, i: int, n: int) -> None:
        self.list[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.list[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size > 0:
            tmp = self.list[self.size-1]
            self.size -= 1
            return tmp

    def resize(self) -> None:
        tmpList = [None] * self.capacity
        self.list.extend(tmpList)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity