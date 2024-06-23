class ItemToPurchase:
    def __init__(self,item_name="none",item_description="none",item_price=0.0,item_quantity=0):
        self.item_name=item_name
        self.item_description=item_description
        self.item_price=item_price
        self.item_quantity=item_quantity

    def print_item_cost(self):
        cost=self.item_quantity*self.item_price
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${cost:.2f}")

class ShoppingCart:
    def __init__(self,customer_name="none",current_date="January 1, 2020"):
        self.customer_name=customer_name
        self.current_date=current_date
        self.cart_items =[]

    def add_item(self,item):
        self.cart_items.append(item)

    def remove_item(self,itemtoremove_name):
        itemtoremove_found = False
        for item in self.cart_items:
            if item.item_name==itemtoremove_name:
                self.cart_items.remove(item)
                itemtoremove_found=True
                break
            if not itemtoremove_found:
                print("Item not found in cart. Nothing removed.")

    def modify_item(self,modify_item):
        item_found = False
        for item in self.cart_items:
            if item.item_name == modify_item.item_name:
                item_found = True
                if modify_item.item_description != "none":
                    item.item_description = modify_item.item_description
                if modify_item.item_price != 0.0:
                    item.item_price = modify_item.item_price
                if modify_item.item_quantity != 0:
                    item.item_quantity = modify_item.item_quantity
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}")
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:\n")

        if choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)

        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            description = input("Enter the item description (leave blank if no change):\n")
            price = input("Enter the item price (leave blank if no change):\n")
            quantity = input("Enter the item quantity (leave blank if no change):\n")
            description = description if description else "none"
            price = float(price) if price else 0.0
            quantity = int(quantity) if quantity else 0
            modified_item = ItemToPurchase(name, description, price, quantity)
            cart.modify_item(modified_item)

        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == 'q':
            break

        else:
            print("Invalid option. Please try again.")

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print_menu(cart)

if __name__ == "__main__":
    main()
