# from random import randint
# print("Welcome to Rock Paper Scissors Game!")
# computer_score = 0
# player_score = 0

# while computer_score < 2 and player_score < 2:
#     print(
#         f"computer score is {computer_score} and Your score is {player_score}")
#     player = input("Enter your play ")
#     rand_num = randint(0, 2)
#     if rand_num == 0:
#         computer_choice = "rock"
#     elif rand_num == 1:
#         computer_choice = "paper"
#     else:
#         computer_choice = "scissors"

#     print(f"the computer plays {computer_choice}")
#     if player == computer_choice:
#         print("it's a draw")
#     elif player == "rock" and computer_choice == "scissors":
#         print("You win!")
#         player_score += 1
#     elif player == "paper" and computer_choice == "rock":
#         print("You win")
#         player_score += 1
#     elif player == "scissors" and computer_choice == "paper":
#         print("you win")
#         player_score += 1
#     else:
#         print("Computer Wins!")
#         computer_score += 1

# print(
#     f"final score of computer is {computer_score} and final score of user is {player_score}")
# if computer_score > player_score:
#     print("Computer wins final round")
# else:
#     print("You win final round")


from random import randint

print('Welcome to the Rock Paper Scissors Game')
print('You need to win at least 2 game to win the tournament!')
print('Best of Luck')

player_wins = 0
computer_wins = 0
computer_choice = ""

while player_wins < 2 and computer_wins < 2:
    rand_num = randint(0, 2)
    player_choice = input("enter your move! Rock Paper or Scissors ").upper()
    if rand_num == 0:
        computer_choice == "paper"
    elif rand_num == 1:
        computer_choice == "rock"
    else:
        computer_choice == "scissors"

    if player_choice == computer_choice:
        print("its a tie!")

    elif player_choice == "rock" and computer_choice == "scissors":
        print("you win")
        player_wins += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("you win")
        player_wins += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("you win")
        player_wins += 1
    else:
        print("Conputer wins")
        computer_wins += 1
    print(
        f"TIll now the  score of computer is {computer_wins} and the score of user is {player_wins}")
print(
    f"final score of computer is {computer_wins} and final score of user is {player_wins}")
if computer_wins > player_wins:
    print("Computer wins final round")
else:
    print("You win final round")
