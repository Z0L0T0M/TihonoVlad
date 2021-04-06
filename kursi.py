L = ['a', 1, -2, 1.2,]
# 1
print([x for x in L if type(x) == int and x%2 == 0])

# 2
print(L[::2])

# 3
print([x for x in L if type(x) !=str and x > 0])

# 4
L = [1,3,4,7,9]
m = 3
print([{x for x in L if x % m == 0},{x for x in L if x % m == 1}])

# 5
D = {1: 2, 'a': 3, -1: 1, 3: 'a'}
print([x + y for x, y in D.items() if type(x) != str and type(y) != str])

#6
L = [3, 4.1, 2]
L.sort()
print([(L[i], L[j]) for i in range(len(L)-1) for j in range(i + 1, len(L))])

#7
L = ['a', 1, -2, 1.2,]
print({key:item for key, item in zip([i for i in L if L.index(i)%2 == 0], [i for i in L if L.index(i)%2 != 0])})
