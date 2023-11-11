# %%

import heapq

def dijkstra(graph, start):
    # 각 정점까지의 현재 최단 거리를 무한대로 초기화
    distance = {node: float('inf') for node in graph}
    # 시작 정점의 최단 거리는 0으로 설정
    distance[start] = 0
    # 시작 정점을 포함한 우선순위 큐를 초기화
    priority_queue = [(0, start)]

    while priority_queue:
        # 현재까지의 최단 거리와 정점을 추출
        current_distance, current_node = heapq.heappop(priority_queue)

        # 현재 노드의 최단 거리가 이미 업데이트된 경우, 무시
        if current_distance > distance[current_node]:
            continue

        # 현재 노드의 인접 정점을 순회
        for neighbor, weight in graph[current_node].items():
            # 현재 노드를 통해 가는 거리
            distance_through_current = current_distance + weight

            # 더 짧은 거리를 찾았을 경우 업데이트
            if distance_through_current < distance[neighbor]:
                distance[neighbor] = distance_through_current
                # 우선순위 큐에 업데이트된 거리와 정점 추가
                heapq.heappush(priority_queue, (distance_through_current, neighbor))

    return distance

# 그래프 예제
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

# 결과 출력
for node, distance in shortest_distances.items():
    print(f'Shortest distance from {start_node} to {node}: {distance}')


# %%
def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    visited[node] = True
    print(node, end=' ')
    print(visited)

    # 현재 노드와 연결된 모든 인접 노드를 재귀적으로 방문
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 예시 그래프 (인접 리스트로 표현)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

# 노드의 방문 여부를 나타내는 배열
visited = [False] * len(graph)

# 시작 노드를 지정하여 DFS 실행
start_node = 0
print("DFS 탐색 결과:")
dfs(graph, start_node, visited)


# %%
def test():
    return 0
#test

# %%
import numpy as np

# Assuming you have the data stored as NumPy arrays or lists
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
data2 = np.array([[4, 5, 6], [10, 11, 12]])

# Extract the columns 2 and 3 from data and data2
data_subset = data[:, 1:3]
data2_subset = data2[:, 1:3]

# Check if the rows in data_subset exist in data2_subset
mask = np.isin(data_subset, data2_subset)

# Filter the rows in data using the mask
result = data[mask[:, 0] & mask[:, 1]]

print(result)


# %%
data, data2

# %%
data_subset, data2_subset

# %%
mask

# %%
import heapq

min_heap = []

heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)

print(min_heap)
min_value = heapq.heappop(min_heap)
print(min_heap)


# %%
# 원래 2차원 배열
original_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 가로와 세로 변경된 2차원 배열
transposed_array = [list(row) for row in zip(*original_array)]

# 결과 출력
for row in transposed_array:
    print(row)

# %%
zip(*original_array)


