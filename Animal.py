class Animal:
    def __init__(self, name): 
        self.__name = name
        print("Hello i am", self.__name)

    def talk(self):
        print( self.__name, "says what you just said!") 

    def drink(self):
        print( self.__name, "like to drink orange juice!") 

    def eat(self):
        print( self.__name, "only eats vegetables!") 

    def fly(self):
        print( self.__name, "flies when he wants to!") 

    def look(self):
        print( self.__name, "looks beautiful!") 

    def counts(self):
        print( self.__name, "counts up to 100!") 
