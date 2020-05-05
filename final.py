#Title: Tic Tac Toe
#Topic: Combinatorics

from tkinter import *
import time
import random
import sys

#create pop-up canvas
tk = Tk()	
c = Canvas(tk, width=400, height=500)
tk.title("Tic-Tac-Toe")
c.pack()

# welcoming the user
c.create_text(200,250, text='Hello! What is your name?')
c.create_text(200,270, fill="gray", text="(Please type your answer into the command terminal)")
print('')
name = input("Hello! What is your name? ")
print('')
print('Hello, ',name,'! Lets play the game Tic-Tac-Toe!')
print('')
print('You can be X and Ill be O.')
print('')
c.delete(ALL)
c.create_text(200,250, text='Hello, '+name+'!')


def print_board():

	#clear canvas
	c.delete(ALL)

	#header
	c.create_text(200,50, text='To play Tic-Tac-Toe, you must get 3 in a row.', font=('chalkboard'))
	c.create_text(200,75, text='Your choices are defined, they must be 0 to 8.', font=('chalkboard'))

	#board
	c.create_line(150,150, 150,450)		#vertical
	c.create_line(250,150, 250,450)
	c.create_line(50,250, 350,250)		#horizontal
	c.create_line(50,350, 350,350)

	#labeling spaces on board
	global s0,s1,s2,s3,s4,s5,s6,s7,s8
	s0 = c.create_text(100,200, fill="gray", text='0', font='chalkboard')		#top row
	s1 = c.create_text(200,200, fill="gray", text='1', font='chalkboard')
	s2 = c.create_text(300,200, fill="gray", text='2', font='chalkboard')
	s3 = c.create_text(100,300, fill="gray", text='3', font='chalkboard')		#mid row
	s4 = c.create_text(200,300, fill="gray", text='4', font='chalkboard')
	s5 = c.create_text(300,300, fill="gray", text='5', font='chalkboard')
	s6 = c.create_text(100,400, fill="gray", text='6', font='chalkboard')		#bot row
	s7 = c.create_text(200,400, fill="gray", text='7', font='chalkboard')
	s8 = c.create_text(300,400, fill="gray", text='8', font='chalkboard')

def check_win(board):

	game = False
	
	if board[0]!='0' and board[1]!='0' and board[2]!='0' and board[3]!='0' and board[4]!='0' and board[5]!='0' and board[6]!='0' and board[7]!='0' and board[8]!='0':
		#its a tie
		game = True

	elif (board[0]=='O' and board[1]=='O' and board[2]=='O') or (board[0]=='O' and board[3]=='O' and board[6]=='O') or (board[0]=='O' and board[4]=='O' and board[8]=='O') or (board[1]=='O' and board[4]=='O' and board[7]=='O') or (board[2]=='O' and board[5]=='O' and board[8]=='O') or (board[2]=='O' and board[4]=='O' and board[6]=='O') or (board[3]=='O' and board[4]=='O' and board[5]=='O') or (board[6]=='O' and board[7]=='O' and board[8]=='O'):
		#computer wins
		game = True

	return game

def users_move(board):

	print('Your turn!')
	move = input('Choose a space to move to. ')
	i = int(move)
	if board[i] == '0':
		board[i] = 'X'	#update board
		board = board
		if move == '0':
			c.delete(s0)
			c.create_text(100,200, fill="blue", text='X', font=("chalkboard",40))
		elif move == '1':
			c.delete(s1)
			c.create_text(200,200, fill="blue", text='X', font=("chalkboard",40))
		elif move == '2':
			c.delete(s2)
			c.create_text(300,200, fill="blue", text='X', font=("chalkboard",40))
		elif move == '3':
			c.delete(s3)
			c.create_text(100,300, fill="blue", text='X', font=("chalkboard",40))
		elif move == '4':
			c.delete(s4)
			c.create_text(200,300, fill="blue", text='X', font=("chalkboard",40))
		elif move == '5':
			c.delete(s5)
			c.create_text(300,300, fill="blue", text='X', font=("chalkboard",40))
		elif move == '6':
			c.delete(s6)
			c.create_text(100,400, fill="blue", text='X', font=("chalkboard",40))
		elif move == '7':
			c.delete(s7)
			c.create_text(200,400, fill="blue", text='X', font=("chalkboard",40))
		elif move == '8':
			c.delete(s8)
			c.create_text(300,400, fill="blue", text='X', font=("chalkboard",40))
		else:
			print('Please choose a number from 0 to 8.')
	else:
		print('A move was already made at that space.')
		users_move()

	return board


