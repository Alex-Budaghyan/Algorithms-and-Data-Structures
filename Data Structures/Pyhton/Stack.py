from Dynamic_array import DynamicArray


class Stack:
    def __init__(self):

        self.array = DynamicArray()

    def push(self, val):
        self.array.push_back(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop element. Stack is empty.")
        else:
            self.array.pop_back()

    def top(self):
        return self.array.array[self.array.size - 1]

    def is_empty(self):
        return not self.array.array

    def __getitem__(self, item):
        raise TypeError("Stack object is not subscriptable")

    def __str__(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            res = ''
            for i in range(self.array.size - 1, 0, -1):
                res += str(self.array.array[i]) + ', '
            res += str(self.array.array[0])
        return f'Stack: [{res}]'


if __name__ == '__main__':
    try:
        s = Stack()
        s.push(5)
        s.push(6)
        s.push(7)
        s.push(8)
        s.push(9)
        s.pop()
        print(s.top())
        print(s)
        # print(s[1])
    except TypeError as te:
        print(str(te))
    except IndexError as ie:
        print(str(ie))