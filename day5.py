#from day4 import modlist
import  students as stu
students={'1':{'name':'abhi','marks':20},'2':{'name':'abhis','marks':20},'3':{'name':'abhawfi','marks':20}}
print(stu.sumofmark(students))


#File Handling

#Write content into file

fp=open('file.txt','w')
content='abcdsnvfhw\nesjfwifh\njkkvfasif\n'
fp.write(content)
fp.close()

# Read entire file
fp=open('file.txt','r')
content=fp.read()
for line    in  content:
    print(line)
fp.close()

#Read line by line from file
fp=open('file.txt','r')
content=fp.readlines()
for line    in  content:
    print(line)
fp.close()

#Seek to certain position
fp=open('file.txt','r')
fp.seek(3,1)
content=fp.read(5)
print content


#Tell current position
print(fp.tell)
##### TODO#########
