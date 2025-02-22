# 입력 받고
N = int(input())
# 부모 리스트를 입력으로 받고
parent_list = list(map(int, input().split()))
# 아이 리스트를 배열로 초기화 한다.
child_list = [list() for _ in range(N)]

print("parent list :",parent_list)
print("child list :", child_list)

for child in range(1, N) :
  parent = parent_list[child]
  child_list[parent].append(child)

print("added child list :", child_list)

def dfs(node) :
  if not child_list[node] :
    return 0
  result = list()
  for child in child_list[node] :
      # 1
    result.append(dfs(child)) # dfs(1) 3 8 15
    print("result :", result)
  result.sort( reverse = True)
  result = [ result[i] + i + 1 for i in range(len(child_list[node])) ]
  return max(result)

print(dfs(0))