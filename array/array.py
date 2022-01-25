#creating an array
from array import *
from cmath import e
from xml.dom.minidom import Element
a1=array('i',[1,2,3,4])  #'i' is type of array , [1,2,3,4,]=initialisers
a2=array('d',[1.6,2.1,3,5,4.1]) 
print(a1)
print(a2)

#adding elements at the end
a1.insert(4,5)
print(a1)

#adding elemts at the beginning
a1.insert(2,9)
print(a1)

#traversing array
a3=array('i',[1,2,3,4,5])
def traverse(a3):
    for i in a3:
        print(i)
traverse(a3)

#accessing elements in an array
def access_array(array,index):
    if index > len(array):
        print("there is no element at this index")
    else:
        print("accessing array")

        print(array[index])

access_array(a3,12)

#searching elements in array
def search_array(array,element):
    for i in range(len(array)):
        if array[i]==element:
            print(f'element {element} is present at index {i}')
            break
    print(f'the element {element} does not exist in array')
        
search_array(a3,7)

#removing element of array
def remove_element(array,e):
    array.remove(e)
    print(array)

remove_element(a3,3)



