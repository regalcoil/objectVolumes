import math

vols = ['sphere', 'cube', 'pyramid', 'cylinder']
b = " "

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
		radius = float(input("What is the radius of your " + vols[choice-1] + "? "))
		itopi = radius*radius*radius*(4/3)
		pi = 3.14159
		nt = itopi*pi
		print(b)
		print("In terms of π:   " + str(itopi) + "π units^3")
		print(b)
		print("Numerical terms: " + str(nt) + " units^3")
	elif choice == 2:
		side = float(input("What are the lengths of the sides of your " + vols[choice-1] + "? "))
		v = side*side*side
		print(b)
		print("Volume:          " + str(v) + " units^3")
	elif choice == 3:
		typeP = int(input("How many sides does the base of your " + vols[choice-1] + " have? "))
		if typeP > 4:
			angle = 360/(typeP*2)
			print(b)
			length = float(input("What is the length of each side? "))
			radians = math.radians(angle)
			radius = (length/2) / math.tan(radians)
			triA = ((length/2) * radius)/2
			Area = triA*(typeP*2)
			print(b)
			height = float(input("What is the height of your " + vols[choice-1] + "? "))
			v = (Area*height)/3
			print(b)
			print("Volume:          " + str(v) + " units^3")
		elif typeP == 4:
			print(b)
			eq = input("Type 'square' if the base of your pyramid is a square and 'rectangle' if it is a rectangle: ")
			eq.lower()
			if eq == 'square':
				angle = 360/(typeP*2)
				print(b)
				length = float(input("What is the length of each side? "))
				radians = math.radians(angle)
				radius = (length/2) / math.tan(radians)
				triA = ((length/2) * radius)/2
				Area = triA*(typeP*2)
				print(b)
				height = float(input("What is the height of your " + vols[choice-1] + "? "))
				v = (Area*height)/3
				print(b)
				print("Volume:          " + str(v) + " units^3")
			elif eq == 'rectangle':
				print(b)
				length = float(input("What is the length of the base of your " + vols[choice-1] + "? "))
				print(b)
				width = float(input("What is the width of the base of your " + vols[choice-1] + "? "))
				print(b)
				height = float(input("What is the height of the base of your " + vols[choice-1] + "? "))
				v = (length*width*height)/3
				print(b)
				print("Volume:          " + str(v) + " units^3")
		elif typeP == 3:
			print(b)
			eq = input("Type 'equilateral' if the base of your pyramid is equilateral, 'right' if the object is a right triangular pyramid or 'other' if it is a irregular trianglular pyramid: ")
			eq.lower()
			if eq == 'equilateral':
				angle = 360/(typeP*2)
				print(b)
				length = float(input("What is the length of each side? "))
				radians = math.radians(angle)
				radius = (length/2) / math.tan(radians)
				triA = ((length/2) * radius)/2
				Area = triA*(typeP*2)
				print(b)
				height = float(input("What is the height of your " + vols[choice-1] + "? "))
				v = (Area*height)/3
				print(b)
				print("Volume:          " + str(v) + " units^3")
			elif eq == 'right':
				print(b)
				length = float(input("What is the length of a side of the base triangle? "))
				print(b)
				height - float(input("What is the height of your " + vols[choice-1] + "? "))
				v = (side*side) * height * ((3**0.5)/12)
				print(b)
				print("Volume:          " + str(v) + " units^3")
			elif eq == 'other':
				print(b)
				length = float(input("What is the length of a side of the base triangle? "))
				bheight = float(input("What is the height of the base triangle? "))
				print(b)
				height - float(input("What is the height of your " + vols[choice-1] + "? "))
				base = (length*bheight)/2
				v = (base*height)/3
				print("Volume:          " + str(v) + " units^3")
	elif choice == 4:
		radius = float(input("What is the radius of the base of your " + vols[choice-1] + "? "))
		print(b)
		height = float(input("What is the height of your " + vols[choice-1] + "? "))
		itopi = radius*radius*height
		pi = 3.14159
		nt = itopi*pi
		print(b)
		print("In terms of π:   " + str(itopi) + "π units^3")
		print(b)
		print("Numerical terms: " + str(nt) + " units^3")
	else:
		print("wrong choice start over!")
	print(b)
	print("****************")
	volume()

volume()