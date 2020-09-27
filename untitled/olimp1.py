res = []
r = int(input())

for j in range(r):
    res.append(0)
    nusfl = input()
    pred = list(map(int, input().split()))
    vict = list(map(int, input().split()))
    l_v = max(pred)
    pred.sort()
    vict.sort(reverse=True)
    for z in range(len(vict)):
        for i in range(len(pred)):
            if pred > vict

    for i in range(len(pred)):
        for z in range(len(vict)):
            if i>0 and pred[i]>l_v:
                res[j] += l_k
                break
            if pred[i] > vict[z]:
                l_v= vict[z]
                l_k= len(vict) - z
                res[j] += l_k
                break
for i in res:
    print(i)
