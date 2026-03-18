import random as r
def guess():
    print("\n============== Let's begin the Game !! ==============\n")
    num=r.randint(0,100)
    a=0
    while True:
        user=int(input("Enter your guess: "))
        a+=1
        if user>num:
            print("Lower")
        elif user<num:
            print("Higher")
        else:
            print("You cracked it in",a,"attempts!!")
            print("The no. was", num)
            break

    ch=input("Do you want to continue(y/n): ").lower()
    if ch=='y':
        guess()
    else:
        print("Thanks for playing.")
        return        
if __name__ == "__main__":
    guess()