class Animal:
    def sound(self):
        print("Some generic sound")
    
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def sound(self):
        print("Bark")
    
    def fetch(self):
        print("The dog is fetching the ball")

# Creating more instances of Animal and Dog
animal1 = Animal()
animal2 = Animal()
dog1 = Dog()
dog2 = Dog()

# Testing sound method
animal1.sound()  
animal2.sound() 
dog1.sound()   
dog2.sound()     

# Testing additional methods
animal1.eat()    
animal2.eat()    
dog1.fetch()    
dog2.fetch()     
