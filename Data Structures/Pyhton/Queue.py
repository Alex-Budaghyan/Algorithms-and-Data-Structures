from Dynamic_array import DynamicArray


class CircularQueue:
    def __init__(self, capacity):
        self.dynamic_array = DynamicArray()
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, val):
        if self.is_full():
            raise IndexError("Cannot enqueue to a full circular queue")

        self.rear = (self.rear + 1) % self.capacity
        self.dynamic_array.insert(self.rear, val)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty circular queue")

        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek into an empty circular queue")
        return self.dynamic_array.array[self.front]

    def size(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "Empty Circular Queue"
        res = ''
        index = self.front
        for _ in range(self.size - 1):
            res += str(self.dynamic_array.array[index]) + ', '
            index = (index + 1) % self.capacity
        res += str(self.dynamic_array.array[index])
        return f'Circular Queue: [{res}]'


if __name__ == "__main__":
    circular_queue = CircularQueue(5)
    circular_queue.enqueue(1)
    circular_queue.enqueue(2)
    circular_queue.enqueue(3)
    circular_queue.enqueue(4)
    circular_queue.enqueue(5)
    print(circular_queue)
    print("Peek:", circular_queue.peek())
    print(circular_queue)
    # circular_queue.enqueue(6)
    # circular_queue.enqueue(7)
    print(circular_queue)
