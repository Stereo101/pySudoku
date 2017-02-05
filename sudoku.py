import re
from heapq import heappush,heappop
#Solve the sudo puzzle logically, or recursively search for a 
#       solution with the smallest guess possible
def solve(sudoString):
	sudo = logicalSearch(sudoString)
	if(isDone(sudo)):
		return sudo
	guesses = getSmallestGuess(sudo)
	if(guesses == 'failed to find'):
		return 'failed to finish'
	else:
		for g in guesses:
			x = solve(g)
			if(x != 'failed to finish'):
				return x
	return 'failed to finish'

#Remove whitespace and normalize string
def prepareString(stringIn):
	return re.sub('0','.',re.sub(r'[^0-9\.]',"",stringIn))

#Return a string with character at position i swapped with char
def mark(sudoString,i,char):
	return sudoString[:i] + char + sudoString[i+1:]

#Fill all empty spaces where only 1 number will fit until no such spaces exist
def logicalSearch(sudoString):
	markArray = []
	for i in range(81):
		if(sudoString[i] == '.'):
			s = getPossible(sudoString,i)
			if(len(s) == 1):
				markArray.append([i,s.pop()])

	if len(markArray) != 0:
		sudoList = list(sudoString)
		for m in markArray:
			sudoList[m[0]] = m[1]
		return logicalSearch("".join(sudoList))
	else:
		return sudoString

#Get possible numbers to place in position i
def getPossible(sudoString,i):
	rowStart = int(i/9)*9
	colStart = i%9
	boxStart = (int(int(i/9)/3)*27) + (3*int((i%9)/3))
	x = {'1','2','3','4','5','6','7','8','9'}
	for k in range(9):
		x.discard(sudoString[rowStart + k])
		x.discard(sudoString[colStart + k*9])
		x.discard(sudoString[boxStart + int(k/3)*9 + k%3])    
	return x
	
#Return strings of boards based on smallest possible guess
def getSmallestGuess(sudoString):
	guessHeap = []
	for i in range(81):
		if(sudoString[i] == '.'):
			s = getPossible(sudoString,i)
			if(len(s) == 0):
				return 'failed to find'
				continue
			heappush(guessHeap,(len(s),s,i))
			
	if(guessHeap):
		s = heappop(guessHeap)
		guesses = []
		print(s[1],'=',s[0],'@',s[2])
		for k in s[1]:
			guesses.append(mark(sudoString,s[2],k))
		return guesses
	else:
		return 'failed to find'

#Check if puzzle is finished
def isDone(sudoString):
	return ('.' not in sudoString)

#Print a sudoku board like you would expect
def prettyPrint(sudoString):
	s = []
	for i in range (9):
		s.append(sudoString[9*i:9*(i+1)] + '\n')
	s.append("\n")
	return "".join(s)

#Main function, load the puzzles and then solve them all
if __name__ == "__main__":
	with open("puzzles.txt",'r') as f:
		lines = f.readlines()
		for l in lines:
			prep = prepareString(l)
			if(len(prep) != 81):
				print("bad puzzle")
			else:
				print(prettyPrint(prep))
				print(prettyPrint(solve(prep)),"\n")
