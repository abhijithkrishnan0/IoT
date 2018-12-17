# -*- coding: utf-8 -*-
#Functions 

def addition(numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    return sum

numbers=[1,1,1,1,1]
sum=addition(numbers)
print sum

students = { '1': {'name': 'Bob', 'grade': 2.5},
	        '2': {'name': 'Mary', 'grade': 3.5},
	        '3': {'name': 'David', 'grade': 4.2},
	        '4': {'name': 'John', 'grade': 4.1},
	        '5': {'name': 'Alex', 'grade': 3.8}
            }

def averageGrade(students):
          
    sum = 0.0
    for key in students:
	    sum = sum + students[key]['grade']
    average = sum/len(students)
    return average

avg = averageGrade(students)
print ("The average grade is: %0.2f" % (avg))
			




# Functions with default values

def printinfo(name="Abhijith",age=21):
    print 'Name ',name
    print 'Age ',age
    return

print("enter name and age")
name=raw_input()
age=input()
print("\n Entered values")
printinfo(name,age)
print("\n default values")
printinfo()


#Functions: Passing by Reference

print("\n\n Example for pass by reference")

def modlist(mylist):
    j=0
    for i in mylist:
        mylist[j]=i+10
        j=j+1
    return

print 'original list'
list=[10,20,30,40]
print list
modlist(list)
print 'modified list (incremented by 10)\n',list

#Functions Keyword argument
print("\n \n")
def printStudentRecords(name,age=20,major="CS"):
	print( "Name: " , name)
	print ("Age: " , age)
	print ("Major: " , major)



printStudentRecords(name="Alex")
printStudentRecords(name="Bob",age=22,major="ECE")
printStudentRecords(name="Alan",major="ECE")


#Functions with variable length

print("\n \n\nExample for variable length passing into function")
def printinfo( arg1, *vartuple ):
	print ("Output is: ") 
	print (arg1) 
	for var in vartuple: 
		print (var) 
	return 

printinfo( 10 ) 
printinfo( 70, 60, 50 )




