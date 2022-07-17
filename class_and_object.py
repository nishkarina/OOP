
# Object Oriented Programming
'''In python, everything is an object whether it is a list or dictionary or your Dataframe everything is object and hence it is very important to get to 
know about how it works.
Let's learn about class:
class is nothing but a set of functions/statements which has predefined things to do. You can define class using class followed by a name for that
class and then semicolon. This is all for your header part you need. 
*P.S.: every class name has to starts with capitalize letter.
Let's take an example below to define a class'''

# class My_First_class:
#     '''This is doc string which tells about why this class has been created or what's the purpose of this class'''
#     print("This is my first class that I have made")

# a_obj = My_First_class
# print(My_First_class())   #<- here you're involking your class
'''Here is the output:
This is my first class that I have made
<__main__.My_First_class object at 0x000001F33023C040>, here the __main__ means it is telling you that you have made a class and main() function has been executed
after that you can see a ".My_First_class" which means that in main() you have made an object which has a name -> My_First_class and it is stored at some 
gibberish location '''
# congratulations! you have just made a class.

'''Now let's talk about object; object is real-world like quantity where as class is logical thing and to bring logical thing into reality we make an object.
Now, there's bit confusin most of the type happens between instance and object and as per my knowledge instantiation which is just a process of creating 
an object ~ instance. In above example a_obj is an object which has been craeted and an instance which is created when class has been built.
If you are still confuse at this point, don't worry just be patient at the end you will get to know the difference between them.'''

# Moving onto next part which is important factor in making class at its best is constructor method:
'''Now, what the heck is constructor method??
Let's cover up two thing here
1. constructor: contstructor method can be defined as def __init__(self): this is again your header part of the function. Now you will ask me who is the function here
because you were telling us about constructor "method". So answer is, anything which can be followed by def and has paranthesis in which you write some arguments is called as
function which ends with : 
2. Concept about method: While a function can be called from anywhere, a class method can only be called from an instance of that class. Because of this, every method is a function but not every function is a method.
function has shown below'''

# some_string = "SOME GIBBERISH WRITING"
# ex = some_string.lower()  #<- here you can see lower() function has been called.
# print(ex)

'''Now moving back to our constructor method, in our class there is no meaningful thing that our class would accomplish it. So we will do it by setting up an initial attributes. '''
# class My_First:

#     def __init__(self, name, age):
#         self.name = name  #->here self.name is an attribute which is assign to the parameter name
#         self.age = age

# a_obj = My_First('Nihal', 28)

'''From above example, you can see, the __init__() is the constructor method and this method set to initialize the state of the object, by initialising the class.
These function can contain any number of parameter but first parameter has to be self variable. This self variable is acts likes a agent/helper through
which you can access all the attributes, methods/functions in the body except class attribute which we will cover in a while.
So, self enables objects to access its attributes and methods and make these instances unique'''

#Class attributes
'''Just like in constructor method there was an attribute, likewise in a class there is a class attribute which has to define before constructor method.
These class attribute has a scope of overall class as it declares gloablly inside the class. There is example below,'''

# class My_first:
#     #class attribute
#     Species = 'Human'

#     def __init__(self, name, age):
#         #instance attributes
#         self.name = name  # Go to the object self refer to and get the value of name which is here is -> name at RHS which is also called object attribute
#         self.age = age

# a_obj = My_first("Nisha", 85)
# print(a_obj.Species) # accessing class attribute
# '''Here in above example there are three types of attributes, one is class and rest are instance attributes.'''

# #accesing the object attribute
# print(a_obj.age)  #o/p: 85
# # We can modify these object attributes by simply assigning a value
# a_obj.age = 58
# print(a_obj.age) #o/p: 58

# Python functions and methods
'''While a function can be called from anywhere, a class method can only be called from an instance of that class. Because of this, every method 
is a function but not every function is a method.
The object that we have created contains an information, but they do not actually do anything. In Python, we use function to do repetitive task.
->Method refers to the funtion which contained an object'''

# class My_first:
#     species = 'Human'

#     def __init__(self, name, age):
#         self.name = name
#         self.age= age

#     def greetings(self):  # as we have  self here as an argument hence below it accessible
#         return (f"Hi, Good Morning Mr/Mrs {self.name}")

# a_obj = My_first("Nisha", 58)
# print(a_obj.greetings())  #o/p: Hi, Good Morning Mr/Mrs Nisha

# we can access objcet attribute and modify them as follows
# class My_first:

#     species = 'Human'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greeting(self):
#         print(f"Hi! Mr/Mrs {self.name}")

#     def birthdate(self):
#         self.age += 1

# a_obj = My_first("Nihal", 56)
# a_obj.birthdate() # we have made connection with a function
# print(a_obj.age) # and have modified the age

#class Inheritance:
'''Inheritance is the process through which we brings the behaviour of the parents class to the child class. We can call all the objects attribute of parent 
class to the child class using super() method.'''

# class Parent_Class:
#     species = 'Human'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return (f"Hi there, Mr/Mrs {self.name}")

# class child_class(Parent_Class):

#     def __init__(self, name, age, id, income):
#         super().__init__(name, age)  # this is super method
#         self.id = id
#         self.income = income

#     def do_work(self):
#         return (f"How may I help you {self.name} with id {self.id}")

# a_obj = child_class("Nihal", 58, 2454, 65479)
# print(a_obj.do_work()) #  How may I help you Nihal with id 2454

# print(a_obj.greet()) # Hi there, Mr/Mrs Nihal and accessing these parent class


'''This super().__init__() function allows you to inherit all the properties of the parent class to the child class without
 needing to repeat them.
Now you can access the parent class.'''

# Polymorphism:
'''Now you can modify and update the behaviour of parent class into a child class using polymorphism. Let's see how it is done
in the below example.'''

# class Parent_Class:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return (f"This is class, Welcome here!")

# class Child_Class(Parent_Class):

#     def __init__(self, name, age, id, income):
#         super().__init__(name, age)
#         self.id = id
#         self.income = income

#     def new_greet(self):
#         return (f"Welcome here!\nHow may I help you Mr/Mrs {self.name} and id {self.id}")   
# a_obj = Child_Class("Nihal", 25, 6574, 65467)
# print(a_obj.new_greet())    #Welcome here!
                            # How may I help you Mr/Mrs Nihal and id 6574

'''This is also called method overriding. Polymorphism allows you to overridden attributes and methods in a child class'''
