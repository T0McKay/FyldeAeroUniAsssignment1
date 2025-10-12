from inventory_database_classDec import InventoryDatabase
from inventory_item_classDec import InventoryItem
from system_classDec import SystemClass

system = SystemClass("admin123")

loggedIn = system.login()

print("")
newItem = InventoryItem()

print("")
newDatabase = InventoryDatabase()

newDatabase.addItem(newItem)
print("")
newDatabase.viewItems()
