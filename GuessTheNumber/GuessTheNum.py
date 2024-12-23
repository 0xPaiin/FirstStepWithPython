n = 57
no_of_guess = 10
while(no_of_guess != 0):
    print(f"Remaining number of guesses is : {no_of_guess}")
    no_of_guess -= 1
    user_input = int(input("Enter the number between 1 and 100: \n")) 
    if(user_input < n):
        print(f"{user_input} is less than the value")
        print("Please Try Again.")
    elif(user_input > n):
        print(f"{user_input} is greater than the value")
        print("Please Try Again.")
    elif (user_input == n):
        print(f"{user_input} is correct number.")
        print("Your guess was right !!")
        break
if(no_of_guess == 0 and user_input != n):
    print("Game Over!! You are out of guesses.")
