# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.

from menu import show_the_menu

def start_app():
    print('Start!')
    show_the_menu()
    print('Goodbye!')


if __name__ == "__main__":
    start_app()