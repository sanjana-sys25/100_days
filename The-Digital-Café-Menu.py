def cafe_checkout():
    # 1. Define the menu dictionary
    menu = {
        "Espresso": 3.50,
        "Latte": 4.25,
        "Cappuccino": 4.50,
        "Croissant": 3.75,
        "Muffin": 3.00,
        "Avocado Toast": 7.50
    }
    
    # Initialize the running total and the receipt list
    running_total = 0.0
    receipt = []
    
    print("Welcome to the Python Café!")
    print("--------------------------")
    print("Menu:")
    for item, price in menu.items():
        print(f" - {item}: ${price:.2f}")
    print("--------------------------")
    print("Type your item to order, or type 'done' to finish.\n")
    
    # 2. Main ordering loop
    while True:
        # .title() normalizes input so "espresso" or "ESPRESSO" matches "Espresso"
        user_input = input("What would you like to order? ").strip().title()
        
        if user_input == "Done":
            break
            
        # 3. Look up the price and update totals
        if user_input in menu:
            price = menu[user_input]
            running_total += price
            receipt.append(user_input)  # Bonus: Add to receipt list
            print(f"Added {user_input} (${price:.2f}) to your order. Current total: ${running_total:.2f}\n")
        else:
            print("Sorry, that item isn't on the menu. Please try again.\n")
            
    # 4. Bonus Challenge: Print a beautiful receipt
    print("\n==============================")
    print("         PYTHON CAFÉ          ")
    print("           RECEIPT            ")
    print("==============================")
    
    if not receipt:
        print("No items ordered.")
    else:
        for item in receipt:
            # Dynamically aligns the price to the right side
            print(f"{item:<20} ${menu[item]:>5.2f}")
            
    print("------------------------------")
    print(f"Total Bill:          ${running_total:>5.2f}")
    print("==============================")
    print("    Thank you for visiting!   ")

# Run the program
cafe_checkout()