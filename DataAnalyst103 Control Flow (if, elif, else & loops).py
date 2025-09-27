#!/usr/bin/env python
# coding: utf-8

# In[14]:


#check if a number is even or odd
b = 17  # You can change this to any integer

if b % 2 == 0:
    print(f"{b} is even.")
else:
    print(f"{b} is odd.")


# In[15]:


#user input
name = input("Enter your name: ")
print(f"Hello, {name}!")


# In[16]:


#If...else statements
age= int(input("Enter your age: "))
if age>= 18:
    print(f"You are {age} years old.")
    print("Age Verification successful")
else:
    print(f"You are {age} years old.")
    print("Age Verification failed")


# In[17]:


# if statements
age = 20
if age >= 18:
    print("You are an adult")


# In[18]:


#If…elif…else
marks = int(input("Enter your maths score: "))
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# In[30]:


#For loops Used to iterate over sequences (list, tuple, string, etc.)
fruits = ["Apples","Bananas","Oranges","Mangoes","cherry"]
for fruit in fruits:
    print(fruit)


# In[31]:


#for loop in range
for i in range(5):
    print(i)


# In[34]:


#while loop runs as long as the condition is true
count=1 #intialization
while count<=3:  #condition
    print(count) #Action..statement
    count+=1 #increment


# In[44]:


# Break and Continue, break: exit loop, continue: skip current iteration
for i in range(int(input("Enter range"))):
    if i == 3:
        continue #used to skip the iteration
    if i == 7:
        continue #can be used multiple times
    if i == 9:
        continue
    if i == 13:
        continue
    if i == 19:
        break    #stops at 19 in a range of 24 
    print(i)


# In[55]:


for i in range(int(input("Enter range"))):
    if i % 3 == 0:
        continue
    if i == 20:
        break
    print(i)


# In[1]:


# Nested if
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("Only citizens can vote")
else:
    print("You are too young to vote")


# In[ ]:




