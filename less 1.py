s = input().replace(' ', '')

for i in range(len(s)):
    s[i] = int(s[i])
    print(type(s[i]))












'''s = input()
n = input()

lst = []
for i in s:
    lst.extend(i)
    lst.append(n)
print(*lst[:-1:], sep='')'''

'''s = input().split('.')
lst = []
for i in range(len(s)):
    s[i] = int(s[i])
    if 0 <= s[i] <= 255:
        lst.append(True)
    else:
        lst.append(False)

if False not in lst:
    print('ДА')
else:
    print('НЕТ')'''

'''   if 1 <= len(s[i]) <= 3 :
       print('ДА')
   else:
       print('НЕТ')'''

'''s = input()

for i in s.split():
    i = int(i)
    print(end='\n')
    for k in range(i):
        print('+', end='')'''

'''s = int(input())
lst = []
for i in range(s):
    n = input()

    if n not in lst:
        lst.append(n)
    else:
        continue
print(lst)'''

'''s = int(input())

lst = []

for i in range(s):
    n = int(input())
    lst.append(n)

lst.remove(min(lst))
lst.remove( max(lst))

print(s, lst)'''

'''s = int(input())
lst = []
lst2 = []

for i in range(s):
    n = int(input())
    lst2.append(n)
    lst.append(n**2+2*n+1)
print(*lst2, sep='\n', end='\n\n')
print(*lst, sep='\n')'''

'''numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

lst = []

for i in numbers:
    lst.append(i ** 2)
print(sum(lst))'''

'''s = int(input())
lst =[]
for i in range(s):
    n = input()
    lst.extend(n)
print(lst)'''

'''s = int(input())
lst = []

for i in range(s):
    n = input()
    lst.append(n)

k = int(input())

for q in range(len(lst)):
    if k > len(lst[q]):
        continue
    g = lst[q][k - 1]
    print(g, end='')'''

'''s = int(input())
lst = []

for i in range(s):
    n = int(input())
    lst.append(n)



print(lst[0::2])'''

'''s = int(input())
lst = []
for i in range(1,s+1):
    if s % i == 0:
        lst.append(i)
print(lst)'''

'''n = int(input())
lst = []

for i in range(n):
    s = int(input())
    g = s**3
    lst.append(g)
print(lst)'''

'''h = []
for i in range(28):
    yy = chr(96+i)
    h.append(yy*i)
print(h[1:-1])'''

'''s = int(input())
lst = []
for i in range(s):
    name = input()
    lst.append(name)
print(lst)'''

'''numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[-1]
del numbers[0]
print(numbers)'''

'''rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

rainbow[3],rainbow[-1] = 'зелёный', 'фиолетовый'

print(rainbow)'''

'''
lst = []

for i in range(1, s+1):
     lst.append(i)
print(lst)'''

'''
massiv = []

while len(massiv) < 5:
    g = int(input())
    if g == 0:
        massiv.append(False)
    else:
        massiv.append(True)
print(sorted(massiv))'''

'''s = 'abch12345h'


u = s[s.find('h'):s.rfind('h'):]
j = u[::-1]
g = s[:s.find('h')] + s [s.rfind('h')+1:s.find('h'):-1] + s[s.rfind('h'):]


print(g)'''

'''s = input()


if s.count('f') == 1:
    print('-1')

elif s.count('f') > 1:
    s = s.replace('f', 'h', 1)
    print(s.find('f'))

elif s.count('f') == 0:
    print('-2')'''

'''for i in range(len(s)):
    if '1' in s:
        s.replace('1', 'one')
        print(s)'''

'''a = ''
count = -1
while a != 'стоп' and a != 'хватит' and a != 'достаточно':
    count += 1
    a = input()

print(count)'''

'''text = input()
total = 0
while text != 'стоп' and text != 'хватит' and text != 'достаточно':
    text = input()
    total = total + 1
print(total)'''

'''a = int(input())
total = 0
for i in range(1,a+1):
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        total += a
print(total)'''

'''total = 1
for i in range(10):
    a = int(input())
    if a == 0:

        pass
    else:
        total = a * total
print(total)'''

'''a = int(input())

factorial = 1
for i in range(1,a+1):
    factorial  *=i
print(factorial)'''

'''a = int(input())

total = 0
for i in range(1, a+1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        total = total + i
print(total)'''

'''a = int(input())
total = 0
for i in range(a):
    b = int(input())

    total += b
print(total)'''

'''-------------------a = int(input())
b = int(input())
total = 0

for i in range(a, b +1):
    count = 0
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total =+ i
    count =+ 1
    print(count)---------------------------'''

'''total = 0
for i in range(1, 6):
    total += i
    print(total, end='')'''

'''a = int(input())
b = int(input())


for i in range(a,b+1): 
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)'''

'''a = int(input())
b = int(input())


if a > b:
    for i in range(a,b-1, -1):
        print(i)
else:
    for i in range(a,b+1):
        print(i)'''

'''a = input()
Saturday = 'суббота'
Sunday = 'воскресенье'

if Saturday in a or Sunday in a:
    print('YES')

else:
    print('NO')'''

'''city1 = input()
city2 = input()
city3 = input()

maximum = max(city1,city2,city3, key=len)
minimum = min(city1,city2,city3, key=len)
print(maximum)
print(minimum)'''

'''print(min(a,b,c))
print(max(a,b,c))'''

'''a, b, c, d, f = float(input()), float(input()), float(input()),float(input()),float(input())


bb = abs(a) + abs(b) + abs(c) + abs(d) + abs(f)
print(bb)'''

'''a = int(input())

one = a // 100 % 10
two = a // 10 % 10
three = a % 10

minimum = min(one,two,three)
maximum = max(one,two,three)
average = (one + two + three) - ((max(one,two,three) + (min(one,two,three))))

subtraction = maximum - minimum

if subtraction == average:
    print('Число интересное')
else:
    print('Число неинтересное')'''

'''a, b, c = int(input()), int(input()), int(input())

print(f'{max(a,b,c)}')
print((a + b + c) - ((max(a,b,c) + (min(a,b,c)))))
print(f'{min(a,b,c)}')'''

'''a, b, c, d, f = int(input()), int(input()), int(input()), int(input()), int(input())

print(f'Наименьшее число = {min({a, b, c, d, f})}')
print(f'Наибольшее число = {max(a, b, c, d, f)}')'''

'''y = float(input())

y= y % 1 / 1
print(y)'''

'''y = float(input())

y = y * 10
print(int(y % 10))'''

'''years = int(input())

if years < 3:
    years *= 10.5
    if years % 1 != 0:
        print(years)
    else:
        print(round(years))

elif years > 2:
    years = (years -2) *4 +21
    print(years)'''

'''f = float(input())

c = 5/9*(f - 32)

print(c)'''

'''a = float(input())


f = 0
if a != 0:
    f  = (a) ** -1
    print(f)
else:
    print('Обратного числа не существует')'''

'''s = float(input())
v1 = float(input())
v2 = float(input())



r = s/ (v1+ v2)
print(r)'''
