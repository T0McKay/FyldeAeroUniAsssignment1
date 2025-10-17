from inventory_database_classDec import InventoryDatabase
from inventory_item_classDec import InventoryItem
from system_classDec import SystemClass


fyldeAeroInvSystem = SystemClass("admin123")
loggedInUserID = fyldeAeroInvSystem.login()

fyldeAeroInvSystem.menu()
