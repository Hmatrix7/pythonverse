#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program to check if a number is positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# In[11]:


# Mini Project 2: Simple Login System
username = "admin"
password = "Monkey"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Login successful. Welcome", user)
else:
    print("Invalid username or password")


# In[13]:


print("\n1.My name? ")
print("2.My Name.")
choice=input("Enter ur choice:")


# In[34]:


#🏦 Mini Project 1: ATM Machine Simulation
balance=500000

username = "admin"
password = "Monkey"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Login successful. Welcome", user)
    print("Hello welcome to Monkeys ATM")
    print("\n1.Check Balance")
    print("2.withdraw")
    print("3.Deposit")
    choice=int(input("Enter your choice"))
    if choice==1:
      print(f"Your balance is:{balance}")
    elif choice==2:
        amount=int(input("Enter withdraw amount"))
        if amount<=balance:
            balance-=amount
            print(f"withdraw successful,Your balance is:{balance}")
        else:
            print("Insufficient funds.")
    elif choice==3:
      deposite=int(input("Enter deposit amount"))
      balance+=deposite
      print(f"New balanceis:{balance}")
    else:
      print("Invalide choice")
else:
    print("Invalid username or password")


    


# In[15]:


##🏦 Mini Project 2: ATM Machine Simulation.02
balance = 5000

print("Welcome to Python Bank ATM")
pin = int(input("Enter your PIN: "))

if pin == 1234:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. New balance:", balance)
        else:
            print("Insufficient funds.")
    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful. New balance:", balance)
    else:
        print("Invalid choice")
else:
    print("Wrong PIN. Access Denied!")


# In[37]:


# Mini Project 3: Restaurant Menu
print("Welcome to Monkey Internet cafe ")
print("1.Preditor  2.Milkshake 3.Coffee 4.Creamcake")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Your choice is preditor ksh65")
elif choice==2:
    print("Your choice is milkshake ksh102")
elif choice==3:
    print("Your choice is coffee ksh401")
elif choice==4:
    print("Your choice is creamcake ksh232")
else:
    print("Invalide choice")


# In[47]:
# Mini Project 4:grade system

student_name=input("Enter your name: ")
math=int(input("Enter your math marks: "))
english=int(input("Enter your english marks: "))
science=int(input("Enter your science marks: "))
average = (math + english + science)/3
print(f"\nStudent Name: {student_name}")
print(f"Your math score: {math}")
print(f"Your english score: {english}")
print(f"Your science score: {science}")
if average>=90:
    print("Your are ok")
    print("Your grade is A")    
elif average>=80:
    print("Your light is getting dim")
    print("Your grade is B") 
elif average>=70:
    print("You live in the darkness")
    print("Your grade is c")
else:
    print("You are a failure")
    print("Your grade is f")
print(f"Average Score: {average:.2f}") #2f for two decimal places



# In[ ]:




