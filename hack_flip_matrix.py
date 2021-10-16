# 1

# 2

# 112 42 83 119

# 56 125 56 49

# 15 78 101 43

# 62 98 114 108


# q = int(input().strip())

q = 1

n = 2

#matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
matrix = [[107, 54, 128, 15], [12, 75, 110, 138], [100, 96, 34, 85], [75, 15, 28, 112]]
print(matrix)

for q_itr in range(q):
    #n = int(input().strip())

    # matrix = []

    # for _ in range(2 * n):
    #     matrix.append(list(map(int, input().rstrip().split())))

    m1 = []
    m2 = []
    m3 = []
    m4 = []
    
    for i in range(n):
        
        m1 += [matrix[i][:n]]
        print(m1)
        m2 += [matrix[i][n:][::-1]]
        print(m2)
        
    for i in range(n, 2*n):
        
        m3 += [matrix[i][:n]]
        print(m3)
        m4 += [matrix[i][n:][::-1]]
        print(m4)
        
    m3 = m3[::-1]
    m4 = m4[::-1]
    res = 0
    #res = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        
        for j in range(n):
            print("i:{},j:{}".format(i,j))
            #res[i][j] = max(m1[i][j], m2[i][j], m3[i][j], m4[i][j])
            res += max(m1[i][j], m2[i][j], m3[i][j], m4[i][j])
    print (res)
    
