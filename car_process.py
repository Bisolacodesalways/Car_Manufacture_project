#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Car_TUI as TUI
import csv
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def retrieve_car_details_by_id(details):
    TUI.started("retrieving car details")
    print("Enter Selected car_ID from 1 to 205: ") # Display message
    car_ID = int(input())
    # specifying the indexes by stating Car_ID position 1 is index 0 which brings about the negative sign.
    car_ID-=1  
    print(f"The individual car details based on the car_ID index {car_ID} are......\n") # Display message
    print(details[car_ID]) # Display message
    TUI.completed()
    
def get_cars_with_specified_cylinder_number(details):
    TUI.started("retrieving car details")
    car_details = []
    cylindernumber = input("Enter any of the cylinder numbers....2,3,4,5,6,8,12: ")
    print(f"The total car details based on   the cylinder number {cylindernumber} are....\n")
    # using list comprehension to retrieve the car details based on cylindernumber entered by the user
    car_cylinder_details = [x for x in details if x[13] == cylindernumber] 
    # display message
    print(car_cylinder_details)
    TUI.completed()
    
def retrieve_cars_for_a_specified_car_body(details):
    TUI.started("retrieving car details")
    car_details_for_a_specified_car_body = []
    print("Enter a specified car body based on the following..sedan,hatchback,wagon,convertible,hardtop: ")
    car_body = str(input())
    print(f"The total car details based on the specified car body {car_body} are.....\n") # Display message
    # using list comprehension to retrieve the car details based on car body entered by the user
    car_details_for_a_specified_car_body = [y for y in details if y[4] == car_body] 
    # display message
    print(car_details_for_a_specified_car_body)  
    TUI.completed()
                                           
def retrieve_specific_columns(details):
    TUI.started("retrieving specific car details")
    print("Enter Selected car_ID from 1-205: ") # Display message
    car_ID = int(input())
    # specifying the indexes by stating Car_ID position 1 is index 0 which brings about the negative sign .
    car_ID-=1 
    print(f"The specific columns(car_ID,fueltype,car_body,engine-location,car-length and car-height) related to an individual car by car_ID index {car_ID} are.......\n")
    car_ID = details[car_ID]
    car_record_based_on_ID = car_ID[0:11:2] # using slicing method to iterate the indexes and step 2 in iteration.
    # Display message
    print(car_record_based_on_ID)
    TUI.completed()

def retrieve_car_names_alphabetically(details):
    TUI.started("retrieving car names alphabetically")
    file_path = "Car_manufacture/CarPrice.csv" # specifying the file path
    df = pd.read_csv("Car_manufacture/CarPrice.csv",header=0) #load into a data frame
    Car_Names = input("Type 'Car Names' to retrieve the car names alphabetically:\n\n ")
    if Car_Names == 'Car Names':
        # group the data in the data frame(df) using pandas and group by function
        df_grouped = df.groupby(['CarName'])
        df_grouped = df.sort_values('car_ID')
        df_grouped = df_grouped.filter(['CarName','car_ID'])
        # Display message
        print(df_grouped)
    TUI.completed()
                                           
def retrieve_sales_summary(details):
    TUI.started("retrieving sales summary")
    # specifying file path
    df = pd.read_csv("Car_manufacture/CarPrice.csv",header=0) #load into a data frame
    car_sales_summary = input("Type 'total' to access the total sales for each car body:\n\n ")
    if car_sales_summary.lower() == 'total':
        # group the data in the data frame(df) using pandas and group by function
        df_grouped = df.groupby(['car_body']).sum()
        df_grouped = df_grouped.filter(['car_body','price'])
        print(df_grouped)
    TUI.completed()
                                           
