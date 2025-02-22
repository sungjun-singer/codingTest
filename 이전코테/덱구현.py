# 앞 뒤를 가리키는 포인터를 가지는 노드 생성
# prev data next 구조
class DoubleNode():
    def __init__(self, data):
        self.data = data
        self.prev = None # 이전 노드를 가리키는 변수
        self.next = None # 다음 노드를 가리키는 변수

# 덱 구현
# head와 tail와 length를 지정한다.

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # 길이를 리턴하는 함수
    def __len__(self):
        return self.length

    # str 함수 head가 없다면 비어있다고 출력
    def __str__(self):
        if self.head is None:
            return "Empty!!"
        # head가 있을 때 노드를 next 포인터가 존재하지 않을 때까지 반복문을 돌며 출력한다.
        res = ""
        node = self.head
        while node.next is not None:
            res += str(node.data) + " ↔︎ "
            node = node.next
        # 마지막 노드에서는 반복하지 않기 때문에 추가해준다.
        return res + str(node.data)


    def __contains__(self, target):
        # head가 비어있으면 아무것도 없기 때문에 False 리턴
        if self.head is None:
            return False
        # head부터 시작해서
        node = self.head
        # node가 존재 하지 않을때까지
        while node is not None:
            # target과 같은 것이 나오면 True 리턴
            if node.data == target:
                return True
            node = node.next
        # 아무것도 나오지 않는다면 False 리턴
        return False

    def appendLeft(self, data):
        # 덱안에 아무것도 없을 경우
        if self.head is None:
            # head와 tail을 새로운 노드에 할당한다.
            self.head = self.tail = DoubleNode(data)
        # 덱안에 노드가 있을 경우
        else:
            # 새로운 노드를 만든 후
            new_node = DoubleNode(data)
            # 새로운 노드의 next포인터로 맨 앞의 노드를 가리킨다.
            new_node.next = self.head
            # 맨 앞의 노드의 prev포인터로 새로운 노드를 가리킨다.
            self.head.prev = new_node
            # head를 새로운 노드로 이동시킨다.
            self.head = new_node
        # 삽입 후 길이를 증가시킨다.
        self.length += 1

    def append(self, data):
        # 덱안에 아무것도 없을 경우
        if self.head is None:
            # head와 tail을 새로운 노드에 할당한다.
            self.head = self.tail = DoubleNode(data)
        else:
            # 새로운 노드를 만든 후
            new_node = DoubleNode(data)
            # 새로운 노드의 prev포인터로 맨 뒤의 노드를 가리킨다.
            new_node.prev = self.tail
            # 맨 뒤의 노드의 next 포인터로 새로운 노드를 가리킨다.
            self.tail.next = new_node
            # tail을 새로운 노드로 이동시킨다.
            self.tail = new_node
        # 삽입 후 길이를 증가시킨다.
        self.length += 1

    def popleft(self):
        # 덱 안에 아무것도 없을 경우 None을 리턴한다.
        if self.head is None:
            return None
        # 뺄 노드를 node변수에 저장해둔다.
        node = self.head
        # 덱 안에 1개만 있을 경우 head와 tail을 None으로 만든다.
        if self.length == 1:
            self.head = self.tail = None
        # 덱 안에 2개 이상의 노드가 있을 경우
        else:
            # 맨 앞의 노드에 있는 head를 두번째 노드로 이동시킨다.
            self.head = self.head.next
            # 맨 앞의 노드가 된 두번째 노드의 prev를 None으로 만든다.
            self.head.prev = None
        # 노드를 뺀 후 길이를 1 줄인다.
        self.length -= 1
        # 저장해뒀던 뺄 노드의 data를 리턴한다.
        return node.data

    def pop(self):
        # 덱 안에 아무것도 없을 경우 None을 리턴한다.
        if self.head is None:
            return None
        # 뺄 노드를 node변수에 저장해둔다.
        node = self.tail
        # 덱 안에 1개만 있을 경우 head와 tail을 None으로 만든다.
        if self.length == 1:
            self.head = self.tail = None
        # 덱 안에 2개 이상의 노드가 있을 경우
        else:
            # 맨 뒤에 노드에 있는 tail를 뒤에서 두번째 노드로 이동시킨다.
            self.tail = self.tail.prev
            # 맨 뒤에 노드가 된 tail의 next를 None으로 만든다.
            self.tail.next = None
        # 노드를 뺀 후 길이를 1 줄인다.
        self.length -= 1
        # 저장해뒀던 뺄 노드의 data를 리턴한다.
        return node.data

    def insert(self, idx, data):
        if idx <= 0:
            self.appendLeft(data)
        elif idx >= self.length:
            self.append(data)
        else:
            node = self.head
            for _ in range(idx-1):
                node = node.next
            new_node = DoubleNode(data)
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
        self.length += 1

    def remove(self, target):
        node = self.head
        while node is not None and node.data != target:
            node = node.next
        if node is None:
            return False
        if node == self.head:
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif node == self.tail:
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        self.length -= 1
        return True

    def reverse(self):
        if self.length < 2:
            return
        self.tail = self.head
        ahead = self.head.next
        while ahead:
            self.head.next = self.head.prev
            self.head.prev = ahead
            self.head = ahead
            ahead = ahead.next
        self.head.next = self.head.prev
        self.head.prev = None

    def my_reverse(self):
        if self.length < 2:
            return
        self.head.prev = self.head.next
        self.head.next = None

        c_node = self.head.prev

        while c_node.next is not None:
            temp_node = c_node.prev
            c_node.prev = c_node.next
            c_node.next = temp_node
            c_node = c_node.prev

        self.tail.next = self.tail.prev
        self.tail.prev = None

        temp = self.head
        self.head = self.tail
        self.tail = temp

def preorder(tree):
    # tree가 문자열 배열
    if not tree:
        return []
    # 결과값 배열
    res = []
    # 스택을 만들고
    stack = Deque()
    # 스택에 0 추가
    stack.append(0)

    # 스택에 값이 있다면 반복
    while stack:
        # index는 0
        index = stack.pop()
        # 결과 값에다가 tree의 인덱스 부분을 넣는다.
        res.append(tree[index])
        # 인덱스를 현재인덱스에 2를 곱하고 2를 더한다.
        # 이걸 그림으로 그리면
        index = 2 * index + 2
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
        index -= 1
        if index < len(tree) and tree[index] is not None:
            stack.append(index)
    return res

graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]}
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}

def bfs(graph, node):
    res = []
    queue = Deque()
    queue.append(node)
    visited = set([node])
    while queue:
        u = queue.popleft()
        res.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return res

print("무방향 그래프의 너비 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", bfs(graph1, 1))
print("노드 2에서 시작: ", bfs(graph1, 2))
print()
print("방향 그래프의 너비 우선 탐색")
print("========================")
print("노드 1에서 시작: ", bfs(graph2, 1))
print("노드 2에서 시작: ", bfs(graph2, 2))