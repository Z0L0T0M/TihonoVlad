def game():
    print('GL and HF!')
    wordlist = input('Enter a word:')
    turns = 10
    buf = ['_' for i in range(len(wordlist))]
    copy = buf
    while turns > 0:
        missed = 0
        letter = input('enter a letter:')
        for l in range(len(wordlist)):
            if wordlist[l] == letter:
                buf[l] = letter
            else:
                missed += 1
        if missed == len(wordlist):
            turns -= 1
        print(buf)
        count = 0
        for i in range(len(buf)):
            if buf[i] == wordlist[i]:
                count += 1
            else:
                count -= 1
        if count == len(buf):
            print("U won!")
            return 1
        if turns == 9: print('             __ __ ')

        if turns == 8: print('''
           | 
           |
           |
           | 
         __|__ ''')

        if turns == 7: print('''
           _____ 
           | 
           |
           |
           | 
         __|__ ''')

        if turns == 6: print('''
           _____ 
           |   |
           |
           |
           | 
         __|__ ''')

        if turns == 5: print('''
           _____ 
           |   |
           |   O
           |
           | 
         __|__ ''')

        if turns == 4: print('''
           _____ 
           |   |
           |   O
           |   |
           | 
         __|__ ''')

        if turns == 3: print('''
           _____ 
           |   |
           |   O
           |  /|
           | 
         __|__ ''')

        if turns == 2: print('''
           _____ 
           |   |
           |   O
           |  /|\ 
           | 
         __|__ ''')

        if turns == 1: print('''
           _____ 
           |   |
           |   O
           |  /|\ 
           |  /
         __|__ ''')

        if turns == 0: print('''
           _____ 
           |   |
           |   O
           |  /|\ 
           |  / \ 
         __|__ ''')

        if turns == 0:
            print('\n\nThe answer is: ', wordlist)


game()
while 1:
    if (input('do u want to play again? (yes or no) ')).lower() == 'yes':
        game()
    else:
        break
