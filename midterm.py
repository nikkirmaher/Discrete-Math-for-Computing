# Title: Towers of Hanoi 
# Topic: Recursion
# Objective: Move all discs from Peg A to Peg C one over the other in decreasing order.
# Rules: The discs can only be moved one at a time. You cannot place a larger disc on top of a smaller disc.


# welcoming the user
print('')
name = input("Hello! What is your name? ")


#animation 
from tkinter import * #imports everything from tkinterface library
import time

tk = Tk() #object initializes Tk system
canvas = Canvas(tk, width=800, height=500) #canvas to draw on
tk.title("Towers of Hanoi") #title at the top of the window
canvas.pack() #tells it we are done configuring the settings

welcome = canvas.create_text(400, 25, text='Hello, '+name+'! Welcome to the Towers of Hanoi puzzle!')
objective = canvas.create_text(400, 50, text='Objective: Move all discs from Peg A to Peg C one over the other in decreasing order.')
rules = canvas.create_text(400, 75, text='Rules: The discs can only be moved one at a time. You cannot place a larger disc on top of a smaller disc.')
start = canvas.create_text(400, 100, text='Good Luck!')

print('')
print('Hello, ',name,'! Lets begin the game. Refer to the pop-up screen and type your moves into the command terminal.')
print('')


n = 1

while n>0:

# LEVEL 1
	print('LEVEL 1')
	if n==1:
		canvas.create_line(0,350, 800,350) #creates line for base of game
		canvas.create_rectangle(200,350, 220,200) #creating peg A
		canvas.create_rectangle(390,350, 410,200) #creating peg B
		canvas.create_rectangle(600,350, 620,200) #creating peg C
		titleA = canvas.create_text(210,360, text='A')
		titleB = canvas.create_text(400,360, text='B')
		titleC = canvas.create_text(610,360, text='C')

		disc1 = canvas.create_oval(190,350, 230,340, fill="red") #creating first disc on peg A
		level = canvas.create_text(400, 150, font='bold', text='LEVEL 1')

		n1step1a = canvas.create_text(50, 400, text='Move disc ')
		print('')
		n1step1a = input('Move disc ')
		if n1step1a == '1':
			n1step1b = canvas.create_text(150, 400, text='1 from peg A to peg ')
			n1step1b = input('1 from peg A to peg ')
			if n1step1b == 'C':
				n1step1c = canvas.create_text(220,400, text='C')
				#move the disc
				canvas.move(disc1, 400, 0)
				n=n+1


			else:
				# reset the puzzle to let player try again
				canvas.delete(ALL)
				tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
				n=1
		else:
			# reset the puzzle to let player try again
			canvas.delete(ALL)
			tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
			n=1

# LEVEL 2
	if n==2:
		print('LEVEL 2')
		canvas.delete(ALL)
		canvas.create_line(0,350, 800,350) #creates line for base of game
		canvas.create_rectangle(200,350, 220,200) #creating peg A
		canvas.create_rectangle(390,350, 410,200) #creating peg B
		canvas.create_rectangle(600,350, 620,200) #creating peg C
		titleA = canvas.create_text(210,360, text='A')
		titleB = canvas.create_text(400,360, text='B')
		titleC = canvas.create_text(610,360, text='C')

		start = canvas.create_text(400, 100, text='Nice work!')
		level = canvas.create_text(400, 150, font='bold',text='LEVEL 2')

		disc1 = canvas.create_oval(190,340, 230,330, fill="red") #creating first disc on peg A
		disc2 = canvas.create_oval(180,350, 240,340, fill="orange") #creating second disc on peg A
		
		n2step1a = canvas.create_text(50, 400, text='Move disc ')
		print('')
		n2step1a = input('Move disc ')
		if n2step1a == '1':
			n2step1b = canvas.create_text(150, 400, text='1 from peg A to peg ')
			n2step1b = input('1 from peg A to peg ')
			if n2step1b == 'B':
				n2step1c = canvas.create_text(220,400, text='B')
				#move disc1 from A to B
				canvas.move(disc1, 190, 0)
				n2step2a = canvas.create_text(50, 420, text='Move disc ')
				n2step2a = input('Move disc ')
				if n2step2a == '2':
					n2step2b = canvas.create_text(150, 420, text='2 from peg A to peg ')
					n2step2b = input('2 from peg A to peg ')
					if n2step2b == 'C':
						n2step2c = canvas.create_text(220,420, text='C')
						#move disc2 from A to C
						canvas.move(disc2, 400, 0)
						n2step3a = canvas.create_text(50, 440, text='Move disc ')
						n2step3a = input('Move disc ')
						if n2step3a == '1':
							n2step3b = canvas.create_text(150, 440, text='1 from peg B to peg ')
							n2step3b = input('1 from peg B to peg ')
							if n2step3b == 'C':
								n2step3c = canvas.create_text(220,440, text='C')
								#move disc2 from A to C
								canvas.move(disc1, 200, 0)
								n=n+1

							else:
								# reset the puzzle to let player try again
								canvas.delete(ALL)
								tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
								n=1
						else:
							# reset the puzzle to let player try again
							canvas.delete(ALL)
							tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
							n=1
					else:
						# reset the puzzle to let player try again
						canvas.delete(ALL)
						tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
						n=1
				else:
					# reset the puzzle to let player try again
					canvas.delete(ALL)
					tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
					n=1
			else:
				# reset the puzzle to let player try again
				canvas.delete(ALL)
				tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
				n=1
		else:
			# reset the puzzle to let player try again
			canvas.delete(ALL)
			tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
			n=1

