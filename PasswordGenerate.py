from random import randint

def isNumber (x):
	val = 0
	try:
		x = int(x)
	except ValueError:
		val = False
	else:
		val = True
	return val

def shuffle(x):
	y = []
	for i in range(len(x)):
		if i < len(x)-1:
			k = randint(0,(len(x)-1)-i)
		else:
			k = 0
		y.append(x[k])
		x.remove(x[k])
	return ''.join(y)
		

print("\n\tWelcome to the password generator!\n")
print("Please note that the minimum size for a password using this generator is 8 characters.")
L = input("Please enter the desired length of your password: ")
while ((isNumber(L) and int(L) < 8) or not isNumber(L)):
	print("Your desired password length must be an integer greater than or equal to 8.")
	L = input("Please enter the desired length of your password: ")

L = int(L)

print("Now choose one of the following options:")
print("0: alphanumeric | 1: alphanumeric and special characters")
choice = input("Please enter your choice: ")
while (choice != str(0) and choice != str(1)):
	print("Please make sure you make a valid choice. The options are '0' or '1'.")
	choice = input("Please enter your choice: ")

choice = int(choice)

if (not choice):
	numberCount = randint(1,L//2+1)
	alphaCount = randint(1,L-(numberCount+1))
	alphaCapCount = L - (numberCount+alphaCount)

	number = []
	alpha = []
	alphaCap = []

	for i in range(numberCount):
		number.append(randint(0,9))
	for i in range(alphaCount):
		alpha.append(randint(97,122))
	for i in range(alphaCapCount):
		alphaCap.append(randint(65,90))

	number = list(map(str,number))
	alpha = list(map(chr,alpha))
	alphaCap = list(map(chr,alphaCap))

	temp = number+alpha+alphaCap

else:
	numberCount = randint(1,L//2+1)
	alphaCount = randint(1,L-(numberCount+2))
	alphaCapCount = randint(1,L-(numberCount+alphaCount+1))
	specialCount = L - (numberCount+alphaCount+alphaCapCount)

	number = []
	alpha = []
	alphaCap = []
	special = []

	specialSymbols = [33, 38, 40, 41, 46]

	for i in range(numberCount):
		number.append(randint(0,9))
	for i in range(alphaCount):
		alpha.append(randint(97,122))
	for i in range(alphaCapCount):
		alphaCap.append(randint(65,90))
	for i in range(specialCount):
		special.append(specialSymbols[randint(0,4)])

	number = list(map(str,number))
	alpha = list(map(chr,alpha))
	alphaCap = list(map(chr,alphaCap))
	special = list(map(chr,special))

	temp = number+alpha+alphaCap+special

password = shuffle(temp)
print("\n\tYour password is: "+password)
