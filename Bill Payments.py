#Restaurant

class Restaurant:
    def __init__(self):
        self.menu = {
            1: {"name": "Chicken Briyani", "price": 190},
            2: {"name": "Mutton Briyani", "price": 250},
            3: {"name": "Mutton Pepper", "price": 100},
            4: {"name": "Chicken Kabab", "price": 120},
            5: {"name": "Fish Fries", "price": 130},
            6: {"name": "Chicken Rice", "price": 120},
            7: {"name": "Chicken Lollipop", "price": 140},
            8: {"name": "Green Chilli", "price": 170},
            9: {"name": "Mutton Liver Masala", "price": 199},
            10: {"name": "Tandoori Chicken", "price": 220},
            11: {"name": "Tandoori Fish Tikka", "price": 190},
            12: {"name": "Prawn tawa Fry", "price": 290}
        }
        self.ordered_items = {}
        self.total = 0
        self.discount = 0
        self.payment = 0
        self.change = 0

#Display Menu List

    def display_menu(self):
        print("Menu list".center(21, "*"))
        for key, value in self.menu.items():
            print(f"{key}. {value['name']} - {value['price']}")

#Choice & Quantity

    def take_order(self):
        while True:
            choice = int(input("Enter your choice (0 to finish): "))
            if choice == 0:
                break
            quantity = int(input("How many: "))
            if choice in self.menu:
                self.ordered_items[choice] = quantity
                self.total += self.menu[choice]["price"] * quantity
            else:
                print("Invalid choice")

#Discount

    def calculate_discount(self):
        if self.total > 1500:
            self.discount = self.total * 0.3
            self.total -= self.discount

#Receipt

    def build_receipt(self):
        print("\nReceipt")
        print("==========")
        print("Master Restaurant")
        print("Number of persons:", len(self.ordered_items))
        print("Ordered items:")
        for key, value in self.ordered_items.items():
            print(f"{self.menu[key]['name']}: {value} x {self.menu[key]['price']} = {value * self.menu[key]['price']}")
        print("Total:", self.total)
        if self.discount:
            print("Discount (30%):", self.discount)
        print("Final Amount:", self.total)
        print("Payment Amount:", self.payment)
        print("Change:", self.change)
        print("Thank you for dining with us!")
        print("==========")

    def process_payment(self):
        self.payment = float(input("Enter payment amount: "))
        if self.payment >= self.total:
            self.change = self.payment - self.total
            self.build_receipt()
        else:
            print("Insufficient payment. Please pay the remaining amount.")

#Finally Print the value


def main():
    restaurant = Restaurant()
    print("Master Restaurant")
    num_persons = int(input("Enter number of persons: "))
    restaurant.display_menu()
    restaurant.take_order()
    restaurant.calculate_discount()
    print("Total:", restaurant.total)
    if restaurant.discount:
        print("Discount (30%):", restaurant.discount)
    print("Final Amount:", restaurant.total)
    restaurant.process_payment()

if __name__ == "__main__":
    main()
