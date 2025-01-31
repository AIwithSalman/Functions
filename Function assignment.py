#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a class and fucntion, and list out the items in the list


# In[10]:


def subfieldinAI():
    fields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
    print(fields)


# In[11]:


subfieldinAI()


# In[ ]:


# Create a function that checks whether the given number is Odd or Even


# In[16]:


def oddEven():
    num=int(input("Enter the number:"))
    if((num%2)==1):
        print("Odd Number")
        message="Odd Number"
    else:
        print("Even Number")
        message="Even Number"
    return message


# In[17]:


message=oddEven()


# In[18]:


if(message=="Even Number"):
    print(" The given number is Even")
else:
    print("The given number is odd")


# In[ ]:


# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female


# In[26]:


def check_marriage_eligibility(age, gender):
    if gender.lower() == "male":
        if age >= 21:
            return "Eligible for marriage"
        else:
            return "Not eligible for marriage"
    elif gender.lower() == "female":
        if age >= 18:
            return "Eligible for marriage"
        else:
            return "Not eligible for marriage"
    else:
        return "Invalid gender"



# In[27]:


age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ")


# In[28]:


result = check_marriage_eligibility(age, gender)
print(result)


# In[29]:


# calculate the percentage of your 10th mark


# In[38]:


def calculate_percentage(subject1, subject2, subject3, subject4, subject5):
    total_marks = subject1 + subject2 + subject3 + subject4 + subject5
    percentage = (total_marks / 500) * 100
    print("Total Marks: " + str(total_marks) + " / 500")
    print("Percentage: " + str(round(percentage, 2)) + "%")


# In[39]:


calculate_percentage(98, 87, 95, 95, 93)


# In[ ]:


#print area and perimeter of triangle using class and functions


# In[45]:


class Triangle:
    def __init__(self, height, breadth, height1=None, height2=None):
        self.height = height
        self.breadth = breadth
        self.height1 = height1
        self.height2 = height2

    def area(self):
        # Area of triangle: (Height * Breadth) / 2
        return (self.height * self.breadth) / 2

    def perimeter(self):
        # Perimeter of triangle: Height1 + Height2 + Breadth
        if self.height1 and self.height2:
            return self.height1 + self.height2 + self.breadth
        else:
            return "Cannot calculate perimeter without additional sides"


# In[46]:


height = 32    
breadth = 34   
height1 = 2    
height2 = 4    

triangle = Triangle(height, breadth, height1, height2)


# In[47]:


print(f"Height: {triangle.height}")
print(f"Breadth: {triangle.breadth}")
print(f"Area formula: (Height * Breadth) / 2")
print(f"Area of Triangle: {triangle.area()}")

print(f"\nHeight1: {triangle.height1}")
print(f"Height2: {triangle.height2}")
print(f"Breadth: {triangle.breadth}")
print(f"Perimeter formula: Height1 + Height2 + Breadth")
print(f"Perimeter of Triangle: {triangle.perimeter()}")


# In[ ]:




