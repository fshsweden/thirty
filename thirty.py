def sumof2(arr, answer):
    res = []
    for x in arr:
        for y in arr:
            if x+y == answer:
                res.append((x,y))

    return res

def sumof3(arr, answer):
    res = []
    for x in arr:
        for y in arr:
            for z in arr:
                if x+y+z == answer:
                    res.append((x,y,z))

    return res

def sumof4(arr, answer):
    res = []
    for x in arr:
        for y in arr:
            for z in arr:
                for a in arr:
                    if x+y+z+a == answer:
                        res.append((x,y,z,a))

    return res


def sumof5(arr, answer):
    res = []
    for x in arr:
        for y in arr:
            for z in arr:
                for a in arr:
                    for b in arr:
                        if x+y+z+a+b == answer:
                            res.append((x,y,z,a,b))

    return res

def sumof6(arr, answer):
    res = []
    for x in arr:
        for y in arr:
            for z in arr:
                for a in arr:
                    for b in arr:
                        for c in arr:
                            if x+y+z+a+b+c == answer:
                                res.append((x,y,z,a,b,c))

    return res

# 0 represents a "dice not counted"

a = [0,1,2,3,4,5,6]

print(set(sumof2(a, 5)))
print(set(sumof3(a, 5)))
print(set(sumof4(a, 5)))
print(set(sumof5(a, 5)))
print(set(sumof6(a, 5)))

