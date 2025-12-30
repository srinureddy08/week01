# shophing list
shopping_list = [] 
while True:
    print("\nChoose an action: add / remove / show / quit")
    choice = input("Enter your choice: ").lower()

    if choice == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added to the shopping list.")

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from the shopping list.")
        else:
            print("Item not found in the list.")

    elif choice == "show":
        if shopping_list:
            print("Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Shopping list is empty.")

    elif choice == "quit":
        print("Exiting Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
