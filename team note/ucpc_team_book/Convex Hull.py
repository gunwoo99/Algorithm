
def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

# def convex_hull(points):
#     hull = [min(points)]
    
#     while True:
#         next_point = points[0]
#         for point in points[1:]:
#             cp = ccw(hull[-1], next_point, point)
#             if cp < 0:
#                 next_point = point
#             elif cp == 0:
#                 dist1 = abs(next_point[0] - hull[-1][0]) + abs(next_point[1] - hull[-1][1])
#                 dist2 = abs(point[0] - hull[-1][0]) + abs(point[1] - hull[-1][1])
#                 if dist2 > dist1:
#                     next_point = point

#         if next_point == hull[0]:
#             break

#         hull.append(next_point)

#     return hull

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

print(min(points))
# print(len(convex_hull(points)))