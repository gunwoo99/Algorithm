A = [0, 0, 0, 0]
B = [0, 0, 0, 0]
# def cross_product3D(v1, v2):
#     i = v1[1] * v2[2] - v1[2] * v2[1]
#     j = v1[2] * v2[0] - v1[0] * v2[2]
#     k = v1[0] * v2[1] - v1[1] * v2[0]
#     return [i, j, k]

def cross_product2D(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def point_to_vector(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1]]

def intersection(A, B):
    VA = point_to_vector(A[:2], A[2:])
    AtoB1 = cross_product2D(VA, point_to_vector(A[:2], B[:2]))
    AtoB2 = cross_product2D(VA, point_to_vector(A[:2], B[2:]))
    if AtoB1 * AtoB2 > 0:
        return False
    
    VB = point_to_vector(B[:2], B[2:])
    BtoA1 = cross_product2D(VB, point_to_vector(B[:2], A[:2]))
    BtoA2 = cross_product2D(VB, point_to_vector(B[:2], A[2:]))
    if BtoA1 * BtoA2 > 0:
        return False
    
    if AtoB1 * AtoB2 == 0 or BtoA1 * BtoA2 == 0:
        if max(A[0], A[2]) < min(B[0], B[2]):
            return False
        if max(B[0], B[2]) < min(A[0], A[2]):
            return False
        if max(A[1], A[3]) < min(B[1], B[3]):
            return False
        if max(B[1], B[3]) < min(A[1], A[3]):
            return False
    return 1