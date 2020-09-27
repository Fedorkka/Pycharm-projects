N = int(input())
arr = []
arr2 = []
for i in range(N):
    A, B = input().split
arr.append(A)
arr2.append(B)
arr3 = []
for i in range(N):
    for k in arr[i]:
        if k in arr3:
            continue
else:
    arr3.append(k)
arr4 = []
for i in range(len(arr3)):
    arr4.append(0)
for i in range(N):
    for k in arr:
        for b in len(arr3):
            if k == arr[b]:
                arr4[b] += arr2[i]
print(max(arr4))
