sudoku = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

#DEFAULT EMPTY BOARD

def get_puzzle(sudoku):
	print ()
	print ("Input values of each line, use 0 for empty.")   
	print ()
	print ("Example: 0 0 7 2 0 0 0 9 0")
	print ("--------------------------")
	print ()
	for row in range(len(sudoku)):			  				#gets string input and convert into integer list
		line = input('line {}:  '.format(row +1)).split() 	
		new_line = list(map(int, line))		 				
		sudoku[row] = new_line								#input integer list into row

	return sudoku 											#return the new puzzle

def print_puzzle(sudoku):									#print properly formatted puzzle
	for row in range(len(sudoku)):
		if row % 3 == 0 and row != 0:						
			print ("---------------------")
		for column in range(len(sudoku[0])):
			if column % 3 == 0 and column != 0:				
				print ("|", end=' ')
			if column %8 ==0 and column != 0:				
				print (sudoku[row][column])
			else:
				print (sudoku[row][column],end=' ')			

def next_empty(sudoku):										#checks each row and column for a 0.
	for row in range(len(sudoku)):
		for column in range(len(sudoku[0])):
			if sudoku[row][column] == 0:
				return (row, column)						#return row and column in tuple as position
	return False

def check(sudoku, num, pos):								#check if number is valid in position
	for row in range(len(sudoku)):							
		if sudoku[row][pos[1]] == num and row != pos[0]:	#checks column
			return False

	for column in range(len(sudoku[0])):					#checks row
		if sudoku[pos[0]][column] == num and column != pos[1]:
			return False									

	box_x = pos[1] //3										#determine position quadrant
	box_y = pos[0] //3

	for row in range(box_y*3, box_y*3 +3):					#checks quadrant of position
		for column in range(box_x*3, box_x*3 +3):
			if sudoku[row][column] == num and (row, column) != pos:
				return False

	return True												#if checks didn't return a false, valid number

def solve(sudoku):											#primary solve function
	empty = next_empty(sudoku)								#get next empty
	if not empty:											#if empty returns false, no more empty (solved)
		return True
	else:
		row, column = empty 								#assign position of empty

	for num in range(1,10):
		if check(sudoku, num, (row, column)):				#check for valid number in assigned position
			sudoku[row][column] = num
			if solve(sudoku):								#if valid, run solve function again to get next empty
				return True									#start nested solve function
			sudoku[row][column] = 0 						#if solve = false, reassign 0, backtrack to parent solve

	return False											#if solve does not find a solution, return false

# solve(sudoku)
# print_puzzle(sudoku)

if __name__=='__main__':									#main program function
	print ()
	print ("-----------------------------------------")
	print ()
	print ("             SUDOKU SOLVER")
	print ()
	print ("-----------------------------------------")
	while True:												#try to get a valid puzzle
		try:
			sudoku = get_puzzle(sudoku)
			print ()
			print_puzzle(sudoku)
			print ()
		except:												#if invalid, try again
			print ()
			print ("invalid input")
			continue

		while True:											#doublecheck with user
			answer = input ("Is this correct? (yes/no) ").lower().strip()
			print ()
			if answer == 'yes':
				print ("Please wait...")
				print ()
				if solve(sudoku):							#run solve on puzzle
					print_puzzle(sudoku)
					input()
					break
				else:										#if solve returns false
					print("No solution.")
					input()
					break

			elif answer == 'no':
				break

			else:
				print ("invalid input.")