def corner(board):

	space = 9
	for i in range(0,9):
		if  board[i]=='0':
			if i%2==0:
				space = i
				break

	move = str(space)
	bots_move(board,move)

def side(board):

	space = 9
	for i in range(0,9):
		if board[i]=='0':
			if i%2!=0 and i!=5:
				space = i
				break

	move = str(space)
	bots_move(board,move)

def middle(board):

	bots_move(board,'4')

def bots_move(board,move):

	i = int(move)
	if board[i] == '0':
		board[i] = 'O'
		print('My turn: '+move)
		if move == '0':
			c.delete(s0)
			c.create_text(100,200, fill="red", text='O', font=("chalkboard",40))
		elif move == '1':
			c.delete(s1)
			c.create_text(200,200, fill="red", text='O', font=("chalkboard",40))
		elif move == '2':
			c.delete(s2)
			c.create_text(300,200, fill="red", text='O', font=("chalkboard",40))
		elif move == '3':
			c.delete(s3)
			c.create_text(100,300, fill="red", text='O', font=("chalkboard",40))
		elif move == '4':
			c.delete(s4)
			c.create_text(200,300, fill="red", text='O', font=("chalkboard",40))
		elif move == '5':
			c.delete(s5)
			c.create_text(300,300, fill="red", text='O', font=("chalkboard",40))
		elif move == '6':
			c.delete(s6)
			c.create_text(100,400, fill="red", text='O', font=("chalkboard",40))
		elif move == '7':
			c.delete(s7)
			c.create_text(200,400, fill="red", text='O', font=("chalkboard",40))
		elif move == '8':
			c.delete(s8)
			c.create_text(300,400, fill="red", text='O', font=("chalkboard",40))
	
	return board

