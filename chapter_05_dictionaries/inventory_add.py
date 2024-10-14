import inventory

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        print(item)
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
inventory.displayInventory(inv)