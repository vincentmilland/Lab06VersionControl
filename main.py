# This is Vincent Milland's file
def encode(password):
    # Ensuring the password is 8-digit and only contains integers
    if not (password.isdigit() and len(password) == 8):
        print("Invalid password. Please enter an 8-digit password containing only integers.")
        return None

    # Shifting each digit up by 3
    encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded_password


def decode(password):
    length = len(password)
    i = 0
    afterdecoding = ""
    while i < length:
        afterdecoding = afterdecoding + str((int(password[i]) - 3) % 10)
        i = i + 1
    return afterdecoding

def main():
    encoded_password = None
    original_password = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode(original_password)
            if encoded_password:
                print("Your password has been encoded and stored!")
        elif option == '2':
            original_password = decode(encoded_password)
            print("The encoded password is " + encoded_password + ", and the original password is "
                  + original_password + ".")
        elif option == '3':
            break  # Exiting the loop to quit the program
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
