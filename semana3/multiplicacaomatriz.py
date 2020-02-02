#1 2 3          1 2          1*1+2*3+3*5   1*2+2*4+3*6
#         *     3 4     =    
#4 5 6          5 6          4*1+5*3+6*5   4*2+5*4+6*6

def mat_mul(A,B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_linhas_B

    C = []
    for linha in range(num_linhas_A):
        C.append([])
        for coluna in range(num_colunas_B):
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C

if __name__ == '__main__':
    A = [[1,2,3], [4,5,6]]
    B = [[1,2], [3,4], [5,6]]
    print(mat_mul(A,B))