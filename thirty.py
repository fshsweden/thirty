from copy import *

def search_exact(arr, target):
    tpl = None
    for a in arr:
        if a == target:
            tpl = a
            print("found a lonesome")
            try:
                arr.remove(a)
            except Exception as e:
                pass
            break
    return arr, tpl

def search_2(arr, target):
    tpl = None

    done = False
    while not done and len(arr) >= 2:
        first = arr[0]
        for x in arr[1:]:
            if not done:
                if first + x == target:
                    print("found a 2some in " + str(first) + " + " + str(x))
                    done = True
                    tpl = (first, x)
                    try:
                        arr.remove(first)
                        arr.remove(x)
                    except Exception as e:
                        pass
                    break

        try:
            if not done:
                arr.remove(first)
        except Exception as e:
            pass

    return arr, tpl


def search_3(arr, target):
    tpl = None

    done = False
    while not done and len(arr) >= 3:
        first = arr[0]
        for x in arr[1:]:
            if not done:
                for y in arr[2:]:
                    if not done:
                        if first + x + y == target:
                            print("found a 3some")
                            done = True
                            tpl = (first, x, y)
                            try:
                                arr.remove(first)
                                arr.remove(x)
                                arr.remove(y)
                            except Exception as e:
                                pass
                            
                            break
        try:
            if not done:
                arr.remove(first)
        except Exception as e:
            pass

    return arr, tpl

def search_4(arr, target):
    tpl = None

    done = False
    while not done and len(arr) >= 4:
        first = arr[0]
        for x in arr[1:]:
            if not done:
                for y in arr[2:]:
                    if not done:
                        for z in arr[3:]:
                            if first + x + y + z == target:
                                print("found a 4some")
                                done = True
                                tpl = (first, x, y, z)
                                try:
                                    arr.remove(first)
                                    arr.remove(x)
                                    arr.remove(y)
                                    arr.remove(z)
                                except Exception as e:
                                    pass
                                break
        try:
            if not done:
                arr.remove(first)
        except Exception as e:
            pass

    return arr, tpl

def search_5(arr, target):
    tpl = None

    done = False
    while not done and len(arr) >= 5:
        first = arr[0]
        for x in arr[1:]:
            if not done:
                for y in arr[2:]:
                    if not done:
                        for z in arr[3:]:
                            if not done:
                                for i in arr[4:]:
                                    if first + x + y + z + i == target:
                                        print("found a 5some")
                                        done = True
                                        tpl = (first, x, y, z, i)
                                        try:
                                            arr.remove(first)
                                            arr.remove(x)
                                            arr.remove(y)
                                            arr.remove(z)
                                            arr.remove(i)
                                        except Exception as e:
                                            pass
                                        break
        try:
            if not done:
                arr.remove(first)
        except Exception as e:
            pass

    return arr, tpl

def search_6(arr, target):
    tpl = None

    done = False
    while not done and len(arr) >= 6:
        first = arr[0]
        for x in arr[1:]:
            if not done:
                for y in arr[2:]:
                    if not done:
                        for z in arr[3:]:
                            if not done:
                                for i in arr[4:]:
                                    if not done:
                                        for p in arr[5:]:
                                            if first + x + y + z + i + p == target:
                                                print("found a 6some")
                                                done = True
                                                tpl = (first, x, y, z, i, p)
                                                try:
                                                    arr.remove(first)
                                                    arr.remove(x)
                                                    arr.remove(y)
                                                    arr.remove(z)
                                                    arr.remove(i)
                                                    arr.remove(p)
                                                except Exception as e:
                                                    pass
                                                break
        try:
            if not done:
                arr.remove(first)
        except Exception as e:
            pass

    return arr, tpl



def search(arr, target):

    orig = copy(arr)
    res_of_1 = []

    print("Searching 1")
    # Stage 1
    while True:
        arr, tpl = search_exact(arr, target)
        if tpl is None:
            break
        else:
            res_of_1.append(tpl)

    print("Searching 2")
    res_of_2 = []
    arr = copy(orig)
    while True:
        arr, tpl = search_2(arr, target)
        if tpl is None:
            break
        else:
            res_of_2.append(tpl)

    print("Searching 3")
    res_of_3 = []
    arr = copy(orig)

    while True:
        arr, tpl = search_3(arr, target)
        if tpl is None:
            break
        else:
            res_of_3.append(tpl)

    print("Searching 4")
    res_of_4 = []
    arr = copy(orig)

    while True:
        arr, tpl = search_4(arr, target)
        if tpl is None:
            break
        else:
            res_of_4.append(tpl)

    print("Searching 5")
    res_of_5 = []
    arr = copy(orig)

    while True:
        arr, tpl = search_5(arr, target)
        if tpl is None:
            break
        else:
            res_of_5.append(tpl)

    print("Searching 6")
    res_of_6 = []
    arr = copy(orig)

    while True:
        arr, tpl = search_6(arr, target)
        if tpl is None:
            break
        else:
            res_of_6.append(tpl)

    return res_of_1, res_of_2, res_of_3, res_of_4, res_of_5, res_of_6

    # r3 = [(1,4),(1,4),(1,4)]


#
# Check if all parts of tuple still exists in array
#
def all_items_still_in_array(tpl, arr):
    arr_cpy = copy(arr)
    for tplitem in list(tpl):
        try:
            arr_cpy.remove(tplitem)
        except:
            return False
    return True


a = [1, 1, 1, 2, 4, 4]
TARGET=5
a = sorted(a)
print(f"Original array: {a}")

groups = search(a, TARGET)

# DEBUG print list
# groupnum = 1
# for g in groups:
#     print(f"group #{groupnum}:{g}")
#     for x in list(g):
#         print(f"Tuple-item in group is: {x}")
#         for y in list(x):
#             print(f"    Item in tuple is: {y}")
#     groupnum += 1


print("Counting points!")
points = 0
for g in groups:
    for tpl in list(g):

        if all_items_still_in_array(tpl, a):
            print(f"YUP, counting this one: {tpl}")
            points += TARGET
            for item in list(tpl):
                a.remove(item)
        else:
            print("NOPE, can't use this one")


print(f"When target is {TARGET}, points = {points}")
print(f"This is what is left of array: {a}")
