#Inhertance

class A():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.a
    def sub(self):
        return self.a - self.b
class B(A):
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

obj = B(10,5)
print(obj.add())
print(obj.div())
    


#Method Overriding 
# class parent():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def value(self):
#         return self.a
# class Child(parent):
#     def value(self):
#         return self.b

# obj = Child(10,20)
# print(obj.value())


#Encapsulation
# using private
# class A():
#     def __init__(self,a,b,c):
#         self.__a = a
#         self.__b = b
#         self.c = c
    
#     def values(self):
#         print(self.__a)
#         print(self.__b)

# obj = A(10,15,4)
# print(obj.c)
# print(obj.__a)


#using protected

class A():
    def __init__(self,a,b):
        self._a = a
        self._b = b
    def value(self):
        return self._a

class B(A):
    def values(self):
        print(self._a)
        print(self._b)

obj = B(10,20)
obj.values()

        
#overloading

# class A():
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def add(self):
#         return self.a+self.b
#     def add(self):
#         return self.a+self.b+self.c
    
# obj = A(10,20,30)
# print(obj.add())


#Abstraction 

# from abc import ABC, abstractclassmethod

# class Vehicle(ABC):
#     @abstractclassmethod
#     def wheels(self):
#         pass
#     @abstractclassmethod
#     def start(Self):
#         pass
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def wheels(self):
#         print("4 wheels")
# v = Car()
# print(v)
