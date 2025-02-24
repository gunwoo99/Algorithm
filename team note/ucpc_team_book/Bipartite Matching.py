left = []
right = []

E = [[] for _ in range(len(left))]
solution = [-1 for _ in range((len(right)))]
visited = [False for _ in range(len(right))]

def dfs(u):
	for v in E[u]:
		if visited[v]:
			continue
        
		visited[v] = True
		if solution[v] == -1 or dfs(solution[v]):
			solution[v] = u
			return True
	return False

for i in range(len(left)):
	visited = [False for _ in range(len(right))]
	dfs(i)