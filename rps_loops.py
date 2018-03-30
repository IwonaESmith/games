from random import randint
player_wins = 0
computer_wins = 0
winning_score = 5
while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player score: {player_wins} Compuer score: {computer_wins}")
	print("Rock...")
	print("Paper...")
	print("Scissors...")
	print("Player, make your move: ")
	
	player = input("(Enter your choice): ").lower()
	if player == "quit" or player == "q":

		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else: 
		computer = "scissors"
	print(f"Computer plays {computer}")
	 
	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "scissors":
			print("player wins!")
			player_wins +=1
		else:
			print("computer wins!")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("player wins!")
			player_wins +=1
		else:
			print("computer wins!")
			computer_wins += 1
	elif player == "scissors":
		if computer == "paper":
			print("player wins!")
			player_wins +=1
		else:
			print("computer wins!")
			computer_wins += 1	
	else:
		print("Please enter a valid move!")
if player_wins > computer_wins:
	print ("Congrats, you won")
elif player_wins == computer_wins:
	print(" It's a tie!")
else:
	print("oh, no Computer won!")
print(f"Final score ... Player score: {player_wins} Compuer score: {computer_wins}")