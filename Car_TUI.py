#!/usr/bin/env python
# coding: utf-8

# Creating a text user Interface Module for the project implementation:Car_Manufacture

# In[5]:


# Specify a line width to display the layout of program
Line_width = 70

# function to display program start
def started(message=" "):
    output = f"Car manufacture project started: {message}..."
    dots = "." * Line_width
    # display message
    print(f"{dots}\n {output}\n")

# function to display program completion
def completed():
    dots = "." * Line_width
    # display message
    print(f"\n Car manufacture project completed.\n {dots}\n")
    
# function to display error message
def error(message):
    # display error message
    print(f"Error!!! {message}\n")
    
    
# function to display menu which will allow the user to select any option to perform operations
def display_menu():
    # program to allow user to select any option to get the details of any car
    print("""

    please select one of the following options:
    
    Retrieve car information
    [I] Option to retrieve an individual car details using the car_ID
    [II] Option to retrieve all cars for a specified cylinder number
    [III] Option to retrieve all cars for a specified car body
    [IV] Option to retrieve specific number (2 to 5) columns related to an individual car by the car_ID 

    Access some specific car details
    [V] Option to retrieve car names alphabetically
    [VI] Option to retrieve summary of sales i.e the total car price for each car body
    [VII] Option to retrieve the top 5 car sale by price (the most expensive) and per car body
    [VIII] Option to retrieve the details of cars based on your own selection

    Display specific visualization
    [IX]option to display/visualize the number of cars per fuel system using a bar chart
    [X] Option to display the horsepower of the top 5 car sale by price (the cheapest) using a 
    subplot
    [XI] Option to display the  the selection of data by your choice to present the customers’ buying 
    behaviour using a suitable visualisation

    """)
    selection = input("Your selection is: ")
    return selection.strip().lower()


# In[ ]:





# In[ ]:





# In[ ]:




