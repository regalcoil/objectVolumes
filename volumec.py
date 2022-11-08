import math

vols = ['sphere', 'cube', 'pyramid', 'cylinder']
b = " "

def area(s):
	angle = 360/(s*2)
	print(b)
	length = float(input("What is the length of each side? "))
	radians = math.radians(angle)
	radius = (length/2) / math.tan(radians)
	triA = ((length/2) * radius)/2
	global Area
	Area = triA*(s*2)

def sphere(x):
	radius = float(input("What is the radius of your " + vols[x-1] + "? "))
	itopi = radius*radius*radius*(4/3)
	pi = 3.14159
	nt = itopi*pi
	print(b)
	print("In terms of π:   " + str(itopi) + "π units^3")
	print(b)
	print("Numerical terms: " + str(nt) + " units^3")

def cube(x):
	side = float(input("What are the lengths of the sides of your " + vols[x-1] + "? "))
	v = side*side*side
	print(b)
	print("Volume:          " + str(v) + " units^3")

def npyramid(sides, y):
	area(sides)
	print(b)
	height = float(input("What is the height of your " + vols[y-1] + "? "))
	v = (Area*height)/3
	print(b)
	print("Volume:          " + str(v) + " units^3")

def fpyramid(sides, y):
	print(b)
	eq = input("Type 'square' if the base of your pyramid is a square and 'rectangle' if it is a rectangle: ")
	eq.lower()
	if eq == 'square':
		area(sides)
		print(b)
		height = float(input("What is the height of your " + vols[y-1] + "? "))
		v = (Area*height)/3
		print(b)
		print("Volume:          " + str(v) + " units^3")
	elif eq == 'rectangle':
		print(b)
		length = float(input("What is the length of the base of your " + vols[y-1] + "? "))
		print(b)
		width = float(input("What is the width of the base of your " + vols[y-1] + "? "))
		print(b)
		height = float(input("What is the height of the base of your " + vols[y-1] + "? "))
		v = (length*width*height)/3
		print(b)
		print("Volume:          " + str(v) + " units^3")
	else:
		print(b)
		print("Wrong choice, try again")
		fpyramid(sides, y)

def tpyramid(sides, y):
	print(b)
	eq = input("Type 'equilateral' if the base of your pyramid is equilateral, 'right' if the object is a right triangular pyramid or 'other' if it is a irregular trianglular pyramid: ")
	eq.lower()
	if eq == 'equilateral':
		area(sides)
		print(b)
		height = float(input("What is the height of your " + vols[y-1] + "? "))
		v = (Area*height)/3
		print(b)
		print("Volume:          " + str(v) + " units^3")
	elif eq == 'right':
		print(b)
		length = float(input("What is the length of a side of the base triangle? "))
		print(b)
		height - float(input("What is the height of your " + vols[y-1] + "? "))
		v = (side*side) * height * ((3**0.5)/12)
		print(b)
		print("Volume:          " + str(v) + " units^3")
	elif eq == 'other':
		print(b)
		length = float(input("What is the length of a side of the base triangle? "))
		bheight = float(input("What is the height of the base triangle? "))
		print(b)
		height - float(input("What is the height of your " + vols[y-1] + "? "))
		base = (length*bheight)/2
		v = (base*height)/3
		print("Volume:          " + str(v) + " units^3")
	else:
		print(b)
		print("Wrong choice, try again")
		tpyramid(sides, y)

def pyramid(x):
	typeP = int(input("How many sides does the base of your " + vols[x-1] + " have? "))
	if typeP > 4:
		npyramid(typeP, x)
	elif typeP == 4:
		fpyramid(typeP, x)
	elif typeP == 3:
		tpyramid(typeP, x)
	else:
		print(b)
		print("Wrong choice, try again")
		print(b)
		pyramid(x)

def cylinder(x):
	radius = float(input("What is the radius of the base of your " + vols[x-1] + "? "))
	print(b)
	height = float(input("What is the height of your " + vols[x-1] + "? "))
	itopi = radius*radius*height
	pi = 3.14159
	nt = itopi*pi
	print(b)
	print("In terms of π:   " + str(itopi) + "π units^3")
	print(b)
	print("Numerical terms: " + str(nt) + " units^3")

def volume():
	print(b)
	print("Which object would you like to find the volume of?")
	print(b)
	for i in vols:
		print(str(vols.index(i)+1) + ": " + i)
	print(b)
	choice = int(input("#: "))
	print(b)
	if choice == 1:
		sphere(choice)
	elif choice == 2:
		cube(choice)
	elif choice == 3:
		pyramid(choice)
	elif choice == 4:
		cylinder(choice)
	else:
		print("Wrong choice, try again")
	print(b)
	print("****************")
	volume()

volume()