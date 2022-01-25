from importlib.abc import Traversable
import numpy as np

#creating 2D array
twodarray=np.array([[11,15,10,5],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twodarray)

#adding elements
#adding columns or rows
newarray=np.insert(twodarray,0,[[1,2,3,4]],axis=1)
print(newarray)
#appending columns or rows
newarray_1=np.append(newarray,[[1,2,3,4,5]],axis=0)
print(newarray_1)

#access elements
def accesselements(array,row,column):
    if row>=len(array) and column>=len(array[0]):
        print("incorrect index")
    else:
        print(array[row][column])
accesselements(newarray_1,2,2)

def traverse(array):
    for i in range(len(array)): #for getting length of array the total element in the array
        for j in range(len(array[0])): #for getting length of column , the total element in the any element
            print(array[i][j],end="")
            print(end=" ")
        print()

traverse(newarray_1)


#searching element in 2D array

def search2d(array,n):
    value=False
    for i in range(len(array)): #for getting length of array the total element in the array
        for j in range(len(array[0])): #for getting length of column , the total element in the any element
            if array[i][j]==n:
                print(f"element {n} present in the array in the {i} row and {j} column")
                value=True
    if value==False:
        print(f'element {n} is not present in the array')
                

search2d(newarray_1,100)

#deleting row or column

new2Darray=np.delete(newarray_1,0,axis=1)  #axis 0 for row and axis 1 for column
print(new2Darray)
