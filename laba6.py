from math import sqrt

# 1
result1 = []
number = int(input('1)enter a number: '))
generator1 = ([[x, y] for x in range(number - 1) if x < y] for y in range(1, number))
for i in generator1:
    result1.append(i)
print(result1)


# 2
def func2(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i


result2 = []
number = int(input('2)enter a number: '))
generator2 = func2(number)
for i in generator2:
    result2.append(i)
print(result2)


# 3
def func3():
    if len(result1) < 2 or len(result2) < 3:
        return None
    yield result1[0:2]
    yield result2[2:len(result2)]


print('3)')
for i in func3():
    print(i)


# 4
def func4():
    for i in result1:
        yield i


print('4)')
for i in func4():
    print(i)

# 7
file_name = input('7)Enter file name: ')
file = open(file_name)
result7 = 0
string = file.readline()
while string:
    for j in string:
        result7 += ord(j)
    result7 -= 10
    string = file.readline()
result7 += 10
file.close()
print(result7)
