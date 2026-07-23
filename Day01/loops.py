'''exercise 1: loops'''
for i in range(1,21):
    print(i)

'''exercise 2: with conditions '''
for i in range(1,21):
    if i % 2 == 0:
        print(i)

'''exercise 3: conditional loops'''
for i in range(1,21):
    if i % 2 == 1:
        print(i,"is odd number")

'''exercise 4: table loops'''
for i in range(1,11):
    print("7 x",i,"=",7*i)

'''exercise 5: sumof numbers loops'''
sum = 0
for i in range(1,101):
    sum += i
print("Sum of numbers from 1 to 100 is:", sum)


'''exercise 6: print pattern loops'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

'''exercise 7: guessing game loops'''
for i in range(1,6):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == 7:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Sorry, try again.")