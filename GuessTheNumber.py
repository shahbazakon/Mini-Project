import random 
print("This Program Create a random Number b/w '1 to 99' \n you have to guess What is It ")
n = random.randint(1,99)
guess = int(input("Enter an integer from 1 to 99 : "))
while(True):

                if guess<n:
                                print("Guess is low ")
                                guess = int(input("Enter an integer from 1 to 99 : "))
                elif guess>n:
                                print("Guess is Highe")
                                guess = int(input("Enter an integer from 1 to 99 : "))
                else:
                                print("Congratulation! You Guess It, it is ", +n)
                                break
