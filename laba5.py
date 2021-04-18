#1

class Sphere:
    def __init__(self, radius = 1, x = 0, y = 0, z = 0):
        self.radius = int(radius)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def get_volume(self):
        return 4/3*3.14*self.radius**2
    def get_square(self):
        return 4*3.14*self.radius**2
    def get_radius(self):
        return self.radius
    def get_center(self):
        return (self.x, self.y, self.z)
    
    def set_radius(self, radius):
        self.radius = int(radius)
    def set_center(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def is_point_inside(self, x, y, z):
        if self.x < x and self.y < y and self.z < z:
            return True
        else:
            return False

#2
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def getXY(self):
        return [self.x, self.y]
    
    def Show(self):
        print(str(self.x) + ' ' + str(self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

p1 = Point(3, 4)
print(str(p1.getXY()))
p1.Show()
#3
p2 = Point(7, 6)
p3 = p1 + p2
print('add:')
p3.Show()

#4
p3 = p1 / p2
print('div:')
p3.Show()

p3 = p1 * p2
print("mul:")
p3.Show()
p3 = p1 - p2
print('sub:')
p3.Show()
print(str(p1 == p2))

#5
class Drob:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y
    def normalize(self):
        if abs(self.y) > abs(self.x):
            for i in range(2, abs(self.x) + 1):
                while self.x % i == 0 and self.y % i == 0:
                    self.x /= i
                    self.y /= i
        elif abs(self.x) > abs(self.y):
            for i in range(2, abs(self.y) + 1):
                while self.x % i == 0 and self.y % i == 0:
                    self.x /= i
                    self.y /= i
        else:
            self.x = 1
            self.y = 1
    def print(self):
        print(str(int(self.x)) + '/' + str(int(self.y)))
    def __add__(self, other):
        d3 = Drob(int(self.x*other.y + other.x*self.y), int(self.y * other.y))
        return d3
    def __sub__(self, other):
        d3 = Drob(int(self.x*other.y - other.x*self.y), int(self.y * other.y))
        return d3
    def __mul__(self, other):
        d3 = Drob(int(self.x * other.x), int(self.y * other.y))
        return d3
    def __truediv__(self, other):
        d3 = Drob(int(self.x * other.y), int(self.y * other.x))
        return d3
    def __lt__(self, other): 
        if self.x / self.y < other.x / other.y:
            return True
        else:
            return False
    def __le__(self, other):
        if self.x / self.y <= other.x / other.y:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.x / self.y == other.x / other.y:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.x / self.y > other.x / other.y:
            return True
        else:
            return False
    def __ge__(self, other): 
        if self.x / self.y >= other.x / other.y:
            return True
        else:
            return False
d1 = Drob(3, 9)
d1.normalize()
d1.print()
d2 = Drob(4, 6)
d2.normalize()
d2.print()
d3 = d1 + d2
d3.normalize()
print('Сумма дробей:')
d3.print()
d3 = d1 - d2
d3.normalize()
print('Разность дробей:')
d3.print()

d3 = d1 / d2
d3.normalize()
print('Частное дробей:')
d3.print()

d3 = d1 * d2
d3.normalize()
print('Проивзедение дробей:')
d3.print()
print('Сравнение дробей d1 и d2:')
d1.print()
d2.print()
print('d1 > d2: ' + str(d1 > d2))
print('d1 >= d2: ' + str(d1 >= d2))
print('d1 < d2: ' + str(d1 < d2))
print('d1 <= d2: ' + str(d1 <= d2))
print('d1 == d2: ' + str(d1 == d2))
#6
class Snow:
    def __init__(self, n):
        self.n = int(n)
    def __add__(self, other):
        return Snow(self.n + other.n)
    
    def __sub__(self, other):
        return Snow(self.n - other.n)
    def __mul__(self, other):
        return Snow(self.n * other.n)
    def __truediv__(self, other):
        return Snow(round(self.n / other.n))
    def makeSnow(self, n):
        buf = '*'*n + '\n'
        return buf*n
s1 = Snow(9)
s2 = Snow(5)
s3 = s1 / s2
print(str(s3.n))
print(s3.makeSnow(5))

#7
class Human:
    default_name = 'Maksimka'
    default_age = 18

    def __init__(self, name = default_name, age = default_age, __money = 0, __property = ''):
        self.age = age
        self.name = name
        self.__money = __money
        self.__property = __property

    def info(self):
        print([self.name, self.age, self.__money, self.__property])

    def default_info(self):
        print([self.default_name, self.default_age])

    def __make_deal(self, bought):
        for i in range(len(bought)):
            if bought[i] == ' ':
                self.__money -= int(bought[i : len(bought)+1])
                print("Успешная покупка !!!")

    def earn_money(self, earned):
        self.__money += earned
    
    def buy(self, title, price):
        if self.__money < price:
            print('Недостаточно средств !!!')
        else:
            self.__make_deal(str(title) +' ' +  str(price))
    
    def __iadd__(self, other):
        self.__money += other
        return self
    def __isub__(self, other):
        self.__money -= other
        return self
    def __imul__(self, other):
        self.__money *= other
        return self
    def __itruediv__(self, other):
        self.__money = int(self.__money / other)
        return self

h1 = Human('Ivan', 18, 1800, 'car')
h2 = Human('Maksimka', 27, 113, '')

h1.info()
h2.earn_money(20)
h1.buy('chess', 100)
h2.buy('car', 150)
h2 += 100
h2.buy('car', 150)
h1 /= 10
h1.info()
