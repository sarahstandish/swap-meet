class Vendor:
    
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        
        self.inventory.append(item)

        return item

    def remove(self, item):

        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return None

    def get_by_category(self, category):
        
        items_in_category = []

        for item in self.inventory:
            if item.category == category.title():
                items_in_category.append(item)

        return items_in_category

    def has_item(self, item):
        return item in self.inventory

    def swap_items(self, vendor2, item1, item2):
        
        if self.has_item(item1) and vendor2.has_item(item2):
            self.remove(item1)
            vendor2.add(item1)
            vendor2.remove(item2)
            self.add(item2)
            return True

        return False

    def swap_first_item(self, vendor2):
        if self.inventory and vendor2.inventory:
            first_item1 = self.inventory[0]
            first_item2 = vendor2.inventory[0]
            self.remove(first_item1)
            vendor2.add(first_item1)
            vendor2.remove(first_item2)
            self.add(first_item2)
            return True

        return False