# LEVEL 3	
	elif n==3:
		print('LEVEL 3')
		canvas.delete(ALL)
		level = canvas.create_text(400, 150, fill="black", font='bold',text='LEVEL 3')
		canvas.create_line(0,350, 800,350) #creates line for base of game
		canvas.create_rectangle(200,350, 220,200) #creating peg A
		canvas.create_rectangle(390,350, 410,200) #creating peg B
		canvas.create_rectangle(600,350, 620,200) #creating peg C
		titleA = canvas.create_text(210,360, text='A')
		titleB = canvas.create_text(400,360, text='B')
		titleC = canvas.create_text(610,360, text='C')

		start = canvas.create_text(400, 100, text='Nice work!')
		level = canvas.create_text(400, 150, font='bold',text='LEVEL 3')

		disc1 = canvas.create_oval(190,320, 230,330, fill="red") #creating first disc on peg A
		disc2 = canvas.create_oval(180,330, 240,340, fill="orange") #creating second disc on peg A
		disc3 = canvas.create_oval(170,340, 250,350, fill="yellow") #creating second disc on peg A

		n3step1a = canvas.create_text(50, 380, text='Move disc ') #step1
		print('')
		n3step1a = input('Move disc ')
		if n3step1a == '1': 
			n3step1b = canvas.create_text(150, 380, text='1 from peg A to peg ')
			n3step1b = input('1 from peg A to peg ')
			if n3step1b == 'C':
				n3step1c = canvas.create_text(220,380, text='C')
				#move disc1 from A to C
				canvas.move(disc1, 400, 0)
				n3step2a = canvas.create_text(50, 400, text='Move disc ')	#step2
				n3step2a = input('Move disc ')
				if n3step2a == '2':
					n3step2b = canvas.create_text(150, 400, text='2 from peg A to peg ')
					n3step2b = input('2 from peg A to peg ')
					if n3step2b == 'B':
						n3step2c = canvas.create_text(220,400, text='B')
						#move disc2 from A to B
						canvas.move(disc2, 190, 0)
						n3step3a = canvas.create_text(50, 420, text='Move disc ')	#step3
						n3step3a = input('Move disc ')
						if n3step3a == '1':
							n3step3b = canvas.create_text(150, 420, text='1 from peg C to peg ')
							n3step3b = input('1 from peg C to peg ')
							if n3step3b == 'B':
								n3step3c = canvas.create_text(220,420, text='B')
								#move disc1 from C to B
								canvas.delete(disc1) 
								disc1 = canvas.create_oval(380,320, 420,330, fill="red") #creating first disc on peg C
								n3step4a = canvas.create_text(50, 440, text='Move disc ')	#step4
								n3step4a = input('Move disc ')
								if n3step4a == '3':
									n3step4b = canvas.create_text(150, 440, text='3 from peg A to peg ')
									n3step4b = input('3 from peg A to peg ')
									if n3step4b == 'C':
										n3step4c = canvas.create_text(220,440, text='C')
										#move disc3 from A to C
										canvas.move(disc3, 400, 0)
										n3step5a = canvas.create_text(50, 460, text='Move disc ')	#step5
										n3step5a = input('Move disc ')
										if n3step5a == '1':
											n3step5b = canvas.create_text(150, 460, text='1 from peg B to peg ')
											n3step5b = input('1 from peg B to peg ')
											if n3step5b == 'A':
												n3step5c = canvas.create_text(220,460, text='A')
												#move disc1 from B to A
												canvas.delete(disc1)
												disc1 = canvas.create_oval(190,320, 230,330, fill="red")
												n3step6a = canvas.create_text(50, 480, text='Move disc ')	#step6
												n3step6a = input('Move disc ')
												if n3step6a == '2':
													n3step6b = canvas.create_text(150, 480, text='2 from peg B to peg ')
													n3step6b = input('2 from peg B to peg ')
													if n3step6b == 'C':
														n3step6c = canvas.create_text(220,480, text='C')
														#move disc2 from B to C
														canvas.move(disc2, 210, 0)
														n3step7a = canvas.create_text(50, 500, text='Move disc ')	#step7
														n3step7a = input('Move disc ')
														if n3step7a == '1':
															n3step7b = canvas.create_text(150, 500, text='1 from peg A to peg ')
															n3step7b = input('1 from peg A to peg ')
															if n3step7b == 'C':
																n3step7c = canvas.create_text(220,500, text='C')
																#move disc1 from A to C
																canvas.move(disc1, 420, 0)

																# FINISHED
																n=0
																canvas.delete(ALL)
																finished = canvas.create_text(400, 250, fill = "green", text='Great Job!')


															else:
																# reset the puzzle to let player try again
																canvas.delete(ALL)
																tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
																n=1
														else:
															# reset the puzzle to let player try again
															canvas.delete(ALL)
															tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
															n=1
													else:
														# reset the puzzle to let player try again
														canvas.delete(ALL)
														tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
														n=1
												else:
													# reset the puzzle to let player try again
													canvas.delete(ALL)
													tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
													n=1
											else:
												# reset the puzzle to let player try again
												canvas.delete(ALL)
												tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
												n=1
										else:
											# reset the puzzle to let player try again
											canvas.delete(ALL)
											tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
											n=1

									else:
										# reset the puzzle to let player try again
										canvas.delete(ALL)
										tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
										n=1
								else:
									# reset the puzzle to let player try again
									canvas.delete(ALL)
									tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
									n=1
							else:
								# reset the puzzle to let player try again
								canvas.delete(ALL)
								tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
								n=1
						else:
							# reset the puzzle to let player try again
							canvas.delete(ALL)
							tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
							n=1
					else:
						# reset the puzzle to let player try again
						canvas.delete(ALL)
						tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
						n=1
				else:
					# reset the puzzle to let player try again
					canvas.delete(ALL)
					tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
					n=1
			else:
				# reset the puzzle to let player try again
				canvas.delete(ALL)
				tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
				n=1
		else:
			# reset the puzzle to let player try again
			canvas.delete(ALL)
			tryagain = canvas.create_text(400, 175, text='Not quite. Try again!')
			n=1

print('Great Job!')
print('')
print('')
print('')
print('---------------------')
print('')
print('Now that youve got the hang of the game, lets look at the Towers of Hanoi as a simple recursive problem.')
print('')
print('We can determine the number of steps it will take to sort a Tower of Hanoi puzzle with any number of discs!')
print('')
n = int(input('Give a number of discs you want to solve for: '))
print('')

#The number of moves it should take to move a tower with n disks should be 2^n - 1
from math import pow
count = int(pow(2,n) - 1)
print('A Tower of Hanoi puzzle with ',n, ' discs should take ',count,' moves to solve.')
print('')

def hanoi(n, A, C, B): 
    if n == 1: 
        print('Move disc 1 from peg ',A,' to peg ',C)
        return
    else:
	    hanoi(n-1, A, B, C) 
	    print('Move disc',n,'from peg ',A,' to peg ',C)
	    hanoi(n-1, B, C, A)

hanoi(n=n, A="A", C="C", B="B") 
print('')

#END OF PROGRAM
	    




	





















