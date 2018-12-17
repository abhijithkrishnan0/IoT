#Classes

class Employee:
 	
	empCount = 0 
	def __init__(self, name, salary): 
		self.name = name 
		self.salary = salary 
		Employee.empCount += 1
 	def displayCount(self):
	 	print ("Total Employee %d" % Employee.empCount) 	
	def displayEmployee(self):
		print ("Name : ", self.name, ", Salary: ", self.salary )
	def __del__(self): 
		class_name = self.__class__.__name__ 
		print (class_name, "destroyed") 


emp1 = Employee("Zara", 2000) 
 
emp2 = Employee("Manni", 5000) 
emp1.displayEmployee() 
emp2.displayEmployee() 
print ("Total Employee %d" % Employee.empCount)



## INHERITANCE


class Parent:
    def __init__(self, a):
        self.a = a
    def print_var1(self):
        print("The value of Parent class variables are:")
        print(self.a)
class Child(Parent):
    def __init__(self, a, b):
        Parent.__init__(self, a)
        self.b = b
    def print_var2(self):
        print("The value of Child class variables are:")
        print(self.b)
X=Child(10,20)
X.print_var1()
X.print_var2()


################ DATE TIME OPERATIONS##############
import  time    as  t
from    datetime    import  date
#Get today's date
now=date.today()
#Print Date ,Day and month
print "Date: " + now.strftime("%d-%m-%y")
print "Day of Week: " + now.strftime("%A")
print "Month: " + now.strftime("%B")

#Set new Date parameter
then = date(2013, 6, 7)
#find number of days between today and the new set date
timediff = now - then
print(timediff.days)



