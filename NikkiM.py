# Title: Towers of Hanoi 
# Topic: Recursion
# Objective: Move all discs from Peg A to Peg C one over the other in decreasing order.
# Rules: The discs can only be moved one at a time. You cannot place a larger disc on top of a smaller disc.


# welcoming the user
print('')
name = input("What is your name? ")
print('') # these blank lines have been added so the text is easier to read when compiled.
print('Hello, ' + name + '! Welcome to the Towers of Hanoi puzzle!')
print('')
print('This puzzle covers the Discrete Mathematics for Computing topic of Recursion!')
print('')
print('The objective of the puzzle is to move all discs from Peg A to Peg C one over the other in decreasing order.')
print('')
print('The discs can only be moved one at a time. You cannot place a larger disc on top of a smaller disc.')
print('')
print('If either of these rules are broken, you have lost the game and must start over.')
print('')
print('Good luck!')
print('')
print('')
print('')
print('')
print('')

n = 1

while n>0:

# LEVEL 1
	if n==1:

		print('LEVEL 1')
		print('')

		# sketch the towers with the discs
		print('     |     |     |')
		print('     |     |     |')
		print('     |     |     |')
		print('     |     |     |')
		print('     |     |     |')
		print('     1     |     |')
		print('---- A --- B --- C ----')
		print('')

		n1step1 = input('1. Move 1 from A to: ')
		if n1step1 == 'C':

			print('')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     1')
			print('---- A --- B --- C ----')
			print('')

			#puzzle solved correctly. increase n by 1 to move onto next level.
			print('Nice work! Moving on to next level...')
			print('')
			n=n+1

		else:
			# reset the puzzle to let player try again
			print('')
			print('TRY AGAIN')
			print('')
			n=1

# LEVEL 2
	if n==2:

		print('LEVEL 2')
		print('')

		# sketch the towers with the discs
		print('     |     |     |')
		print('     |     |     |')
		print('     |     |     |')
		print('     |     |     |')
		print('     1     |     |')
		print('    *2*    |     |')
		print('---- A --- B --- C ----')
		print('')

		#step 1
		n2step1 = input('1. Move 1 from A to: ')
		if n2step1 == 'B':

			print('')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('    *2*    1     |')
			print('---- A --- B --- C ----')
			print('')

			#step 2
			n2step2 = input('2. Move 2 from A to: ')
			if n2step2 == 'C':
				print('')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     1    *2*')
				print('---- A --- B --- C ----')
				print('')

				#step 3
				n2step3 = input('3. Move 1 from B to: ')
				if n2step3 == 'C':
						print('')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     1')
						print('     |     |    *2*')
						print('---- A --- B --- C ----')
						print('')

						print('Nice work! Moving on to next level...')
						print('')
						n=n+1
				else:
					print('')
					print('TRY AGAIN')
					print('')
					n=1
			else:
				print('')
				print('TRY AGAIN')
				print('')
				n=1
		else:
			print('')
			print('TRY AGAIN')
			print('')
			n=1

