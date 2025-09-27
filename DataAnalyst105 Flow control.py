#!/usr/bin/env python
# coding: utf-8

# In[6]:


for i in range(1,6):  # round bracket are used for range
    print(i)


# In[7]:


for i in range(6):
    print(i)
    


# In[8]:


count=1 #initialize
while count<=10: #condition
    print(count) #statements
    count += 1 #incremeant


# In[9]:


#print odd numbers btw 1 and 20
for i in range(1,20):
    if i % 2 == 0:
        continue
    print(i)
    


# In[10]:


for i in range(1,10): #printing even numbers
    if i % 2 == 1:
        continue
    print(i)


# In[11]:


#Loop with Strings
for letter in "Python":
    print(letter)


# In[16]:


#Nested Loops
for i in range(1,5):
    for j in range(6,10):
        print(i,j)


# In[14]:


for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")


# In[ ]:




