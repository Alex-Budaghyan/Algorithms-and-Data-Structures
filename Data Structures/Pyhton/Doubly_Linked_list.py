class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLList:
    def __init__(self):
        self.m_head = None
        self.m_tail = None

    def push_back(self, data):
        new_node = Node(data)
        if self.m_head is None:
            self.m_head = new_node
            self.m_tail = new_node
        else:
            self.m_tail.next = new_node
            new_node.prev = self.m_tail
            self.m_tail = new_node

    def push_front(self, data):
        new_node = Node(data)
        if self.m_head is None:
            self.m_head = new_node
            self.m_tail = new_node
        else:
            new_node.next = self.m_head
            new_node.next.prev = new_node
            self.m_head = new_node

    def pop_back(self):
        if self.m_head is None:
            raise IndexError("pop from empty doubly linked list")
        if self.m_head == self.m_tail:
            self.m_head = self.m_tail = None
        else:
            self.m_tail = self.m_tail.prev
            self.m_tail.next = None

    def pop_front(self):
        if self.m_head is None:
            raise IndexError("pop from empty doubly linked list")
        if self.m_head == self.m_tail:
            self.m_head = self.m_tail = None
        else:
            self.m_head = self.m_head.next
            self.m_head.prev = None

    def insert(self, val, index):
        if 0 > index or index > self.size():
            raise IndexError("List index out of range.")
        if isinstance(val, DLList):
            if index == 0:
                val.m_tail.next = self.m_head
                self.m_head.prev = val.m_tail
                val.m_head.prev = None
                self.m_head = val.m_head
            elif index == self.size():
                self.m_tail.next = val.m_head
                val.m_head.prev = self.m_tail
                self.m_tail = val.m_tail
            else:
                i = 0
                current = self.m_head
                while current.next is not None and i != index - 1:
                    i += 1
                    current = current.next
                val.m_tail.next = current.next
                if current.next is not None:
                    current.next.prev = val.m_tail
                current.next = val.m_head
                val.m_head.prev = current
        else:
            if index == self.size():
                self.push_back(val)
            elif index == 0:
                self.push_front(val)
            else:
                new_node = Node(val)
                if index > self.size():
                    current = self.m_tail
                    i = self.size()
                    while current.prev is not None and i != index:
                        i -= 1
                        current = current.prev
                else:
                    i = 0
                    current = self.m_head
                    while current.next is not None and i != index - 1:
                        i += 1
                        current = current.next
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                new_node.prev = current

    def delete(self, index):
        if 0 > index or index >= self.size():
            raise IndexError("List index out of range")
        if index == 0:
            self.pop_front()
        elif index == self.size() - 1:
            self.pop_back()
        else:
            if index >= self.size() // 2:
                current = self.m_tail
                i = self.size() - 1
                while current.prev is not None and i != index:
                    i -= 1
                    current = current.prev
            else:
                current = self.m_head
                i = 0
                while current.next is not None and i != index:
                    i += 1
                    current = current.next
            current.next.prev = current.prev
            current.prev.next = current.next

    def search(self, value):
        index = 0
        current = self.m_head
        while current is not None:
            if current.data == value:
                return index
            index += 1
            current = current.next
        return -1

    def reverse(self):
        if self.m_head is None or self.m_head == self.m_tail:
            return
        left = self.m_head
        right = self.m_tail
        while left != right and left.prev != right.next:
            left.next, left.prev = left.prev, left.next
            right.next, right.prev = right.prev, right.next
            left = left.prev
            right = right.next
        self.m_head, self.m_tail = self.m_tail, self.m_head

    def size(self):
        curr = self.m_head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def __str__(self):
        current = self.m_head
        s = ''
        while current is not None:
            s += str(current.data)
            current = current.next
            if current is not None:
                s += '<=>'
        return f"DLL: {s}: Size: {self.size()}"


if __name__ == '__main__':
    dllst = DLList()
    # dllst.push_back(5)
    # dllst.push_back(7)
    # dllst.push_back(9)
    dllst.push_front(1)
    dllst.push_front(2)
    dllst.push_front(3)
    dllst.push_back(4)
    dllst.push_front(5)
    dllst.push_back(6)
    dllst.pop_back()
    dllst.pop_front()
    dllst.insert(5, 4)
    dllst1 = DLList()
    dllst1.push_back(6)
    dllst1.push_front(10)
    dllst1.insert(12, 1)
    print(dllst1)
    print(dllst)
    dllst.insert(dllst1, 4)
    print(dllst)
    dllst.delete(4)
    print(dllst.m_head.data, dllst.m_tail.data, sep=' ')
    print(dllst)
    print(dllst.search(5))
    dllst.reverse()
