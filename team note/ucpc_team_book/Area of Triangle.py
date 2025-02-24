def area(p1, p2, p3):
    A = p1[0] * p2[1] + p2[0] * p1[1] + p3[0] * p1[1]
    B = p1[1] * p2[0] + p2[1] * p1[0] + p3[1] * p1[0]
    return abs(A - B)