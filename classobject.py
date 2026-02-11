
#class is a blueprint of an object
#object is an instance of a class
class Employee:
    #Attributes/Variables
    name ="Sharleen"
    age = 40
    gender = "Male"
    salary =70000.00

    #Behaviour/Functions
    def eat(self):
        print("Employee eaten")


employee1 = Employee() #Creating an object
print(employee1.name)

employee2 = Employee()
print(employee2.name)

employee3 = Employee()


