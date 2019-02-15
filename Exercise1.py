#Define a function that accepts a percentage as an argument and returns a letter grade (A+, A, A-, B+, etc) for that percentage.

#Prompt your user to enter a percentage and display a message showing them the equivalent letter grade.


def percentage(grade):

	if int(grade) >= 80: 
		return print("You got an A in the class.")

	elif int(grade) >= 70:
		return print("You got a B in the class.")	
	
	elif int(grade) >= 60:
		return print("You got a C in the class.")	

	elif int(grade) == 50:
		return print("You got a D in the class.")	

	else:
		return print("You failed with a capital F loool!")	

		
print("What percentage grade did you get in the course?")
grade = 0
grade = int(input())
percentage(grade)