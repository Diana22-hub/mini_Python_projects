import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
             break
        else:  
            print("It must be between 1 and 4 players.")        
    else:
        print("Try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_indx in range(players):
        print("n\Player player_indx + 1's turn.")
        print("Current_score: ", player_scores[player_indx], "\n")
        current_score = 0

    while True:
        should_roll = input("Do you want to roll the dice? (y/n): ")
        if should_roll.lower() != 'y':
            print("Game over. Thanks for playing!")
            break
        
        value = roll()
        if value == 1:
            current_score = 0
            print("You rolled a 1! Turn over, no points added.")
        else:
            current_score += value
            print("you rolled a: ", value)

    print("Your score is: ", current_score)

player_scores[player_indx] += current_score
print("Ypour total score is: ", player_scores[player_indx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player ", winning_idx + 1, " wins with a score of ", max_score)