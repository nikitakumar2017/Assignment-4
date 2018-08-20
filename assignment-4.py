#Q.1- Reverse the whole list using list methods.
list1=[]
n=int(input("Enter number of elements you want to enter in the list "))
for i in range(n):
    n=int(input("Enter element "))
    list1.append(n)
print(list(reversed(list1))) 


#Q.2- Print all the uppercase letters from a string.
str1=input("Enter string ")
for i in str1:
    if (i>='A' and i<='Z'):
        print(i) 

#Q.3- Split the user input on comma's and store the values in a list as integers.
str1=input("Enter some numbers seperated by comma's ")
list1=[]
list2=[]
list1=str1.split(',')
for i in list1:
    i=int(i)
    list2.append(i)
print(list2) 

#Q.4- Check whether a string is palindromic or not.
str1=input("Enter a string ")
length=len(str1)
high=length-1
i=0
low=0
flag=0
while (i<length and flag==0):
    if(str1[low]==str1[high]):
        high-=1
        low+=1
        flag=0
    else:
        flag=1
    i+=1
if(flag==0):
    print("Yes")
else:
    print("No")


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
import copy as c
list1=[1,2,[3,4],5]
list2=c.deepcopy(list1)
list1[2][0]=7
print(list1)
print(list2)
''' Difference between shallow copy and deep copy is that in shallow copy if the original object contains any references to mutable object
then the duplicate reference variable will be created pointing to the old object and no duplicate object is created whereas in deep copy a duplicate object
is created. '''
