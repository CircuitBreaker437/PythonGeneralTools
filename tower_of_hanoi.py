# Filename: tower_of_hanoi.py
# Programmer: Marcin Czajkowski
# Revision: 1.0 
# Purpose: Simple algorithm for towers of hanoi

import sys

#This variable will track the total number of moves
NUM_OF_MOVES = 0    

#Towers of Hanoi algorithm
def move_disk(disks, source, transfer, destination):
    global NUM_OF_MOVES
    if disks == 0:
        return
    else:
        move_disk(disks - 1, source, destination, transfer)
        print ("Moving disk:\n    ->from %s tower to %s tower" % (source, destination))
        NUM_OF_MOVES += 1
        move_disk(disks - 1, transfer, source, destination)
        
#Validating user input
while(True):
	disks = input("Enter number of plates (positive INTEGERS only please): ")
	try:
		if ((disks != '') and (int(disks) > 0)):
			disks_num = int(disks)
			break
	except ValueError:
		#detected invalid value that cannot be an integer
		continue

#User iput validated - tart the HANOI algorithm
move_disk(disks_num, "SOURCE", "TRANSFER", "DESTINATION")
print ("Total number of moves = %s" % NUM_OF_MOVES)
