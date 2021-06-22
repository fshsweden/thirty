from copy import *

def search_exact(arr, target):
    tpl = None
    for a in arr:
        if a == target:
            tpl = a
            print("found a lonesome")
            arr.remove(a)
            break
    return arr, tpl

def search_2(arr, target):
    tpl = None

    done = False
    while not done and len(arr) >= 2:

        # arr

        first = arr[0]
        for x in arr[1:]:
            if first + x == target:
                print("found a 2some")
                done = True
                tpl = (first, x)
                arr.remove(first)
                arr.remove(x)
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
                    if first + x + y == target:
                        print("found a 3some")
                        done = True
                        tpl = (first, x, y)
                        arr.remove(first)
                        arr.remove(x)
                        arr.remove(y)
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

    return res_of_1, res_of_2, res_of_3

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


a = [1, 1, 4, 4, 1, 2]
TARGET=6
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
