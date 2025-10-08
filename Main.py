from inventory_item_classDec import InventoryItem

print("")
newItem = InventoryItem()
print("")

print(f"Name         : {newItem.name}")
print(f"Product code : {newItem.productCode}")
print(f"Expiry Date  : {newItem.expiryDate.strftime('%m/%d/%Y')}")
print(f"Quantity     : {newItem.quantity}")
print(f"Location     : {newItem.location}")
