from inventory_database_classDec import InventoryDatabase
from inventory_item_classDec import InventoryItem

print("")
newItem = InventoryItem()

print("")
newDatabase = InventoryDatabase()

newDatabase.addItem(newItem)
print("")
newDatabase.viewItems()
