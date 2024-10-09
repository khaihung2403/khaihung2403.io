def test(nums: list):
    num1 = set(nums)
    tong = 0
    for num in num1:
        solan = nums.count(num)
        if solan == 4:
            tong += 1
    if tong == len(num1):
        return True
    return False
def test(M: list, T: int):
    matran = {}
    index = 0
    lst = []
    for num in M:
        matran[index] = num
        index += 1
    for key in range(len(M)):
        num1 = matran[key]
        for i in range(len(num1)):
            if num1[i] == T:
                lst.append([key,i])
    return lst
def test(string: str):
    sum = 0
    for char in string:
        if char.isupper():
            sum += ord(char)
    return sum
def test(nums: list):
    list1 = []
    if nums[0] < nums[1]:
        list1.append(0)
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            list1.append(i)
    return list1
def test(nums: list):
    list1 = []
    tong = nums[0]
    for i in range(len(nums)):
        if nums[i] >= tong:
            list1.append(nums[i])
            tong  =  nums[i]
        else:
            list1.append(tong)
    return list1
def binary_search(item_list: list, item: int) -> bool:
    left, right = 0, len(item_list)-1

    while left <= right:
        mid = (left + right) //2
        if item_list[mid] == item:
            return True
            break
        elif item_list[mid] < item:
            left = mid+1
        else:
            right = mid - 1
    return False
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return False
def test(string: str):
    string = string.replace(" ","")
    mang1 = []
    bien = ""
    mang2 = []
    for char in string:
        bien += char
        if char == "(":
            mang1.append(char)
        elif char == ")":
            mang1.pop()
        if not mang1:
            mang2.append(bien)
            bien = ""
    return mang2

print(binary_search([1,2,3,5,8], 6))