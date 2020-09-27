m = [0] * 4
terms = [0] * 4
n = int(input())
sum_exist = False

if n > 4:
    for i in range(4):
        m[i] = int(input())
    for i in range(4, n):
        a = int(input())
        if not sum_exist:
            terms = [m[0], m[0], a, a]
            sum_exist = True
        else:
            if m[0] % 13 != 0 and m[0] > terms[0]:
                terms[0] = m[0]
            if m[0] % 13 == 0 and m[0] > terms[1]:
                terms[1] = m[0]
            if a % 13 != 0 and a > terms[2]:
                terms[2] = a
            if a % 13 == 0 and a > terms[3]:
                terms[3] = a
        for z in range(3):
            m[i]= m[i+1]
        m[3]= a
    if terms[1] % 13 == 0 and terms[3] % 13 == 0:
        if terms[1] + terms[3] > terms[0] + terms[3] or terms[1] + terms[3] > terms[1] + terms[2]:
            print(terms[1], terms[3])
        elif terms[0] + terms[3] > terms[1] + terms[2]:
            print(terms[0], terms[3])
        else:
            print(terms[1], terms[2])
    elif terms[1] % 13 == 0:
        print(terms[1], terms[2])
    elif terms[3] % 13 == 0:
        print(terms[0], terms[3])
    else:
        print("NO")
else:
    print("NO")



