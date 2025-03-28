
def dfs(n, r, upper_positions):
    possible_case = 0
    possible_positions = [True for _ in range(n)]
    for i, upper_position in enumerate(upper_positions):
        possible_positions[upper_position] = False

        L_cross_position = upper_position - (r - i)
        R_cross_position = upper_position + (r - i)
        if 0 <= L_cross_position:
            possible_positions[L_cross_position] = False
        if R_cross_position < n:
            possible_positions[R_cross_position] = False
    
    possible_positions = [i for i in range(n) if possible_positions[i]]
    
    if r == n - 1:
        return len(possible_positions)
    
    for position in possible_positions:
        possible_case += dfs(n, r + 1, upper_positions + [position])
    return possible_case

n = int(input())
print(dfs(n, 0, []))