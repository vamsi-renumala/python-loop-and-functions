#!/usr/bin/env python
# coding: utf-8

# ### Loops and Functions

# #### -- if -- elif -- 1else

# In[1]:


a=20
b=33
if b>a:
    print("b is greater than a")


# In[2]:


a=40
b=33
if b>a:
    print("b is greater than a")
else:
    print("False");


# In[3]:


if a==b:
    print("true")
else:
    print("false")


# In[20]:


if a!=b:
    print("true")
else:
    print("false")


# In[21]:


time=int(input("enter the time : "))
if time>7:
    print("Attend the blackbucks.")


# In[19]:


marks=int(input("please enter your marks : "))
if marks>=50:
    print("congratulations \n you cleared the subject")
else:
    print("you failed \n Betterluck next time")


# In[18]:


a=9
b=7
c=5

if a>b:
  print("one digited")
elif b>c:
  print("two digited")
else:
  print("three digited")


# In[17]:


experience=int(input("enter your experience"))
if experience>15:
    print("extordinary")
elif experience>10:
    print("super")
else:
    print("good")


# In[16]:


age=int(input("Enter your age : "))
if age<5:
  print("no entry fee");
elif(age>5 and age<=13):
  print("fee is 100 rupees")
elif(age>13 and age<=50):
  print("fee is 30 rupees")
else:
  print("no entry fee")


# ### Loops

# ### 1.for

# #### for loop is used when we know the no of times the loop want to execute

# In[15]:


for i in "vamsi":
  if i=="i":
    break
  print(i)


# In[14]:


team=["sathwik","srinu","chari","vamsi"]
for names in range(0,len(team)):
  if names==3:
    break
  else:
    print(team[names])

  print("counter is " +str(names))


# In[13]:


team=["sathwik","srinu","chari","vamsi"]
for x in team:
  print(x)
  if x=="chari":
    break


# #### here print statement is above if: ,so it prints all except condition 

# In[12]:


team=["sathwik","srinu","chari","vamsi"]
for x in team:
  if x=="chari":
    break
  print(x)
  


# In[11]:


num=range(1,11)
addition=0
for i in num:
    addition=addition+i
    i=i+1
print("Addition is : ",addition)


# #### here print statement is below if: ,so it prints all before condition 

# ### while loops

# #### while loop is used when we don't know the no of times the loop want to execute

# In[10]:


num=range(1,11)
addition=0
for i in num:
    addition=addition+i
    i=i+1
print("Addition is : ",addition)


# ### Functions
# ### A block of reusable code that runs when called.

# #### 1.Built-in
# #### 2.User Defined
# #### 3.Lambda

# ### 1.Built-in

# In[6]:


print("hello","welcome to the session",sep=',')


# ### 2.user defined

# In[5]:


def greet(name):
  print("hello,",name,"welcome to the session.")

personname=input("Enter your name ")
greet(personname)


# In[4]:


def area_of_triangle(base,height):
  return(0.5*base*height)

base=int(input("Enter base value"))
height=int(input("Enter height value"))
area_of_triangle(base,height)


# ### 3.Lambda

# #### lambda arguments:expression

# In[1]:


x=lambda a:a+1
print(x(2))


# In[2]:


### greater number
def greater(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2
    
greater(10,20)


# In[3]:


greater=lambda num1,num2 : num1 if num1>num2 else num2
greater(10,20)


# In[8]:


print("hello")


# In[ ]:




