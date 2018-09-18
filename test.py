import os 		# this is for system pause
import random
n=15
guess=0
tguess=int(n*random.random())+1
while (guess!=tguess):
	guess=int(input("Enter your guess Value: "))
	if (guess>0):
		if (guess>tguess):
			print("Mali ang Hula mo lower! ")
		elif (guess<tguess):
			print("Mali ang Hula mo Higher")
	else:
		print("Weak Suko na agad")
		break

else:
	print("Nice Nahulaan Mo!")
#print("Enter your Name: ")
#x=input()
#x =input("Enter a number: ")
#print("Hello, " + x)


os.system("pause") 			# command for system pause