def mat_mult(A, B): 
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def mat_transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def mat_inverse_3x3(M):
    det = (
        M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
        - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
        + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
    )

    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")

    inv = [[0]*3 for _ in range(3)]
    inv[0][0] =  (M[1][1]*M[2][2] - M[1][2]*M[2][1]) / det
    inv[0][1] = -(M[0][1]*M[2][2] - M[0][2]*M[2][1]) / det
    inv[0][2] =  (M[0][1]*M[1][2] - M[0][2]*M[1][1]) / det

    inv[1][0] = -(M[1][0]*M[2][2] - M[1][2]*M[2][0]) / det
    inv[1][1] =  (M[0][0]*M[2][2] - M[0][2]*M[2][0]) / det
    inv[1][2] = -(M[0][0]*M[1][2] - M[0][2]*M[1][0]) / det

    inv[2][0] =  (M[1][0]*M[2][1] - M[1][1]*M[2][0]) / det
    inv[2][1] = -(M[0][0]*M[2][1] - M[0][1]*M[2][0]) / det
    inv[2][2] =  (M[0][0]*M[1][1] - M[0][1]*M[1][0]) / det

    return inv

def fit_regression(x1, x2, y):
    n = len(y)
    X = [[1, x1[i], x2[i]] for i in range(n)]
    Y = [[y[i]] for i in range(n)]

    Xt = mat_transpose(X)
    XtX = mat_mult(Xt, X)
    XtX_inv = mat_inverse_3x3(XtX)
    XtY = mat_mult(Xt, Y)
    B = mat_mult(XtX_inv, XtY) 

    b0, b1, b2 = B[0][0], B[1][0], B[2][0]
    return b0, b1, b2

x1 = [1, 2, 3, 4]
x2 = [2, 1, 3, 5]
y  = [2, 3, 6, 8]

b0, b1, b2 = fit_regression(x1, x2, y)
print("Intercept (b0):", b0)
print("Coeff b1:", b1)
print("Coeff b2:", b2)
