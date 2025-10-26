name = input("Type your name: ")
print("Welcome to the adventure", name, "!")

answer = input("Your are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
        answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()
        if answer == "swim":
            print("You swam across and were eaten by an alligator. You lose.")
        elif answer == "walk":
            print("You walked for many miles, ran out of water and lost the game.")
        else:   
            print("Not a valid option. You lose.")
elif answer == "right":
        answer = input("You come to a bridge, it looks wobbly. Do you want to cross it or head back (cross/back)? ").lower()
        if answer == "cross":
            print("You crossed the bridge and found a treasure chest full of gold! You win!")
        elif answer == "back":
            print("You go back and lose.")
        else:   
            print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name)
   
      