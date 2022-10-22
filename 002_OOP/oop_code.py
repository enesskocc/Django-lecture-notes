import os
from re import S
from tkinter.filedialog import SaveFileDialog
os.system('cls' if os.name == 'nt' else 'clear')


print("-------------------------------------")

# def print_types(data):
#     for i in data:
#         print(i, type(i))


# test = [122, 'victor', [1,2,3], (1,2,3), {1,2,3,}, True, lambda x:x]
# print_types(test)


    
# class Person:
#     name = "victor"
#     age = 32


# person1 = Person()
# person2 = Person()

# print(person1.name)
# print(person2.age)

# Person.job = "developer"
# print(person1.job)


#! class attributes vs instance attributes:

# person1.location = "Türkiye"
# # print(person2.location)

# person2.age = 18
# print(person2.age)

# class Person:
#     company = "clarusway"
    
#     def test(self):
#         print("test")
    
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
        
#     def get_details(self):
#         print(self.name, self.age)
    
#     @staticmethod
#     def salute():
#         print("Hi there !")
    

# person1 = Person()
# print(person1.company)
# person1.test()  # >>>>>>> Person.test(person1)


# person1.set_details(name="barry", age=45)  # Person.set_details(person1, name=barry, age=45)
# person1.get_details()
# person1.salute()


#! special methods (init , str, ...)


class Person:
    company = "clarusway"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def get_details(self):
        print(self.name, self.age)
        
    def __str__(self):
        return f"{self.name} - {self.age}"
    
        
        
""" person1 = Person(name="henry", age=23)
# person1.get_details()     
# print(person1.__id)
print(person1._Person__id2)



liste = [3,1,6,3]
liste.sort()
print(liste) """

class Lang:
    def __init__(self, lang):
        self.lang = lang
        
    def display_langs(self):
        print((self.lang))



class Employee(Person, Lang):
    def __init__(self, name, age, path, lang):
        super().__init__(name,age)
        Lang.__init__(self, lang)
        # self.name = name
        # self.age = age
        self.path = path
        
    
    def get_details(self):
        super().get_details()
        print(self.path)


emp1 = Employee("ahmet", 23, "FS", ["python", "javascript"])
# emp1.get_details()
# emp1.display_langs()




# print(Employee.mro())
# print(help(Employee))
# print(emp1.__dict__)




#! inner class:



# from django.db import models

# class Makale(models.Model):
#     title = models.CharField(max_length=30)
#     author = models.CharField(max_length=50)
    
#     class Meta:
#         ordering = ["title"]
    
    
# myMakale = Makale(title="adasd", author="asda")



#!Topics to be Covered:

#* Everything in Python is class
#? Defining class
#* Defining class attributes
#? Difference between class attributes and instance attributes
#* SELF keyword
#? Static methods
#* Special methods (init, str)
#? 4 pillars of OOP:
#     Encapsulation
#     Abstraction
#     Inheritance
#        Multiple inheritance
#     Polymorphism
#        Overriding methods
#* Inner class







print("-------------------------------------")