# LEVEL 3	
	elif n==3:

		print('LEVEL 3')
		print('')

		# sketch the towers with the discs
		print('     |     |     |')
		print('     |     |     |')
		print('     |     |     |')
		print('     1     |     |')
		print('    *2*    |     |')
		print('   **3**   |     |')
		print('---- A --- B --- C ----')
		print('')

		#step1
		n3step1 = input('1. Move 1 from A to: ')
		if n3step1 == 'C':

			print('')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('    *2*    |     |')
			print('   **3**   |     1')
			print('---- A --- B --- C ----')
			print('')

			#step2
			n3step2 = input('2. Move 2 from A to: ')
			if n3step2 == 'B':

				print('')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('   **3**  *2*    1')
				print('---- A --- B --- C ----')
				print('')

				#step3
				n3step3 = input('3. Move 1 from C to: ')
				if n3step3 == 'B':
						print('')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     1     |')
						print('   **3**  *2*    |')
						print('---- A --- B --- C ----')
						print('')

						#step4
						n3step4 = input('4. Move 3 from A to: ')
						if n3step4 == 'C':
							print('')
							print('     |     |     |')
							print('     |     |     |')
							print('     |     |     |')
							print('     |     |     |')
							print('     |     1     |')
							print('     |    *2*  **3**')
							print('---- A --- B --- C ----')
							print('')

							#step5
							n3step5 = input('5. Move 1 from B to: ')
							if n3step5 == 'A':
								print('')
								print('     |     |     |')
								print('     |     |     |')
								print('     |     |     |')
								print('     |     |     |')
								print('     |     |     |')
								print('     1    *2*  **3**')
								print('---- A --- B --- C ----')
								print('')

								#step6
								n3step6 = input('6. Move 2 from B to: ')
								if n3step6 == 'C':
									print('')
									print('     |     |     |')
									print('     |     |     |')
									print('     |     |     |')
									print('     |     |     |')
									print('     |     |    *2*')
									print('     1     |   **3**')
									print('---- A --- B --- C ----')
									print('')

									#step7
									n3step7 = input('7. Move 1 from A to: ')
									if n3step7 == 'C':
										print('')
										print('     |     |     |')
										print('     |     |     |')
										print('     |     |     |')
										print('     |     |     1')
										print('     |     |    *2*')
										print('     |     |   **3**')
										print('---- A --- B --- C ----')
										print('')
										print('Nice work! Moving on to the last level, youve got this!')
										n=n+1
										
									else:
										print('')
										print('TRY AGAIN')
										print('')
										n=1
								else:
									print('')
									print('TRY AGAIN')
									print('')
									n=1
							else:
								print('')
								print('TRY AGAIN')
								print('')
								n=1
						else:
							print('')
							print('TRY AGAIN')
							print('')
							n=1
				else:
					print('')
					print('TRY AGAIN')
					print('')
					n=1
			else:
				print('')
				print('TRY AGAIN')
				print('')
				n=1
		else:
				print('')
				print('TRY AGAIN')
				print('')
				n=1
