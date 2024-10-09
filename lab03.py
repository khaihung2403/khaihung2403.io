//bai1
def perfect_number(n):
    sum = 0
    x = n
    for i in range(1,(int)(n/2)+1):
        if n%i==0:
            sum += i
    if sum == x:
        return True
    return False
//bai2
def pascal_triangle(n):
    list1 = [0]
    lst1 = [1]
    lst2 = [1]
    lst3 = []
    lst4 = [[1]]
    for i in range(n-1):
        lst1 = lst1 + list1
        lst2 = list1 + lst2
        for l1,l2 in zip(lst1,lst2):
            lst3.append(l1+l2) 
        lst1 = lst3[:]
        lst2 = lst3[:]
        lst4.append(lst3[:])
        lst3.clear()
    return lst4
//bai3
def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.lower()
    str1 = set(str1)
    str1.remove(' ')
    if len(str1) == 26:
        return True
    return False
//bai4
mangmoi = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sapxep = sorted(mangmoi, key=lambda x:x[1])
print(sapxep)
//bai 5
mangmoi = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sapxep = sorted(mangmoi, key=lambda x: int(x['model']),reverse=True)
print(sapxep)
//bai6
mang = [1,2,3,4,5,6,7,8,9,10]
mang1 = list(filter(lambda x:x%2==0,mang))
mang2 = list(filter(lambda x:x%2==1,mang))
print(mang1)
print(mang2)
//bai6
mang = [1,2,3,4,5,6,7,8,9,10]
mang1 = list(map(lambda x:x**2,mang))
mang2 = list(map(lambda x:x**3,mang))
print(mang1)
print(mang2)
//bai7
timestring = "2020-01-15 09:03:32.744178"
date_part, time_part = timestring.split() 
year, month, day = date_part.split('-')      
time = time_part
print(int(year)) 
print(int(month))
print(int(day))
print(time)
//bai8
def fibonacci(n):
    fibo = []
    fibonaci = lambda a,b: (b,a+b)
    a,b = 0,1
    for i in range(n):
    fibo.append(a)
    a, b = fibonaci(a, b)
    return fibo
//bai9
list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
lst = {}
for num in list1:
    tong = sum(num)
    if tong not in lst:
        lst[tong] = []
    lst[tong].append(num)
sapxep = sorted(lst.items(),key=lambda x:x[0])
sapxep1 = lambda x: x[1]
for i in sapxep:
    print(sapxep1(i))
//bai10
mang1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
mang2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

avergrade = lambda x: sum(x) / len(x)
result1 = tuple(map(avergrade, zip(*mang1)))
result2 = tuple(map(avergrade, zip(*mang2)))

print(result1)
print(result2)
