class DynamicArray:
    def __init__(self):
        self.array = []
        self.size = 0
        self.capacity = 0

    def push_back(self, val):
        if self.size == 0 or self.size == self.capacity:
            self.shrink()
        self.array[self.size] = val
        self.size += 1

    def push_front(self, val):
        if self.size == 0 or self.size == self.capacity:
            self.shrink()
        for i in range(self.size, 0, -1):
            self.array[i] = self.array[i - 1]
        self.array[0] = val
        self.size += 1

    def insert(self, index, val):
        if index < 0:
            raise IndexError("Index out of range")

        if self.size == self.capacity:
            self.shrink()
        if index == 0:
            self.push_front(val)
        elif index >= self.size:
            self.push_back(val)
        else:
            for i in range(self.size, index - 1, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = val
            self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Cannot pop from an empty array")
        self.size -= 1
        if self.size < self.capacity // 2:
            self.capacity //= 2

    def pop_front(self):
        if self.size == 0:
            raise IndexError("Cannot pop from an empty array")
        for i in range(self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        if self.size < self.capacity // 2:
            self.capacity //= 2

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('List index out of range')
        if index == 0:
            self.pop_front()
        elif index == self.size - 1:
            self.pop_back()
        else:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i+1]
            self.size -= 1
        if self.size < self.capacity // 2:
            self.capacity //= 2

    def search(self, val):
        for i in range(self.size):
            if self.array[i] == val:
                return True
        return False

    def shrink(self):
        if self.capacity == 0:
            self.capacity = 1
            self.array = [None]
        else:
            new_array = [None] * self.capacity
            self.array = self.array + new_array
            self.capacity *= 2

    def resize(self, size, val):
        if size == self.size:
            return
        elif size <= 0:
            self.capacity = 1
            self.size = 0
            return
        elif size < self.size:
            self.size = size
            if self.size < self.capacity // 2:
                self.capacity //= 2
        else:
            if size > self.capacity:
                self.capacity = size * 2
            for i in range(self.size, size):
                self.array[i] = val
            self.size = size

    def __str__(self):
        if self.size == 0:
            return f'Empty List size: {self.size}, capacity: {self.capacity}'
        res = ''
        for i in range(self.size - 1):
            res += str(self.array[i]) + ', '
        res += str(self.array[self.size - 1])
        return f'[{res}] size: {self.size}, capacity: {self.capacity}'


if __name__ == '__main__':
    try:
        da = DynamicArray()
        da.push_back(1)
        da.push_back(2)
        da.push_front(3)
        da.push_front(10)
        da.push_back(6)
        da.push_back(7)
        print(da)
        da.insert(3, 8)
        print(da)
        da.insert(0, 0)
        print(da)
        da.insert(10, 9)
        print(da)
        da.insert(5, 16)
        print(da)
        da.pop_front()
        print(da)
        da.pop_back()
        print(da)
        da.pop_back()
        print(da)
        da.delete(1)
        print(da)
        da.delete(0)
        print(da)
        print(da.search(1))
        print(da.search(102))
        da.delete(2)
        da.delete(0)
        print(da)
        da.resize(6, 5)
        print(da)
    except IndexError as ie:
        print(str(ie))