def bot_goes(board):

	#check if user went first and chose corner, bot should choose middle
	xcount=0
	ocount=0
	for i in range(0,9):
		if board[i]=='X':
			xcount = xcount+1
		elif board[i]=='O':
			ocount=ocount+1
	if xcount==1 and ocount==0 and board != ['0', '0', '0', '0', 'X', '0', '0', '0', '0']:
		middle(board)
	
	#check to win
	elif board[0]=='O' and board[1]=='O' and board[2]!='X':		#{0,1,2}
		bots_move(board,'2')
	elif board[0]=='O' and board[2]=='O' and board[1]!='X':
		bots_move(board,'1')
	elif board[1]=='O' and board[2]=='O' and board[0]!='X':
		bots_move(board,'0')
	elif board[0]=='O' and board[3]=='O' and board[6]!='X':	#{0,3,6}
		bots_move(board,'6')
	elif board[0]=='O' and board[6]=='O' and board[3]!='X':
		bots_move(board,'3')
	elif board[3]=='O' and board[6]=='O' and board[0]!='X':
		bots_move(board,'0')
	elif board[0]=='O' and board[4]=='O' and board[8]!='X':	#{0,4,8}
		bots_move(board,'8')
	elif board[0]=='O' and board[8]=='O' and board[4]!='X':
		bots_move(board,'4')
	elif board[4]=='O' and board[8]=='O' and board[0]!='X':
		bots_move(board,'0')
	elif board[1]=='O' and board[4]=='O' and board[7]!='X':	#{1,4,7}
		bots_move(board,'7')
	elif board[1]=='O' and board[7]=='O' and board[4]!='X':
		bots_move(board,'4')
	elif board[4]=='O' and board[7]=='O' and board[1]!='X':
		bots_move(board,'1')
	elif board[2]=='O' and board[5]=='O' and board[8]!='X':	#{2,5,8}
		bots_move(board,'8')
	elif board[2]=='O' and board[8]=='O' and board[5]!='X':
		bots_move(board,'5')
	elif board[5]=='O' and board[8]=='O' and board[2]!='X':
		bots_move(board,'2')
	elif board[2]=='O' and board[4]=='O' and board[6]!='X':	#{2,4,6}
		bots_move(board,'6')
	elif board[2]=='O' and board[6]=='O' and board[4]!='X':
		bots_move(board,'4')
	elif board[4]=='O' and board[6]=='O' and board[2]!='X':
		bots_move(board,'2')
	elif board[3]=='O' and board[4]=='O' and board[5]!='X':	#{3,4,5}
		bots_move(board,'5')
	elif board[3]=='O' and board[5]=='O' and board[4]!='X':
		bots_move(board,'4')
	elif board[4]=='O' and board[5]=='O' and board[3]!='X':
		bots_move(board,'3')
	elif board[6]=='O' and board[7]=='O' and board[8]!='X':	#{6,7,8}
		bots_move(board,'8')
	elif board[6]=='O' and board[8]=='O' and board[7]!='X':
		bots_move(board,'7')
	elif board[7]=='O' and board[8]=='O' and board[6]!='X':
		bots_move(board,'6')


	#check if you need to block
	elif board[0]=='X' and board[1]=='X' and board[2]!='O':	#{0,1,2}
		bots_move(board,'2')
	elif board[0]=='X' and board[2]=='X' and board[1]!='O':
		bots_move(board,'1')
	elif board[1]=='X' and board[2]=='X' and board[0]!='O':
		bots_move(board,'0')
	elif board[0]=='X' and board[3]=='X' and board[6]!='O':	#{0,3,6}
		bots_move(board,'6')
	elif board[0]=='X' and board[6]=='X' and board[3]!='O':
		bots_move(board,'3')
	elif board[3]=='X' and board[6]=='X' and board[0]!='O':
		bots_move(board,'0')
	elif board[0]=='X' and board[4]=='X' and board[8]!='O':	#{0,4,8}
		bots_move(board,'8')
	elif board[0]=='X' and board[8]=='X' and board[4]!='O':
		bots_move(board,'4')
	elif board[4]=='X' and board[8]=='X' and board[0]!='O':
		bots_move(board,'0')
	elif board[1]=='X' and board[4]=='X' and board[7]!='O':	#{1,4,7}
		bots_move(board,'7')
	elif board[1]=='X' and board[7]=='X' and board[4]!='O':
		bots_move(board,'4')
	elif board[4]=='X' and board[7]=='X' and board[1]!='O':
		bots_move(board,'1')
	elif board[2]=='X' and board[5]=='X' and board[8]!='O':	#{2,5,8}
		bots_move(board,'8')
	elif board[2]=='X' and board[8]=='X' and board[5]!='O':
		bots_move(board,'5')
	elif board[5]=='X' and board[8]=='X' and board[2]!='O':
		bots_move(board,'2')
	elif board[2]=='X' and board[4]=='X' and board[6]!='O':	#{2,4,6}
		bots_move(board,'6')
	elif board[2]=='X' and board[6]=='X' and board[4]!='O':
		bots_move(board,'4')
	elif board[4]=='X' and board[6]=='X' and board[2]!='O':
		bots_move(board,'2')
	elif board[3]=='X' and board[4]=='X' and board[5]!='O':	#{3,4,5}
		bots_move(board,'5')
	elif board[3]=='X' and board[5]=='X' and board[4]!='O':
		bots_move(board,'4')
	elif board[4]=='X' and board[5]=='X' and board[3]!='O':
		bots_move(board,'3')
	elif board[6]=='X' and board[7]=='X' and board[8]!='O':	#{6,7,8}
		bots_move(board,'8')
	elif board[6]=='X' and board[8]=='X' and board[7]!='O':
		bots_move(board,'7')
	elif board[7]=='X' and board[8]=='X' and board[6]!='O':
		bots_move(board,'6')

	#check if all corners and sides are taken
	elif board[0]!='0' and board[1]!='0' and board[2]!='0' and board[3]!='0' and board[5]!='0' and board[6]!='0' and board[7]!='0' and board[8]!='0':
		middle(board)

	#check if all corners are taken
	elif board[0]!='0' and board[2]!='0' and board[6]!='0' and board[8]!='0':
		side(board)

	else:
		corner(board)


