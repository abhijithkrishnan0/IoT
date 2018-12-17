#while statement

i=0
while i<10:
    if (i%2==0):
        print "even"
    else:
        print "odd"
    i+=1

#Range statement with AP and without AP

#Without AP
nums=range(10)
print(nums)

#with AP ,common diff =2
nums=range(0,10,2)
print nums




#Use continue and break statements

#Use of break statemnets
y=1
for x in range(4,256,4):
	y = y * x
	if y > 512:
		break
	print y

#Using continue statement

fruits=['apple','orange','banana','mango']
for item in fruits:
        if (item=='banana'):
            continue
        else:
            print item

#Using pass statements

fruits=['apple','orange','banana','mango']
for item in fruits:
        if (item=='banana'):
            pass
        else:
            print item


#Program 1

numlist=list()
while(True):
    inp=raw_input('Enter a number')
    if inp=="done":
        break
    value=float(inp)
    numlist.append(value)
print(numlist)
print(max(numlist))
print(min(numlist))
