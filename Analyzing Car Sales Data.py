#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from io import StringIO


# In[49]:


dataset = ('Make,Model,Year,Price,Mileage,Color,Location \n'
           'toyota, corolla, 2018,234,,black,karachi\n'
           'honda,civic,2019,456, 299.999,green,lahore\n'
          'ford,focus,2020,678,3999.67,white,landhi') 


# In[50]:


df = pd.read_csv(StringIO(dataset))


# In[51]:


df.to_csv('car_sales.csv')


# In[34]:


df.columns


# In[53]:


import pandas as pd

# Step 1: Read in the car_sales.csv file and create a DataFrame
df = pd.read_csv('car_sales.csv')

# Step 2: Display the first 5 rows of the DataFrame
print(df.head())

# Step 3: Determine how many cars are in the dataset
num_cars = len(df)
print("Number of cars in dataset:", num_cars)

# Step 4: Calculate the average price of a car in the dataset
avg_price = df['Price'].mean()
print("Average price of a car:", avg_price)

# Step 5: Determine the most common car make and model in the dataset
common_make_model = df.groupby(['Make', 'Model']).size().sort_values(ascending=False).reset_index(name='count').iloc[0]
print("Most common make and model:", common_make_model['Make'], common_make_model['Model'])

# Step 6: Create a new DataFrame that only contains cars made in the year 2021
df_2021 = df[df['Year'] == 2021]

# Step 7: Calculate the total mileage of all the cars in the dataset
total_mileage = df['Mileage'].sum()
print("Total mileage of all cars:", total_mileage)

# Step 8: Determine the average price of a car with less than 50,000 miles on it
avg_price_under_50k = df[df['Mileage'] < 50000]['Price'].mean()
print("Average price of a car with less than 50,000 miles:", avg_price_under_50k)

# Step 9: Create a new column in the DataFrame that indicates whether a car is "expensive" or "cheap"
df['Price Category'] = df['Price'].apply(lambda x: "expensive" if x > avg_price else "cheap")

# Step 10: Write the modified DataFrame to a new CSV file called car_sales_modified.csv
df.to_csv('car_sales_modified.csv', index=False)


# In[ ]:




