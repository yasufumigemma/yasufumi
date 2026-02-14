A = [[1, 2],
     [3, 4]]

B = [[2, 3],
     [4, 5]]

# 2x2 行列同士の積 C = A * B
C = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        C[i][j] = sum(A[i][k] * B[k][j] for k in range(2))

print(C)
