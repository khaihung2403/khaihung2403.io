def ex_list1(lst: list):
    i=0
    for char in lst:
        if len(char) >= 2 and char[0] == char[-1]:
            i = i+1
    return i
def ex_list2(n: int, s: str):
    newlist = []
    lst = s.split()
    for num in lst:
        if len(num) > n:
            newlist.append(num)
    return newlist
def ex_list3(lst: list):
    dem = 0
    for num in lst:
        if num > 2 and (num % i != 0 for i in range(2, int(num**0.5) + 1)):
            dem = dem+1
    if dem == len(lst):
        return True
    return False   
def ex_list4(lst: list):
    if len(lst) == 1:
        return [lst]
    permutations = []
    for i in range(len(lst)):
        current_element = lst[i]
        remaining_list = lst[:i] + lst[i+1:]
        for perm in ex_list4(remaining_list):
            permutations.append([current_element] + perm)
    return permutations
def ex_list5(lst: list):
    tong = 1
    sum = 1
    i = 0
    dodai  = len(lst)
    while i < dodai - 1:
        if lst[i] < lst[i + 1]:
            tong = tong + 1
            sum = max(tong,sum)
        else:
            tong = 1
        i = i+1
    return sum
def ex_list6(lst1: list, lst2: list):
    list1 = []
    for num in lst1:
            if num in lst2:
                list1.append(num)
    list2 = set(list1)
    list2 = sorted(list(list2))
    return list2
def ex_list7(lst: list):
    for num in lst:
        solan = lst.count(num)
        if solan == 1:
            return num
            break
    return None
def ex_list8(k: int, lst: list):
    lst = sorted(lst)
    length = len(lst)
    return lst[length-k]
def ex_list9(lst: list, sum: int):
    list1 = []
    lst = sorted(lst)
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst[j] == sum:
                list1.append((lst[j],lst[i]))
    list1.reverse()          
    return list1
def ex_list10(lst: list):
    list1 = []
    for num in lst:
        for i in num:
            list1.append(i)
    list1 = sorted(list1)
    return list1
def ex_dict1(a: int, b: int):
    dict = {}
    for i in range(a,b+1):
        dict.update({i : i*i})
    return dict
def ex_dict2(d: dict):
    dict1 = {key: d[key] for key in sorted(d.keys())}
    return dict1
def ex_dict3(d1: dict, d2: dict):
    dict1 = {key: d[key] for key in sorted(d.keys())}
    return dict1
def ex_dict4(d: dict):
    dict1 = ['']
    for key in d:
        result = []
        for num in dict1:
            for value in d[key]:
                result.append(num + value)
        dict1 = result
    dict2 = set(dict1)
    return dict2
def ex_dict5(s: str):
    dict1 = {}
    lst = list(s)
    for char in lst:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    return dict1
def ex_dict6(lst1: list, lst2: list):
    dict1 = {}
    for i in range(len(lst1)):
        if lst1[i] not in dict1:
            dict1[lst1[i]] = set()
            dict1[lst1[i]].add(lst2[i])
    return dict1 
def ex_dict7(lst1: list, lst2:list, lst3:list):
    dict1 = []
    for i in range(len(lst1)):
        student = {lst1[i]: {lst2[i]: lst3[i]}}
        dict1.append(student)
    return dict1
def ex_dict8(lst: list):
    dict1 = {}
    for key,value in lst:
        if key in dict1:
            dict1[key].append(value)
        else:
            dict1[key] = [value]
    return dict1
def ex_dict9(d: dict):
    list1 = list(d.values())
    tong = 0
    for string in list1:
        tong += len(string)
    return tong
def ex_dict10(d: dict):
    dict1 = {}
    for key in d:
        if d[key] in dict1:
            dict1[d[key]].append(key)
        else:
            dict1[d[key]] = [key]
    return dict1
def ex_set1(set1: set, set2: set):
    set3 = set()
    for num in set1:
        if num in set2:
            set3.add(num)
    return set3
def ex_set2(set1: set, set2: set):
    set3 = set()
    set3 = set1.union(set2)
    for num in set1:
        if num in set2:
            set3.remove(num)
    return set3
def ex_set3(set1: set, set2: set):
    list1 = []
    set3 = set()
    set4 = set()
    for num in set1:
        if num not in set2:
            set3.add(num)
    list1.append(set3)
    for num in set2:
        if num not in set1:
            set4.add(num)
    list1.append(set4)
    return tuple(list1)
def ex_set4(count: int, lst1: list):
    list1 = set()
    n = len(lst1)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if lst1[i] + lst1[j] + lst1[k] == count:
                    list1.add(tuple(sorted((lst1[i], lst1[j], lst1[k]))))
    return list(list1)
def ex_set5(set1: set, set2: set):
    count = 0
    for num in set2:
        if num in set1:
            count = count + 1
    if count == len(set2):
        return True
    return False
def ex_set6(set1: set):
    list1 = list(set1)
    list1 = sorted(list1)
    list2 = set(list1)
    list2 = list(list2)
    if len(list2) < 3:
        return None
    return list2[-3]
def ex_set7(set1: set):
    list1 = list(set1)
    del list1[0]
    list1 = set(list1)
    return list1
print(ex_set7({0, 1, 3, 4, 5}))