#end the game
def endgame():

	c.delete(ALL)
	c.create_text(200,250, text="Good game!", fill='green')
	print('')
	print('')
	print('')
	print('Good game!')
	time.sleep(1)
	print('But notice how you didnt win...')
	time.sleep(1)
	print('')
	print('If you havent caught on by now...') 
	time.sleep(2)
	print('This game is programmed so that I always win or ends in a draw.')
	time.sleep(5)
	print('')
	print('The program takes into account the possible moves that you might make...')
	time.sleep(5)
	print('For example - lets say you decide to go first and you choose a corner.')
	time.sleep(5)
	print('')
	print('Then, I will always choose the middle as my first move to force a tie, or I will win if you somehow make a terrible mistake.')
	time.sleep(8)
	print('')
	print('However, if you decide to let me go first, I will always choose a corner for my first move...')
	time.sleep(8)
	print('')
	print('If I go first and choose to start in the corner, unless someone makes a terrible mistake, ')
	time.sleep(5)
	print('I will win if you choose a side or a corner, and we will tie if you choose the middle.')
	print('')
	time.sleep(5)
	print('Therefore, there is a 7/8 chance of winning if you start with a corner (so going first is definitely a big plus!).')
	time.sleep(8)
	print('')
	print('Now lets say I start in the center and you choose a side... There would now be a 4/8 (1/2) chance of me winning.')
	time.sleep(10)
	print('')
	print('4/8 odds are definitely decent, but not as good as the 7/8 odds of winning if I started in a corner.')
	time.sleep(5)
	print('')
	print('A better solution would be if I started in the center and you choose a corner...')
	time.sleep(4)
	print('Then, I could choose the opposite of that corner and have a 4/6 (2/3) chance of winning.')
	print('')
	time.sleep(4)
	print('Overall, you will have the best odds of winning Tic-Tac-Toe if you start in the corner!')
	time.sleep(5)
	print('')
	print('The lesson of this program is...')
	time.sleep(3)
	print('If your turn is first, you should start in the corner to have a 7/8 chance of winning.')
	time.sleep(5)
	print('If your turn is second and your opponent starts in the corner, you should start in middle to tie the game.')
	time.sleep(5)
	print('Hope you learned something from this and youre able to defeat your opponents in all future Tic-Tac-Toe matches!')
	time.sleep(5)

#begin the game		
def begin(): 
	
	board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']	#initial empty board
	gofirst = input('Would you like to go first? Yes or No: ')
	if gofirst == 'YES' or gofirst == 'yes' or gofirst=='Yes':
		print('')
		print('Awesome!')
		print('')
		print_board()
		while check_win(board) == False:
			users_move(board)
			bot_goes(board)
		
		print('')
		print('')
		print('')
		print('Good game!')
		again = input('Wanna play again? Yes or No: ')
		if again=='yes' or again=='Yes' or again=='YES':
			begin()
		else:
			endgame()
			
	elif gofirst == 'NO' or gofirst == 'no' or gofirst=='No':
		print('')
		print('Ok! Ill go first.')
		print('')
		print_board()
		while check_win(board) == False:
			bot_goes(board)
			if check_win(board) == False:
				users_move(board)
			else:
				break

		print('')
		print('')
		print('')
		print('Good game!')
		again = input('Wanna play again? Yes or No: ')
		if again=='yes' or again=='Yes' or again=='YES':
			begin()
		else:
			endgame()
		
		
begin()


