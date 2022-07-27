import random
import time
def start():
	input("START THE GAME, PRESS ENTER\n")
def rule():
	print("RULE: THERE WILL BE 2 PLAYERS IN THIS GAME, ONE IS YOU AND THE OTHER IS BOT\nTHE GAME IS BASED ON ADDING NUMBERS\nONE OF THE PLAYER WILL WRITE A NUMBER BETWEEN 1 AND 10\nTHE OTHER PLAYER WILL DO THE SAME\nNUMBERS WILL BE ADDED ON EACH TURN OF BOTH THE PLAYERS\nTHE PLAYER ON WHOSE NUMBER IS ADDED AND RESULTS 100 IS THE WINNER\n\n")
def normal():
	num = 0
	while num <= 100:
		sub = int(input("PLAYER 1, ENTER: "))
		while sub < 1 or sub > 10 or sub + num > 100:
			sub = int(input("PLAYER 1, CHOOSE WISELY: "))
		num += sub
		print("TOTAL ==",num, "\n")
		if num == 100:
			print("PLAYER 1 WON THE GAME\n\n\nNOW SINCE YOU WON THE GAME, YOU MAY TRY THE IMPOSSIBLE MODE\n\nSTARTING IN 5 SECONDS")
			time.sleep(5)
			impossible()
			break
		dub = random.randrange(1,11)
		while dub + num > 100:
			dub = random.randrange(1, 101 - num)
		print("PLAYER 2, ENTER:", dub)
		num += dub
		print("TOTAL ==", num, "\n")
		print()
		if num == 100:
			print("PLAYER 2 WON THE GAME\n\n\nNOW SINCE YOU LOST THE GAME, YOU MAY WANT TO RETRY\n\nRESTARTING IN 5 SECONDS")
			time.sleep(5)
			normal()
			break
def impossible():
	num = 0
	while num <= 100:
		sub = int(input("PLAYER 1, ENTER:"))
		while sub < 1 or sub > 10 or sub + num > 100:
			sub = int(input("PLAYER 1, CHOOSE WISELY:"))
		num += sub
		print("TOTAL ==",num, "\n")
		if num == 100:
			print("PLAYER 1 WON THE GAME")
			break
		if num < 11:
			dub = 12 - sub
		elif num > 11:
			dub = 11 - sub
		print("PLAYER 2, ENTER:", dub)
		num += dub
		print("TOTAL ==", num, "\n")
		if num == 100:
			print("PLAYER 2 WON THE GAME")
			break
def mode_select():
	diff = input("For normal mode, enter 1\nFor Impossible mode, enter 2\nChoice: ")
	if diff == str(1):
		print("YOU CHOSE NORMAL MODE\nGAME STARTS IN 5 SECONDS\n")
		time.sleep(5)
		normal()
	elif diff == str(2):
		print("YOU CHOSE IMPOSSIBLE MODE\nGAME STARTS IN 5 SECONDS\n")
		time.sleep(5)
		impossible()
	else:
		print("PLEASE ENTER 1 OR 2\n")
		mode_select()
start()
rule()
mode_select()