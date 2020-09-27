k = int(input())
m = []
result = []
for i in range(k):
    a = list(reversed(input().split("/")))
    m.append(a)
for i1 in range(3):
    m.sort(key=lambda i: i[i1])
    for i in range(len(m)):
        if m[i][i1] == m[len(m) - 1][i1]:
            result.append(m[i])
    m = result
    result = []
result = m[0][2] + "/" + m[0][1] + "/" + m[0][0]
print(result)
