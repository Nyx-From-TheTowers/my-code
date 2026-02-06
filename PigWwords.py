import random

word_opt = ("Nerdy Nerd", "Whaskly Gambler", "Goofy Goober", "Peanut", "Ively Wannabe")

word_options = (word_opt[random.randint(0, len(word_opt))])

def roll():
    min_roll = 1
    max_roll = 6
    roll = random.randint(min_roll, max_roll)
    return roll

while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("https://www.youtube.com/watch?v=KOs9caqQVig&pp=ygUTbnVoIHVoIHNvdW5kIGVmZmVjdA%3D%3D")
    else:
        print("https://www.youtube.com/watch?v=KOs9caqQVig&pp=ygUTbnVoIHVoIHNvdW5kIGVmZmVjdA%3D%3D")
print("Players Assembled")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer", player_index + 1, "turn has begun!")
        print("Your total score this round is", player_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("would you like to roll? (y) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("A One was rolled! Points Lost!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled", value,".  Added to score!")

        print("Current score is", current_score)
    
        player_scores[player_index] += current_score
        print("Total score is", player_scores[player_index])

max_score = max(player_scores)
low_score = min(player_scores)
winning_idx = player_scores.index(max_score)
losing_idx = player_scores.index(low_score)
print("\nPlayer", winning_idx +1, "Is the winner with a score of", max_score)
print("Player", losing_idx +1, "Is a", word_options, "\n")