def retrieve_top_5_car_sale(details):
    TUI.started("retrieving top 5 car sales per car body")
    df =  pd.read_csv("Car_manufacture/CarPrice.csv",header=0) #load into a data frame
    highest_top5_car_sale = input("Type 'highest sales' to access the 5 most expensive car for each body type:\n\n ")
    if highest_top5_car_sale.lower() == 'highest sales':
        #use panda sort and filter function to retrieve carbody and price data
        sorted_sales = df.sort_values(by = ["car_body", "price"], inplace =False, ascending=[1,0])
        sorted_sales = sorted_sales.filter(['car_body', 'price'])
        sorted_sales[0:5] # using slicing to get the indexes from 0 to 5 excluding index 5 after being sorted
        sorted_sales = sorted_sales.reset_index(drop = True)
        print(f"Top 5 most expensive cars per body type:\n\n {sorted_sales}")
    TUI.completed()     
      
def retrieve_selected_car_details(details):
    TUI.started("Showing total sales for each car name")
    data = np.loadtxt("Car_manufacture/CarPrice.csv",delimiter=",", dtype=str)
    df = pd.read_csv("Car_manufacture/CarPrice.csv",header=0) #load into a data frame
    total_sales = input("Type 'total' to access the total sales for each car name:\n\n ")
    if total_sales.lower() == 'total':
        #group data using car name and sum 
        df_grouped = df.groupby(['CarName']).sum()
        df_grouped = df_grouped.filter(['CarName','price'])
        print(df_grouped)
    TUI.completed()                                           
                                           
def display_no_of_cars_per_fuelsystem(details):
    TUI.started("Showing bar chart of cars per fuel system")
    df = pd.read_csv("Car_manufacture/CarPrice.csv")
    chart = input("Type 'display chart' to view information on the number of cars per fuel system:\n\n ")
    #using the value_count function to determine the number of cars per fuel system 
    fuel_system_sort  = df["fuelsystem"].value_counts()
    fuel_system = fuel_system_sort.tolist()
    car_no = fuel_system_sort.index.tolist()
    #plotting bar chart 
    fig = plt.figure() 
    plt.bar(car_no, fuel_system)
    plt.xlabel("Fuel System")
    plt.ylabel("No. of Cars")
    plt.title("Number of Cars per Fuel System")
    plt.show() # show the graph                                                           
    TUI.completed()                                      

def display_horsepower_of_top_5_car_sale(details):
    TUI.started("displaying chart of 5 most expensive cars in relation to horsepower")
    df = pd.read_csv("Car_manufacture/CarPrice.csv")
    plot = input("Type 'display chart' to view information on the horse power of the 5 cheapest cars :\n\n ")
        
    #sort data by cheapest price 
    df_plot = df.sort_values(by=["price"], ascending=True) [['CarName','horsepower']]
        
    #Create a new dataframe for 5 cheapest cars
    df_plot_5 = df_plot.head()
        
    fig, ax = plt.subplots(figsize=(15, 12))
    plt.suptitle("Horsepower of 5 Cheapest Cars ", fontsize=18, y=0.95)
        
    # retrieve the car name from the sorted dataframe and convert to list
    cars = df_plot_5['CarName'].tolist()
        
    # retrieve the horse power from the sorted dataframe and convert to list
    horsepower = df_plot_5['horsepower'].tolist()
        
    # use loop to get  through the length of car list in dataframe of 5 cheapest cars
    for i in range(len(df_plot_5['CarName'])):
        # using iteration indexes, add new subplot
        ax = plt.subplot(1, 5, i + 1)
        # filter df and plot horsepower on the new subplot axis
        ax.bar(cars[i],horsepower[i])
        #format chart 
        ax.set_ylim(0,100) 
    TUI.completed()
                                           
def display_customer_selection(details):
    TUI.started("displaying the chart showing the relationship btw purchased cars and cylinder number")
    df = pd.read_csv("Car_manufacture/CarPrice.csv",header=0) #load into a data frame
    plot = input("Type 'display chart' to view information on the  Purchased Car based on cylindernumber :\n\n ")
    
    #setting x and y variable
    x = df["cylindernumber"]
    y = df["price"] 
    fig = plt.figure()
    
    #plotting graph 
    plt.scatter(x, y, color='green',s=5)
    plt.xlabel('cylindernumber')
    plt.ylabel('Price')
    plt.title('Relationship between cylinder number and Car Price')
    plt.show()  # display chart
    TUI.completed()                                            
                                           
                                           


# In[ ]:




