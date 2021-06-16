def display(*name, **address):
	""" Docstring - multi arguments """
	for items in name:
		print (items)
		
	for items in address.items():
		print(items)

#calling function	
display ("Girish", "anita", "arti", "shewta", Girish = "LA", anita = "US", arti = "India", shewta = "LA")
print(display.__doc__)

help(display)



