# InventorySystem

## Inventory system using Django in Python.

To run the project:

Download the repo.<br/>
In a command prompt, cd to the mysite directory.<br/>
Execute '$ python manage.py runserver' to start a local SQLite database.<br/>
Finally, in your browser go to 'http://localhost:8000/inventory/'<br/>


## Comments:

I've added an expiry_date field to the requirement for an inventory item in the case where the items are perishable.<br/>
With this I added an option to view all items due to expire in the next 2 days or that have already expired.<br/>
Unfortunately, I ran out of time to allow blank entries for expiry in the case of non-perishables.<br/>
<br/>
I also ran out of time to get the "Get all items from inventory for a given category" and "Get all items from inventory between a given price range" queries working.<br/>
<br/>
