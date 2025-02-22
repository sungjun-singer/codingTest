import heapq

def heappush(heap, data):
    # 맨 뒤에 새로운 요소 넣기
    heap.append(data)
    # 새로운 요소 인덱스 반환
    current = len(heap) - 1
    # 새로운 요소가 루트로 간다면 반복문 탈출
    while current > 0:
        # 자식 노드가 부모 X 2 이거나 부모 X 2 + 1이기 때문에 역순으로 부모노드 인덱스 구하기
        parent = (current - 1) // 2
        # 부모가 새로운 노드보다 더 크다면 swap
        if heap[parent] > heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            current = parent
        else:
            break


def my_heappush(heap, data):
    heap.append(data)

    current = len(heap) - 1
    while current > 0:
        parent = (current - 1) // 2
        if heap[current] < heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
            current = parent
        else:
            break

def heappop(heap):
    # 힙에 아무것도 없으면 "Empty heap!!!"
    if not heap:
        return "Empty heap!!"
    # 힙에 요소가 하나만 있다면 그 요소 pop
    elif len(heap) == 1:
        heap.pop()
    # pop_data 임시 저장, 마지막 요소 루트로 이동(다시 정렬하기 위함)
    pop_data, heap[0] = heap[0], heap.pop()
    # 루트와 그 자식부터 시작한다.
    current, child = 0, 1
    # child의 길이가 heap 범위를 넘어간다면 반복문 탈출
    while child < len(heap):
        # 형제 노드 인덱스
        sibling = child + 1
        # 형제 노드와 자식 노드를 비교해 형제 노드가 더 작다면 형제노드가 루트로 올라갈 자격이 있다.
        if sibling < len(heap) and heap[child] > heap[sibling]:
            child = sibling
        # 부모노드가 자식 노드보다 더 크다면 위치 swap
        if heap[current] > heap[child]:
            heap[current], heap[child] = heap[child], heap[current]
            # 다음 단계로 간다.
            current = child
            child = current * 2 + 1
        else:
            break
    return pop_data

def my_heappop(heap):
    if not heap:
        return "Empty heap!!"
    elif len(heap) == 1:
        return heap.pop()
    pop_data, heap[0] = heap[0], heap.pop()

    current, child = 0, 1
    while child < len(heap):
        sibling = child + 1
        if sibling < len(heap) and heap[sibling] < heap[child]:
            child = sibling
        if heap[child] < heap[current]:
            heap[current], heap[child] = heap[child], heap[current]
            current = child
            current = child * 2 + 1
        else:
            break
    return pop_data


def heapify(arr):
    current = start = len(arr) - 1

    while start > 0:
        is_swap = False
        while current > 0:
            parent = (current - 1) // 2
            if arr[parent] > arr[current]:
                # 부모가 더 크다면 swap
                arr[parent], arr[current] = arr[current], arr[parent]
                # swap 후 다음 단계로
                current = parent
                is_swap = True
            else:
                break
        if is_swap:
            current = start
        else:
            current = start = current - 1

""" 
0 1 2 3 4 5 6
cur = 6
start = 6
parent = 2


        7
    5        3
1     2   4    6

"""



h1 = [3,4,5,1,2]
h2 = [3,4,5,1,2]

heapq.heapify(h1)
heapify(h2)

heapq.heappush(h1, 2)
heapq.heappush(h1, 3)
heapq.heappush(h1, 4)
heapq.heappush(h1, 5)
heapq.heappush(h1, 6)
my_heappush(h2, 2)
my_heappush(h2, 3)
my_heappush(h2, 4)
my_heappush(h2, 5)
my_heappush(h2, 6)

print(h1)
print(h2)



