# Pranav Annapareddy and Arjun Talati
def encode(password):
    encPassword = ""
    if len(password) != 8 or not password.isdigit():
        print("Invalid input. Password must be an 8-digit string containing only integers.")
        return None

    for digit in password:
        encDigit = str((int(digit) + 3) % 10)
        encPassword += encDigit

    return encPassword

def decode(encPassword):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter a password to encode: ")
            encPassword = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            decPassword = decode(encPassword)
            print(f"The encoded password was {encPassword} and the original password was {decPassword}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == '__main__':
    main()