# LEVEL 4	
	elif n==4:

		print('LEVEL 4')
		print('')

		# sketch the towers with the discs
		print('     |     |     |')
		print('     |     |     |')
		print('     1     |     |')
		print('    *2*    |     |')
		print('   **3**   |     |')
		print('  ***4***  |     |')
		print('---- A --- B --- C ----')
		print('')

		#step1
		n4step1 = input('1. Move 1 from A to: ')
		if n4step1 == 'B':

			print('')
			print('     |     |     |')
			print('     |     |     |')
			print('     |     |     |')
			print('    *2*    |     |')
			print('   **3**   |     |')
			print('  ***4***  1     |')
			print('---- A --- B --- C ----')
			print('')

			#step2
			n4step2 = input('2. Move 2 from A to: ')
			if n4step2 == 'C':

				print('')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('     |     |     |')
				print('   **3**   |     |')
				print('  ***4***  1    *2*')
				print('---- A --- B --- C ----')
				print('')

				#step3
				n4step3 = input('3. Move 1 from B to: ')
				if n4step3 == 'C':

					print('')
					print('     |     |     |')
					print('     |     |     |')
					print('     |     |     |')
					print('     |     |     |')
					print('   **3**   |     1')
					print('  ***4***  |    *2*')
					print('---- A --- B --- C ----')
					print('')

					#step4
					n4step4 = input('4. Move 3 from A to: ')
					if n4step4 == 'B':

						print('')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     |')
						print('     |     |     1')
						print('  ***4*****3**  *2*')
						print('---- A --- B --- C ----')
						print('')

						#step5
						n4step5 = input('5. Move 1 from C to: ')
						if n4step5 == 'A':

							print('')
							print('     |     |     |')
							print('     |     |     |')
							print('     |     |     |')
							print('     |     |     |')
							print('     1     |     |')
							print('  ***4*****3**  *2*')
							print('---- A --- B --- C ----')
							print('')

							#step6
							n4step6 = input('6. Move 2 from C to: ')
							if n4step6 == 'B':

								print('')
								print('     |     |     |')
								print('     |     |     |')
								print('     |     |     |')
								print('     |     |     |')
								print('     1    *2*    |')
								print('  ***4*****3**   |')
								print('---- A --- B --- C ----')
								print('')

								#step7
								n4step7 = input('7. Move 1 from A to: ')
								if n4step7 == 'B':

									print('')
									print('     |     |     |')
									print('     |     |     |')
									print('     |     |     |')
									print('     |     1     |')
									print('     |    *2*    |')
									print('  ***4*****3**   |')
									print('---- A --- B --- C ----')
									print('')

									#step8
									n4step8 = input('8. Move 4 from A to: ')
									if n4step8 == 'C':

										print('')
										print('     |     |     |')
										print('     |     |     |')
										print('     |     |     |')
										print('     |     1     |')
										print('     |    *2*    |')
										print('     |   **3*****4***')
										print('---- A --- B --- C ----')
										print('')

										#step9
										n4step9 = input('9. Move 1 from B to: ')
										if n4step9 == 'C':

											print('')
											print('     |     |     |')
											print('     |     |     |')
											print('     |     |     |')
											print('     |     |     |')
											print('     |    *2*    1')
											print('     |   **3*****4***')
											print('---- A --- B --- C ----')
											print('')

											#step10
											n4step10 = input('10. Move 2 from B to: ')
											if n4step10 == 'A':

												print('')
												print('     |     |     |')
												print('     |     |     |')
												print('     |     |     |')
												print('     |     |     |')
												print('     |     |     1')
												print('    *2*  **3*****4***')
												print('---- A --- B --- C ----')
												print('')

												#step11
												n4step11 = input('11. Move 1 from C to: ')
												if n4step11 == 'A':

													print('')
													print('     |     |     |')
													print('     |     |     |')
													print('     |     |     |')
													print('     |     |     |')
													print('     1     |     |')
													print('    *2*  **3*****4***')
													print('---- A --- B --- C ----')
													print('')

													#step12
													n4step12 = input('12. Move 3 from B to: ')
													if n4step12 == 'C':

														print('')
														print('     |     |     |')
														print('     |     |     |')
														print('     |     |     |')
														print('     |     |     |')
														print('     1     |   **3**')
														print('    *2*    |  ***4***')
														print('---- A --- B --- C ----')
														print('')

														#step13
														n4step13 = input('13. Move 1 from A to: ')
														if n4step13 == 'B':

															print('')
															print('     |     |     |')
															print('     |     |     |')
															print('     |     |     |')
															print('     |     |     |')
															print('     |     |   **3**')
															print('    *2*    1  ***4***')
															print('---- A --- B --- C ----')
															print('')

															#step14
															n4step14 = input('14. Move 2 from A to: ')
															if n4step14 == 'C':

																print('')
																print('     |     |     |')
																print('     |     |     |')
																print('     |     |     |')
																print('     |     |    *2*')
																print('     |     |   **3**')
																print('     |     1  ***4***')
																print('---- A --- B --- C ----')
																print('')

																#step15
																n4step15 = input('15. Move 1 from B to: ')
																if n4step15 == 'C':

																	print('')
																	print('     |     |     |')
																	print('     |     |     |')
																	print('     |     |     1')
																	print('     |     |    *2*')
																	print('     |     |   **3**')
																	print('     |     |  ***4***')
																	print('---- A --- B --- C ----')
																	print('')

																	print('Nice work!')
																	# exit the game
																	n=0

																else:
																	print('')
																	print('TRY AGAIN')
																	print('')
																	n=1	

															else:
																print('')
																print('TRY AGAIN')
																print('')
																n=1	

														else:
															print('')
															print('TRY AGAIN')
															print('')
															n=1	

													else:
														print('')
														print('TRY AGAIN')
														print('')
														n=1	

												else:
													print('')
													print('TRY AGAIN')
													print('')
													n=1	

											else:
												print('')
												print('TRY AGAIN')
												print('')
												n=1

										else:
											print('')
											print('TRY AGAIN')
											print('')
											n=1

									else:
										print('')
										print('TRY AGAIN')
										print('')
										n=1

								else:
									print('')
									print('TRY AGAIN')
									print('')
									n=1

							else:
								print('')
								print('TRY AGAIN')
								print('')
								n=1

						else:
							print('')
							print('TRY AGAIN')
							print('')
							n=1

					else:
						print('')
						print('TRY AGAIN')
						print('')
						n=1

				else:
					print('')
					print('TRY AGAIN')
					print('')
					n=1

			else:
				print('')
				print('TRY AGAIN')
				print('')
				n=1

		else:
			print('')
			print('TRY AGAIN')
			print('')
			n=1

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
	    




	





















