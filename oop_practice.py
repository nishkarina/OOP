#  Practice problems on OOPs by PyNative
# 1.Write a python program to create a Vehicle class with max_speeed and mileage instance attribute 
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# a_obj = Vehicle(190, 22)
# print(a_obj.max_speed)

# ------------------------------------------------------------------------------------------------------------------------------

# 2.Create a class Vehicle without creating any variables and methods
# class Vehicle:
#     pass

#3. Create a child class Bus that wiill inherit all of the variables and methods of the Behicle class
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# a_obj = Bus(180, 22)
# print(a_obj.mileage)

# ---------------------------------------------------------------------------------------------------------------------------

# 4. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50 

# class Vehicle:
#     def __init__(self, max_speed, mileage, seating_capacity = 50):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seating_capacity = seating_capacity

# class Bus(Vehicle):
#     def __init__(self, max_speed, mileage):
#         super().__init__(max_speed, mileage)
#     def text(self):
#         return (f"This is Volvo bus which has {self.mileage} mileage and max speed is {self.max_speed} and has seating capacity of {self.seating_capacity}")

# a_obj = Bus(180, 22)
# print(a_obj.text())

# ---------------------------------------------------------------------------------------------------------------------------

# 5. Define a class attribute "color" with a default value white. That means every vehicle color should be a white
# class Vehicle:
#     color = "white"

#     def __init__(self, max_speed, mileage, seating_capacity):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seating_capacity = seating_capacity

# class Car(Vehicle):
#     pass

# class Bus(Vehicle):
#     pass

# a_obj = Vehicle(122, 12, 50)
# print("The color is ",format(a_obj.color))

# ------------------------------------------------------------------------------------------

# 6.
'''Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating_capacity*100.
If vehicle is Bus instance, we need to add an extra 10% on full fare as a maintanance charge. 
So total fare for bus will  become the final = total_fare + 10% of the total fare'''

# class Vehicle:
#     color = 'white'
#     def __init__(self, max_speed, mileage, seating_capacity = None):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seating_capacity = seating_capacity

#     def fare(self):
#         return self.seating_capacity * 100

# class Bus(Vehicle):

#     def full_fare(self):
#         amount = super().fare()   #using super() we have inherited fare function from parent class
#         final_fare = amount + (10/100)*amount
#         return final_fare

# a_obj = Bus(120, 22, 80)
# print(f"This is the fare of bus {a_obj.fare()}")
# print(f"This is full_fare of the bus {a_obj.full_fare()}")

# ---------------------------------------------------------------------------------------------------------------------

# 7. Write a program to determine which class a given Bus object belongs to

# class Vehicle:

#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage


# class Bus(Vehicle):
#     pass

# a_obj = Bus(120, 22)
# print(type(a_obj)) # it is saying this Bus class belongs to main function

# --------------------------------------------------------------------------------------------------------------

# 8. Determine if school_bus is also an instance of the Vehicle class

# class Vehicle:
#     def __init__(self, name, mileage, car_type):
#         self.name = name
#         self.mileage = mileage
#         self.car_type = car_type

# class Bus(Vehicle):
#     def __init__(self, name, mileage, car_type, max_speed):
#         Vehicle.__init__(self,name, mileage, car_type)
#         self.max_speed = max_speed

# class Car(Bus):
#     def __init__(self, name, mileage, car_type, max_speed, torque):
#         Bus.__init__(self, name, mileage, car_type, max_speed)
#         self.torque = torque

# first_obj = Bus('Volvo', 12, 'BUS', 122)
# second_obj = Car('Nexon', 28, 'SUV Compact', 190, '240 Nm')
# print(isinstance(first_obj, Vehicle)) #True
# print(isinstance(second_obj, Bus)) #True
# print(isinstance(second_obj, Vehicle)) # True
# print(isinstance(first_obj, Car)) # False

# ------------------------------------------------------------------------------------------------------------------------