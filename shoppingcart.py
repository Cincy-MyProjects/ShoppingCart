class ItemToPurchase:
    def __init__(self,item_name="none",item_price=0,item_quantity=0):
        self.item_name=item_name
        self.item_name=item_name
        self.item_price=item_price
        self.item_quantity=item_quantity

    def print_item_cost(self):
        cost=self.item_quantity*self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${cost:.2f}")

print("Item 1\n")
item_name = input("Enter the item name:\n")
item_price = float(input("Enter the item price:\n"))
item_quantity = int(input("Enter the item quantity:\n"))
item1 = ItemToPurchase()
item1.item_name=item_name
item1.item_price=item_price
item1.item_quantity=item_quantity

print("Item 2\n")
item_name = input("Enter the item name:\n")
item_price = float(input("Enter the item price:\n"))
item_quantity = int(input("Enter the item quantity:\n"))

item2 = ItemToPurchase()
item2.item_name = item_name
item2.item_price = item_price
item2.item_quantity = item_quantity
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${total_cost}")
