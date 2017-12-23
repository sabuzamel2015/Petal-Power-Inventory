import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory.head(10)

product_request = inventory[['location', 'product_description']] 

seed_request = inventory[(inventory.location =='Brooklyn') & (inventory.product_type=='seeds')]

inventory['in_stock'] = lambda x: True \
    if x>0 \
    else False

get_stock = lambda x: True \
      if x > 0 \
      else False
    
inventory['in_stock'] = inventory.quantity.apply(get_stock)

inventory['total_value'] = inventory.price * inventory.quantity

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.product_type + inventory.product_description 
                     
  
print(inventory)




