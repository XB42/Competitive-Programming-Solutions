try:
    ctr = 0
    T = int(input())
    for testcases in range(T):
        N = int(input())
        A = [0]*N
        A = input().split()
        for i in range(N):
            A[i] = float(A[i])
            A[i] = 1/A[i]
        for i in range(N):
            for j in range(i+1,N):
                if A[i] + A[j] == 1:
                    ctr +=1
        print(ctr)
except:
    pass