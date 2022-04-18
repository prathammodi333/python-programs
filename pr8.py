# It is base class
class base:
    # In base class one display function without any parameter
    def display(self):
        print("I am in base class")
    
# It is derived class
class derived:
    # In derived class one display function without any parameter
    def display(self):
        print("I am in derived class")

b1 = base()     # create b1 object of base class
d1 = derived()      # create d1 object of derived class

b1.display()        # call the base class function - display   (I am in base class)
d1.display()        # call the derived class function - display  (I am in derived class)