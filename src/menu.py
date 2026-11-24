from data import play, stats

def show_the_menu():
    print("===== ROCK PAPER SCISSORS =====")
    print("Start")
    print("Stats")
    print("Exit")
    choice = input("Choose an option: ")
    if choice == "Start":
        play()
    elif choice == "Stats":
        stats()
    elif choice == "Exit":
        print("Goodbye")
    else:
        print("Invalid choice.")