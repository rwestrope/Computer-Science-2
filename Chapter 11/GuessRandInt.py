import random
guess = False
correct_num = random.randint(1, 100)


def number_guess(num):
    global guess, correct_num
    
    

    if num == correct_num:
        print("good job, thats right")
        guess = True
    elif num < correct_num:
        print("bad job, that's too low")
    elif num > correct_num:
        print("bad job, that's too high")
    
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    # Convert the string tokens into integers
    while guess == False:

        user_input = int(input("guess a number"))
        number_guess(user_input)



    #tokens = user_input.split()
    #for token in tokens:
    #    num = int(token)
    #    number_guess(num)