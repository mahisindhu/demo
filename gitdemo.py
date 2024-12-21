print("hello")
def rotate_by_90(mat):
    n = len(mat)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Step 2: Reverse the columns
    for j in range(n):
        for i in range(n // 2):
            mat[i][j], mat[n - i - 1][j] = mat[n - i - 1][j], mat[i][j]

def print_matrix(mat):
    for row in mat:
         print(" ".join(map(str, row)))