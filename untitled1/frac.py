alphabet = "←→↑↓"
a = "00000"
k = 0
while a != "33333":
    if a[0] != "2" and a[0] != a[2] and a[2] != a[4] and a[1] != a[3]:
        k += 1
        print("    " +
              alphabet[int(a[0])] + alphabet[int(a[1])] + alphabet[int(a[2])] + alphabet[int(a[3])] + alphabet[
                  int(a[4])])
    else:
        print(
            alphabet[int(a[0])] + alphabet[int(a[1])] + alphabet[int(a[2])] + alphabet[int(a[3])] + alphabet[int(a[4])])

    a = list(a)
    a[4] = str(int(a[4]) + 1)
    for i in reversed(range(len(a))):
        if a[i] == "4":
            a[i] = "0"
            a[i - 1] = str(int(a[i - 1]) + 1)
    a = "".join(a)

print(alphabet[int(a[0])] + alphabet[int(a[1])] + alphabet[int(a[2])] + alphabet[int(a[3])] + alphabet[int(a[4])])
if a[0] != "2" and a[0] != a[2] and a[2] != a[4] and a[1] != a[3]:
    k += 1
print(k)
