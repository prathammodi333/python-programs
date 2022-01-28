# Name : PRATHAM MODI
# ID : 20CE056
# Aim :  Find Captain Room Number
# GITHUB LINK : https://github.com/prathammodi333/python-programs
n = int(input("enter the number of members per group : "))
myLiST = [int(item) for item in input("Enter the list items : ").split()]
# using list comprehension
listToStr = ''.join([str(elem) for elem in myLiST])
new_str = listToStr

NO_OF_CHARS = 256

# Returns an array of size 256 containing count
# of characters in the passed char array
def getCharCountArray(string):
	count = [0] * NO_OF_CHARS
	for i in string:
		count[ord(i)]+= 1
	return count

# The function returns index of first non-repeating
# character in a string. If all characters are repeating
# then returns -1
def firstNonRepeating(string):
	count = getCharCountArray(string)
	index = -1
	k = 0

	for i in string:
		if count[ord(i)] == 1:
			index = k
			break
		k += 1

	return index

index = firstNonRepeating(new_str)
if index == 1:
	print ("Either all characters are repeating or string is empty")
else:
	print ("captain's room is : " , new_str[index])




