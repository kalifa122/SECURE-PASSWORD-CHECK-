import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    """
    Generates a secure password.
    
    :param length: Length of the password
    :param use_digits: Include digits?
    :param use_specials: Include special characters?
    :return: A string representing the generated password
    """
    if length < 6:
        raise ValueError("Minimum password length is 6 characters.")

    characters = list(string.ascii_letters)
    if use_digits:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()-_=+[]{};:,.<>?/|")

    if not characters:
        raise ValueError("No characters available to generate the password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated password:", generate_password())
