N = 1
capacity = [[0 for __ in range(N)] for _ in range(N)]
flow = [[0 for __ in range(N)] for _ in range(N)]
adjacent = [[] for _ in range(N)]

# setting capacity, adjacent => multi direction
def flow_update(start, end, path):
	flow_value = float("inf")
	current = end
	
	# finding min flow_value 
	while current != start:
		flow_value = min(flow_value, capacity[path[current]][current] - flow[path[current]][current])
		current = path[current]
	
	# flow chart update
	current = end 
	while current != start:
		flow[path[current]][current] += flow_value
		flow[current][path[current]] -= flow_value
		current = path[current]
	return flow_value

def bfs(start, end):
	path = [-1 for _ in range(N)]
	queue = [start]
	for u in queue:
		for v in adjacent[u]:
			if capacity[u][v] - flow[u][v] > 0 and path[v] == -1:
				queue.append(v)
				path[v] = u
				if v == end:
					return flow_update(start, end, path)
	return 0

def edmonds_karp(start, end):
	max_flow = 0
	while True:
		addition = bfs(start, end)
		if addition > 0:
			max_flow += addition
		else:
			break
	return max_flow