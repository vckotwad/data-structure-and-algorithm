from array import *

#create an array and traverse
a1=array('i',[1,2,3,4,5])
for i in a1:
    print(i)

#access element thourgh indexes
for i in range(len(a1)):
    print(a1[i])

#append any value to the array using append method
a1.append(6)
print(a1)

#insert value in an array using insert method
a1.insert(0,6)
print(a1)

#extend python array using extend method
a1.extend([1,2,3])
print(a1)

#add items from list into array using fromlist() method
l1=[1,2,3,4]
a1.fromlist(l1)
print(a1)

#remove any array elemtn using remove() method
a1.remove(6)
print(a1)

# remove last array element using pop() method
a1.pop()
print(a1)

# fetch any element though its index using index() method
print(a1.index(6))

# reverse a python array using reverse() method
a1.reverse()
print(a1)

# get array buffer info though buffer_info() method
print(a1.buffer_info())

# check for  number of occurance of an element using count() method
print(a1.count(1))

# convert arra to a python list with some element using tolist() method
l2=a1.tolist()
print(l2)

# slice element from an array
print(a1[0:5:2])