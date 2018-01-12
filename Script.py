import codecademylib
import pandas as pd

#Reading the csv file in order to view it in the terminal. csv cotains dataset
inventory = pd.read_csv('inventory.csv')

#Viewing the first 10 lines of the dataset(lines 0-9)
staten_island = inventory.head(10)

#Selecting the 'location' and 'product_description' columns from the dataframe(inventory)
product_request = inventory[['location', 'product_description']] 

#Selecting the 'Brooklyn' locations and product_type 'seeds' 
seed_request = inventory[(inventory.location =='Brooklyn') & (inventory.product_type=='seeds')]

#Using lambda function to state that if x>0, then the inventory is in stock.  
inventory['in_stock'] = lambda x: True \
    if x>0 \
    else False

get_stock = lambda x: True \
    if x > 0 \
    else False

#Making sure that the 'in stock'column is associated with the 'quantity' column  
inventory['in_stock'] = inventory.quantity.apply(get_stock)

#This determines the total value of the inventory 
inventory['total_value'] = inventory.price * inventory.quantity

#using lambda to format the row and combine the two together
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
#Getting the full description of the variable by adding the 'product_type' column to the 'product_description' column
inventory['full_description'] = inventory.product_type + inventory.product_description 
                     
#print the inventory  
print(inventory)




