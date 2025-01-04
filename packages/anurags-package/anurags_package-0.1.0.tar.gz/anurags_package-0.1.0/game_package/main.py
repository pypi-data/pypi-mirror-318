# main.py
def play():
    print("Welcome to the game!")
    # Your game logic goes here.
    while True:
        choice = input("Type 'quit' to exit: ").strip().lower()
        if choice == 'quit':
            print("Thanks for playing!")
            break
