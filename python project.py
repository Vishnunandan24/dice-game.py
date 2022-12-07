import random
while True:
    user_count=0
    computer_count=0
    print("welcome to dice game")
    play=int(input("how many times do you want to play from 1 to 6: "))
    user_play=int(input('''
    press 1 to start the game
    press 2 to exit'''))
    if user_play==1:
        for r in range(play):
            user=int(input("Enter the value:"))
            c=random.randint(1,6)
            if user==c:
                print("match draw")

                user_count+=1
                computer_count +=1
            elif user>c:
                print("Congratulation you won")
                user_count+=1
            else:
                print("you loose")
                computer_count+=1
        if computer_count==user_count:
            print("final match is draw")
            print("your points:",user_count)
            print("computer points:",computer_count)
        elif computer_count >user_count:
            print("try again! final match you loose:")
            print("your points:",user_count)
            print("computer points:",computer_count)
        else:
            print("Congatulation you won")
            print("your points:",user_count)
            print("computer points:",computer_count)
    else:
        break




