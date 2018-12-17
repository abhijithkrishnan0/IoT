def printinfo(students):
    for studs in students:
        print studs
    return
def sumofmark(students):
    sum=0
    for studs   in  students:

        sum+=students[studs]['marks']
    return  sum