# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.

from menu import menu

def start_app():
    print('Start!')
    menu()
    print('Goodbye!')


if __name__ == "__main__":
    start_app()