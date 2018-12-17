#Type conversion
a=1000
b=str(a)
print "Integer variable" 
print   a
print "\n String value"
print b

#Conditional statements

a=3
b=5
if a>b:
    print"a is larger"
else:
    print "b is larger"

#string check in conditional statements

str1="Isengard"
str2="Is"
print "str1 is"
print str1
print "str2 is "
print str2
print "Checking if str2 is str1"
if str2 in str1:
    print "True"
else:
    print "false"

#check for key

students={'name':'Mary','id':'8776'}
if students.has_key('age'):
    print "key found"
else:    
    print "no key"

#For statements

helloString="ABcdEF"

for c in helloString:
    print c

fruits=['apple','mango','watermelon','strawbverry']
for item in fruits:
    print item

