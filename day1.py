#numbers
#integer
a=5
print "a is of type",type(a)
b=5.2
print "b is of type",type(b)
c=524134L
print "c is of type",type(c)
d=5+4j
print "d is of type",type(d)

#addition
e=a+b
print "sum of a and b ",e
#subtraction
e=a-b
print "diff of a and b ",e

#product

f=a*b
print "product of a and b ",f
#division
f=a/b
print "division of a by b ",f

#power

g=a**2
print "square of a is",g 


#Strings

s="my first string"
print(type(s))

#String concatenatiom

s="first string!!"
t="SECONDSTRING"
print "string 1: ",s,"\nstring 2: ",t,"\n concatenated string ",s+t

#length of string

print len(s)

#convert string to int
numString="1000"
numInt=int(numString)
print numInt

#convert to upper and lower cases

print(s.upper())
print(t.lower())

#Substrings

print s[5]
print s[:5],"\n",s[5:]

#using strip

print s.strip("!")


#Lists

#create list

fruits=["apple","mango","banana"]
print(type(fruits))

#length

print(len(fruits))

#access elements

print fruits[1]
print fruits[1:3]
print fruits[1:]

#append item
fruits.append("pear")
print fruits

#remove item
fruits.remove("mango")
print fruits

#insert element
fruits.insert(1,"mango")
print fruits

#combine list

vegetables=["tomato","potato","carrot"]
eatable=fruits+vegetables
print eatable

#Mixed data type

mixed=["data",5,100.1,8287398L]
print(type(mixed))


#tuples

fruits=("apple","mango","banana","pineapple")
print fruits

#length
print len(fruits)

#get element
print fruit[0]
print fruit [1:]

#combine tuples

vegetables=("potato","carrot","onion","radish")
eatable=vegetable+fruits
print eatable
