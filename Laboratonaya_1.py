d=int(input())
e=int(input())


def NOD (a,b):#нахождение нод
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def NOK (a,b):#нахождение нок
    return a*b/NOD(a, b)

print(NOK(d,e))