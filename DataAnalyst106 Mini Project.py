#!/usr/bin/env python
# coding: utf-8

# In[15]:


cart = []
while True:
    item = input("Enter item to add (or 'done' to finish): ")
    if item == "done":
        break
    cart.append(item)

print("\nYour Shopping Cart:")
for product in cart:
    print("-", product)


# In[16]:


cart=[]
while True:
    item=input("Enter")
    if item == "done":
        break
    cart.append(item)

print("\nYour Shopping Cart:")
for product in cart:
    print("-",product)


# In[17]:


cart = []
total = 0

while True:
    item = input("Enter item to add (or 'done' to finish): ")
    if item.lower() == "done":
        break
    
    price = float(input(f"Enter price for {item}: "))
    
    # Store item and price as a tuple
    cart.append((item, price))
    
    # Add to total
    total += price

# Show results
print("\n🛍️ Your Shopping Cart:")
for product, price in cart:
    print(f"- {product}: {price} KES")

print("\n💰 Total Bill:", total, "KES")


# In[3]:


# Create an empty list
friends = []

# Ask user for 3 friends' names
for i in range(3):
    name = input(f"Enter the name of friend {i+1}: ")
    friends.append(name)

# Show the list of friends
print("\nYour friends are:", friends)


# In[5]:


friends = []
count = 0  # keep track of how many friends entered

while True:
    name = input("Enter a friend's name: ")
    friends.append(name)
    count += 1

    if count == 3:   # stop after 3 friends
        break

print("\nYour friends are:", friends)



# In[ ]:




