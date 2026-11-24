from data import play, stats

def show_the_menu():
    print("===== RECIPE BOX =====")
    print("1. Add a recipe")
    print("2. View all recipes")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")
    if choice == "1":
        play()
    elif choice == "2":
        stats()
    elif choice == "3":
        print("Goodbye")
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")