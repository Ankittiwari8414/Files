 # Calling methods of same name using function.

# class A:
#     def x(self):
#         return "hello"
    
# class B:
#     def x(self):
#         return "Yess"
    
# def z(q):
#     return q.x()


# r=A()
# t=B()

# print(z(r))
# print(z(t))

#  Using inheritance

# class Maths:
#     def area (self):
#         pass

#     def perimeter(self):
#         pass

#     def circumference(self): 
#         pass

# class Rectangle(Maths):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
    
#     def area(self):
#         return self.l* self.b

#     def perimeter(self):
#         return 2*(self.l+self.b)
           
# class square(Maths):
#     def __init__(self,a):
#         self.a=a
    
#     def area (self):
#         return self.a*self.a
    
#     def perimeter(self):
#         return 4*(self.a)

# class circle(Maths):
#     def __init__(self,r,pie):
#         self.r=r
#         self.pie=pie

#     def area(self):
#         return  self.pie*self.r*self.r

#     def circumference(self):
#         return 2*self.pie*self.r
    
# x=[Rectangle(3,5),square(4)]
# c=[circle(4,3.14)]
# for result in x:
#     print(result.area())

# for result in x:
#     print(result.perimeter())

# for result in c:
#     print(result.circumference())


# Abtract Base Class in polymorphism

# from abc import ABC,abstractmethod

# class NSTI(ABC):
#     @abstractmethod
#     def xyz(self):
#         pass

# class AI(NSTI):
#     def xyz(self):
#         return "Artificial Intelligence"

# class CHNM(NSTI):
#     def xyz(self):
#         return "Computer Hardware, Networking and Maintance"

# class CSA(NSTI):
#     def xyz(self):
#         return "Computer software Application"

# trade=[AI(),CHNM(),CSA()]

# for result in trade:
#     print(result.xyz())

#                              TASK

 #  Demonstrates calculating the area of different shapes using Abstract Class

# from abc import ABC, abstractmethod

# class shapes:
#     @abstractmethod
#     def area(self):
#         pass

# class rectangle(shapes):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
    
#     def area (self):
#         return self.l*self.b

# class square(shapes):
#     def __init__(self,s):
#         self.s=s

#     def area (self):
#         return self.s*self.s

# class circle(shapes):
#     def __init__(self,pie,r):
#         self.pie=pie
#         self.r=r

#     def area (self):
#         return 2*self.pie*self.r
# class triangle(shapes):
#     def __init__(self,b,h):
#         self.b=b
#         self.h=h

#     def area (self):
#         return 1/2*self.b*self.h

# class trapezoid(shapes):
#     def __init__(self,a,b,h):
#         self.a=a
#         self.b=b
#         self.h=h

#     def area (self):
#         return 0.5*(self.a+self.b)*self.h

# x=[rectangle(4,5),square(4)]
# y=[circle(3.14,6)]
# z=[triangle(4,7)]
# A=[trapezoid(4,6,8)]

# for result in x:
#     print(result.area())

# for result in y:
#     print(result.area())

# for result in z:
#     print(result.area())

# for result in A:
#     print(result.area())

# Write a code for Abstract class where you are building a restaurant ordering system. 
# The menu includes main courses, beverages, and desserts.
#  Each item has a different preparation time and pricing model.

# from abc import ABC,abstractmethod

# class Restaurant:
#     @abstractmethod
#     def order(self):
#         pass

# class maincourses(Restaurant):
#     def __init__(self,dish_name,preparation_time,price):
#         self.dish_name=dish_name
#         self.preparation_time=preparation_time
#         self.price=price

#     def order(self):
#         return f'Dish Name : {self.dish_name}, Preparation Time : {self.preparation_time}, price : {self.price}'

# class Beverage(Restaurant):
#     def __init__(self,drinks_name,preparation_time,price):
#         self.drinks_name=drinks_name
#         self.preparation_time=preparation_time
#         self.price=price

#     def order(self):
#         return f'Drinks Name : {self.drinks_name}, Preparation Time : {self.preparation_time}, Price : {self.price}'

# class Desserts(Restaurant):
#     def __init__(self,desserts_name,preparation_time,price):
#         self.desserts_name=desserts_name
#         self.preparation_time=preparation_time
#         self.price=price

#     def order(self):
#         return f'Desserts Name : {self.desserts_name}, Preparation Time : {self.preparation_time}, price :{self.price}'


# x=[maincourses("Paneer","25 Min","250/-")]
# y=[Beverage("cold cofee","10 min","180/-")]
# z=[Desserts("lalmohan","5 min","50/-")]
    
# for result in x:
#     print(result.order())

# for result in y:
#     print(result.order())

# for result in z:
#     print(result.order())


