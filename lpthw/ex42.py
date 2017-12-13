# Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a __init__
        self.name = name

## Cat is-a Animal:
class Cat(Animal):
    def __init__(self, name):
        ##Cat has-a name
        self.name = name


# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has a pet
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init(name)
        ## Employee has-a salary
        self.salary = salary

##Fish is is-a object:
class Fish(object):
    pass

##Salmon is-a fish
class Salmon(Fish):
    pass

##Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

##mary is-a person
mary = Person("Mary")

##mary has-a pet cat satan
mary.pet = satan

##Frank is-a Employee
frank = Employee("Frank", 120000)

##frank has-a pet dog rover
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

##crouse is -a salmon
crouse = Salmon()

##harry is a Halibut
harry = Halibut()



    
