class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLList:
    def __init__(self):
        self.m_head = None

    def push_back(self, data):
        node = Node(data)

        if self.m_head is None:
            self.m_head = node
        else:
            current = self.m_head
            while current.next is not None:
                current = current.next
            current.next = node

    def push_front(self, data):
        node = Node(data)
        node.next = self.m_head
        self.m_head = node

    def pop_back(self):
        if self.m_head is None:
            raise IndexError("pop from empty linked list")
        if self.m_head.next is None:
            self.m_head = None
        else:
            current = self.m_head
            while current.next.next is not None:
                current = current.next
            current.next = None

    def pop_front(self):
        if self.m_head is None:
            raise IndexError("pop from empty linked list")
        else:
            self.m_head = self.m_head.next

    def search(self, val):
        current = self.m_head
        while current.next is not None:
            if current.data == val:
                return True
            current = current.next
        return False

    def insert(self, val, index):
        current = self.m_head
        i = 0
        if 0 > index or index > self.size():
            raise IndexError("List index out of range.")
        if isinstance(val, SLList):
            curr1 = val.m_head
            if index == 0:
                while curr1.next is not None:
                    curr1 = curr1.next
                curr1.next = self.m_head
                self.m_head = val.m_head
            else:
                i = 0
                while current.next and i != index - 1:
                    current = current.next
                    i += 1
                while curr1.next is not None:
                    curr1 = curr1.next
                curr1.next = current.next
                current.next = val.m_head
        else:
            if index == 0:
                self.push_front(val)
            else:
                while current.next is not None and i != index - 1:
                    current = current.next
                    i += 1
                node = Node(val)
                node.next = current.next
                current.next = node

    def delete(self, index):
        current = self.m_head
        i = 0
        if 0 > index or index >= self.size():
            raise IndexError("List index out of range.")
        if index == 0:
            self.pop_front()
        else:
            while current.next is not None and i < index - 1:
                current = current.next
                i += 1
            current.next = current.next.next

    def size(self):
        index = 0
        current = self.m_head
        while current is not None:
            index += 1
            current = current.next
        return index

    def get_middle(self):
        if self.m_head is None:
            raise ValueError("Linked list is empty")
        else:
            p, q = self.m_head, self.m_head
            while q is not None and q.next is not None:
                q = q.next.next
                if q is None:
                    break
                p = p.next
            return p

    def has_cycle(self):
        if self.m_head is None:
            raise Exception("Linked lis is empty")
        p = self.m_head
        q = self.m_head
        b = False
        while q is not None and q.next is not None:
            q = q.next.next
            p = p.next
            if p == q:
                b = True
                break
        if b:
            curr = self.m_head
            while p != curr:
                curr = curr.next
                p = p.next
            return p
        else:
            return False

    def reverse(self):
        if self.m_head is None:
            raise Exception("Linked list is empty")
        prev = None
        current = self.m_head
        while current is not None:
            n = current.next
            current.next = prev
            prev = current
            current = n
        self.m_head = prev

    # def reverseR(self):
    #     if self.m_head is None or self.m_head.next is None:
    #         return self.m_head
        # tmp = reverseR(s)

    def merge(self, other):
        merge_sll = SLList()
        curr1 = self.m_head
        curr2 = other.m_head
        while curr1 is not None and curr2 is not None:
            if curr1.data < curr2.data:
                merge_sll.push_back(curr1.data)
                curr1 = curr1.next
            else:
                merge_sll.push_back(curr2.data)
                curr2 = curr2.next

        while curr1 is not None:
            merge_sll.push_back(curr1.data)
            curr1 = curr1.next

        while curr2 is not None:
            merge_sll.push_back(curr2.data)
            curr2 = curr2.next

        return merge_sll

    def __str__(self):
        current = self.m_head
        s = ''
        while current is not None:
            s += str(current.data)
            current = current.next
            if current is not None:
                s += '->'
        return f"SLL: {s}: Size: {self.size()}"


if __name__ == "__main__":
    llst = SLList()
    llst.push_back(2)
    llst.push_back(3)
    llst.push_back(4)
    llst.push_front(1)
    llst.push_back(7)
    llst.push_back(9)
    llst.delete(4)
    llst.pop_back()
    llst.push_back(8)
    llst.push_back(9)
    new_llst = SLList()
    new_llst.push_back(10)
    new_llst.push_back('Alex')
    # llst1 = SLList()
    # llst1.push_back(5)
    # llst1.push_back(6)
    # llst1.push_back(7)
    # cycle = llst.m_head
    # end = llst.m_head
    # print(llst)
    # for i in range(4):
    #     cycle = cycle.next
    # print(cycle.data)
    # for i in range(llst.size() - 1):
    #     end = end.next
    # print(llst.merge(llst1))
    # end.next = llst.m_head
    print(llst)
    llst.insert(new_llst, 5)
    print(llst)
    # print(llst.reverse())
