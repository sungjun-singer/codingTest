"""
1. 우선 DoubleNode를 만들어야한다.
2. 그리고 head와 tail가지는 구조를 만들어야한다.
3. 그리고 다양한 메소드를 구현하면 된다.
"""
from fcntl import FASYNC


class DoubleNode():
    def __init__(self, _data):
        self.prev = None
        self.next = None
        self.data = _data

class Deque():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # 길이를 리턴하는 함수
    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return "Empty!"
        res = ""
        node = self.head
        while node.next is not None:
            res += str(node.data) + " ↔ "
            node = node.next
        return res + str(node.data)

    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node is not None:
            if node.data == target:
                return True
            node = node.next
        return False

    def append_left(self, data):
        if self.head is None:
            self.head = self.tail = DoubleNode(data)
        else:
            new_node = DoubleNode(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def popLeft(self):
        if self.head is None:
            return "Empty!!"
        if self.length == 1:
            return self.head.data

        pop_data = self.head
        next_node = self.head.next
        self.head.next = None
        next_node.prev = None
        self.head = next_node
        self.length -= 1
        return pop_data

    def pop(self):
        if self.head is None:
            return "Empty!!"
        pop_data = self.tail.data
        if self.length == 1:
            self.head = self.tail = None
        else:
            prev_node = self.tail.prev
            self.tail.prev = None
            prev_node.next = None
            self.tail = prev_node
        self.length -= 1
        return pop_data

    def insert(self, idx, data):
        if idx <= 0:
            self.appendLeft(data)
        elif idx >= self.length:
            self.append(data)
        else:
            new_node = DoubleNode(data)
            node = self.head
            for _ in range(idx -1):
                node = node.next
            node.next.prev = new_node
            new_node.next = node.next
            new_node.prev = node
            node.next = new_node
        self.length += 1

    def remove_idx(self, idx):
        if idx <= 0:
            self.popLeft()
        elif idx >= self.length:
            self.pop()
        else:
            node = self.head
            for _ in range(idx):
                node = node.next
            node.next.prev = node.prev
            node.prev.next = node.next
            node.prev = node.next = None
        self.length -= 1

    def remove(self, target):
        node = self.head
        while node.next is not None and node.data is not target:
            node = node.next
        if node is None:
            return False
        if self.length == 1:
            self.head = self.tail = None
            return node.data
        else:
            if node == self.head:
                self.head = node.next
                self.head.prev = None
            elif node == self.tail:
                self.tail = node.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.length -= 1
            return node.data

    def reverse(self):
        if self.length < 2:
            return
        else:
            self.tail = self.head
            ahead = self.head.next
            while ahead:
                self.head.next = self.head.prev
                self.head.prev = ahead
                self.head = ahead
                ahead = ahead.next
            self.head.next = self.head.prev
            self.head.prev = None

deq = Deque()

deq.append_left(2)
deq.append_left(3)
deq.append_left(4)
deq.append_left(5)
deq.append_left(6)
print(deq)
print(deq.reverse())
print(deq)



