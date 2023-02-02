T = int(input())
for testcases in range(T):
    N = int(input())
    nlist = [0]*N
    mlist = [0]*N

    for i in range(N):
        abc = input()
        if abc[0:2] not in ['11 ', '12 ', '13 ', '14 ', '15 ']:
            if abc[0:2] in ['1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ']:
                mlist[i], nlist[i] = abc.split()
                mlist[i] = int(mlist[i])
                nlist[i] = int(nlist[i])

    total = 0
    for i in range(N):
        max = nlist[i]
        for j in range(i+1,N):
            if mlist[i] == mlist[j] and mlist[i] > 0:
                if nlist[i] < nlist[j]:
                    max = nlist[j]
                nlist[j] = 0
        total += max
    print(total)