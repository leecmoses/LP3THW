# Good reference: http://www.pythonforbeginners.com/super/working-python-super-function


## class Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a __init__ that takes self and name as parameters
        self.name = name

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a __init__ that takes self and name as parameters
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name as parameters
        self.name = name

        ## class Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## Return a proxy object that delegates method calls to a parent or sibling class of type.
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## From mary get attribute pet and set it to satan
mary.pet = satan 

## frank is-a Employee instance has-a attribute name of Frank and salary of 120000
frank = Employee("Frank", 120000)

## pet attribute of frank is-a rover
frank.pet = rover

## flipper is-a Fish instance
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## harry is-a Halibut instance
harry = Halibut()