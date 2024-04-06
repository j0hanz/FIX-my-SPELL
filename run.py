import word_art

def main():
    print(word_art.welcome)
    print("Hello! ⊂(◉‿◉)つ".ljust(200))
    
    while True:
        name = input("Enter your name please: ").capitalize()
        if not name.isalpha():
            print(f'Is that your name? Nah try again.\n')
        else:
            break
main()
