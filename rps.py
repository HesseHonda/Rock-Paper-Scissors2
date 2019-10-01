#name
#rock paper scissors
# Varibles
import random
pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]
#Welcome Massage
# print the message
print("Welcome to the game, prove yourself and become a god in rock paper scissors")
# prompt for player name
pName = input("what is your mortal name? ")

#game Loop

#Final Score
def printScore():
	print("The score is: ")
	print(pName + ": " + str(pScore))
	print("Computer: " + str(cScore))
	print("Ties: " + str(ties))
# Write Message
# Write player score
# write computer score
# write how many ties

# Game Loop
# Make a forever loop
while True:
	# Print current score
	printScore()
	# prompt for a choice (r (rock), p (paper), s(scissors), q(quit))
	pChoice = input("Enter r (rock), p (paper), s (scissors) or q (to quit): ")
	# get computers choice
	if pChoice == "q":
		break
	cChoice = random.choice(computerChoices)
	# Compare for player entering r
	if pChoice == "r":
		print(pName + " picked Rock")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		# if computer is p
		elif cChoice == "p":
			print("Computer picked Paper")
			print("Paper covers Rock")
			cScore = cScore + 1
		# if computer is s
		else:
			print("Computer picked Scissors")
			print("Rock Breaks Scissors")
			pScore = pScore + 1
	# Compare fro player entering p
	elif pChoice =="p":
		print(pName + " picked Paper")
		if cChoice == "r":
			print("Computer picked Rock")
			print("Paper covers Rock")
			pScore = pScore + 1
		elif cChoice =="p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		else:
			print("Computer picked Scissors")
			print("Scissors cut paper")
			cScore = cScore + 1
		
	# Compare for player entering s
	elif pChoice == "s":
		print(pName + " picked Scissors")
		if cChoice == "r":
			print("Computer picked Rock")
			print("Rock breaks Scissors")
			cScore = cScore + 1
		elif cChoice =="p":
			print("Computer picked Paper")
			print("Scissors cuts Paper")
			pScore = pScore + 1
		else:
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
		
	# deal with palyer entering q
	# deal with entering anything else