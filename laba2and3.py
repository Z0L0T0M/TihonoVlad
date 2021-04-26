'''
# 1, 2
def func1():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if a > b:
        print(str(a) + ' > ' + str(b))
    elif a < b:
        print(str(a) + ' < ' + str(b))
    else :
        print(str(a) + ' = ' + str(b))
func1()

# 3
def func3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    S = input("Enter string: ")
    i = 0
    buf = ''
    while 1:
        if i == len(S):
            break
        buf += S[i]
        if S[i] == '1' or S[i] == '2' or S[i] == '3' or S[i] == '4' or S[i] == '5' or S[i] == '6' or S[i] == '7' or S[i] == '8' or S[i] == '9' or S[i] == '0' and S[i+1]!=')' :
            buf += ' '
        i+=1
    S = buf
    print(S)
func3()

#4
def func4():
    j = 0
    spisok = '123456789'
    stroka1 = ''
    stroka2 = ''
    N = int(input("Введите число "))
    stroka3 = ' '*N + '1'
    print(stroka3)
    for i in range(1, N):
     if N<=1:
         break
     stroka1 += ' ' * (N - i)
     while len(stroka1)!=N+1:
         stroka1 = stroka1 + spisok[j]
         j = j + 1
     j = 0
    
     while len(stroka2)!=i:
         stroka2 = spisok[j] + stroka2
         j = j + 1
     j = 0
     print(stroka1+stroka2)
     stroka1 = ''
     stroka2 = ''
    
    n = N
    if N>1:
     for i in range(1, N):
         j = 0
         stroka1 = stroka1 + ' '*(j+1+i)
         while len(stroka1)!=N+1:
             stroka1 = stroka1 + spisok[j]
             j = j + 1
         j = 0
    
         while len(stroka2)!=n-2:
             stroka2 = spisok[j] + stroka2
             j = j + 1
         n=n-1
    
         print(stroka1+stroka2)
         stroka1 = ''
         stroka2 = ''
    stroka3 = ' '*N + '1' 
func4()
        

#8
def func8():
    number = int(input("Enter class number: "))
    if number > 0 and number < 5:
        print('1')
    elif number > 4 and number < 10:
        print('2')
    else:
        print('3')
func8()

#9
def func9():
    S = input("Enter string: ")
    for i in range(len(S)):
        print(ord(S[i]))
func9()

#10
def func10():
    S = input("Enter string: ")
    sum = 0
    for i in range(len(S)):
        sum += ord(S[i])
    print("Сумма кодовэлементов строки: " + str(sum))
func10()

#11
def func11():
    S = {4: '7', 7:'8', 1:'9', 2:'2', 5:'0',3:'1'}
    buf = []
    for k,v in S.items():
        buf.append(k)
    buf.sort()
    print([S[buf[i]] for i in range(len(buf))])
func11()

#12
def func12():
    S = [1, 2, 3, 5, 7, 8, 9, 11]
    x = int(input('Введите число: '))
    i = 0
    while i in range(len(S)):
        if i == x:
            print('число найдено!')
            break
        i+=1
    else:
        print('Число не найдено!')
func12()

#13
def func13():
    S = [1, 2, 3, 5, 7, 8, 9, 11]
    x = int(input('Введите число: '))
    for i in S:
        if i == x:
            print('число найдено!')
            break
    else:
        print('Число не найдено!')
func13()
'''  


        
        
        
        
        
    
    
