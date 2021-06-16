class car:
    """ A simple class for cars """

    #Constructor to initialize

    def __init__(self,company, color):
        #These are private variables
        print("__init__ function is called for ", self)
        self.company = company
        self.color = color
    #Member function to pring car company and color
    def display(self):
        print("this is a ", self.color, self.company)


#Let us use built in variables"
F = car("Ferrari", "Red")
F.display()

print("car.__name__ = ", car.__name__)
print("car.__doc__ = ", car.__doc__)
print("car.__module__ = ", car.__module__)
print("car.__dict__ = ", car.__dict__)



        
