import random
def game():
    print("Hello! What is your name?")
    name = input()
    print("Well, ", name,", I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    cnt = 0
    while(True):
        print("Take a guess.")
        a = int(input())
        cnt+=1
        if(a < num):
            print("Your guess is too low.")
        elif(a > num):
            print("Your guess is too high.")
        else:
            print("Good job, ",name,"! You guessed my number in ",cnt," guesses!")
            return
game()
