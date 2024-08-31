import secrets
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate a secure random password based on specified criteria."""
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")

    return ''.join(secrets.choice(characters) for _ in range(length))


def get_user_input():
    """Collect user input for password generation settings."""
    try:
        num_passwords = int(input("Enter number of passwords: "))
        length = int(input("Enter password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        return num_passwords, length, use_uppercase, use_lowercase, use_digits, use_symbols
    except ValueError as e:
        print(f"Error: {e}")
        return None


def display_passwords(num_passwords, length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate and display passwords, with an option to copy each to the clipboard."""
    for _ in range(num_passwords):
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        print(f"Generated Password: {password}")

        if input("Copy to clipboard? (y/n): ").lower() == 'y':
            pyperclip.copy(password)
            print("Password copied to clipboard!")


def main():
    """Main function to run the password generator program."""
    user_input = get_user_input()
    if user_input:
        num_passwords, length, use_uppercase, use_lowercase, use_digits, use_symbols = user_input
        display_passwords(num_passwords, length, use_uppercase, use_lowercase, use_digits, use_symbols)


if __name__ == "__main__":
    main()
