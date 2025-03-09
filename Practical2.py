#Array
first_array = [7, 2.3, True, "Sonam", None]
first_array.append(3)
#append will add in the element in the array 
# python already knows it has 5 element si it will put 3 in the array and not create another copy
#only some function will create a copy(Reassignment)                                                           
firstArrayLength = len(first_array)

second_Array =[7, 2.3, True, "Sonam", None]
secondArrayLength = len(second_Array)
print(firstArrayLength - secondArrayLength)






#logic about Index(it shows position)(starts from 0)
#logic about array length(it will show number of elements)(starts from 1)
#because array is a contigous set(has defined set of sequencing)

#python list is an array


# LOOP

ProgramList = ["Civil","EE","ECE","MECH","IT","Arch","SWE" ,"WRE","EG","ICE"]
arrayLength = len(ProgramList)

for i in range(arrayLength):
    print(ProgramList[i])
    

# while loop

ProgramList = ["Civil","EE","ECE","MECH","IT","Arch","SWE" ,"WRE","EG","ICE"]
arraylen = len(ProgramList)
index = 0
while index < arraylen:
    print(ProgramList[index])
    index = index + 1 