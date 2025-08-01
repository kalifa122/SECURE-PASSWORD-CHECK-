import string

def check_password_strength(password: str) -> dict:
    """
    Checks the complexity of the password.
    Returns a dictionary indicating whether each criterion is met.
    """
    return {
        "Length ≥ 8 characters"       : len(password) >= 8,
        "Contains an uppercase letter": any(c.isupper() for c in password),
        "Contains a lowercase letter" : any(c.islower() for c in password),
        "Contains a digit"            : any(c.isdigit() for c in password),
        "Contains a special character": any(c in string.punctuation for c in password),
    }

def is_strong_password(password: str) -> bool:
    """
    Returns True if the password meets all security criteria.
    """
    return all(check_password_strength(password).values())

if __name__ == "__main__":
    pwd = input("🔐 Enter a password to check: ").strip()

    if not pwd:
        print("\n⚠️ No password entered. Please try again.")
    else:
        results = check_password_strength(pwd)
        
        print("\n🔎 Password evaluation:")
        for criterion, is_valid in results.items():
            print(f" - {criterion:<35} : {'✅' if is_valid else '❌'}")

        if is_strong_password(pwd):
            print("\n✅ Strong password!")
        else:
            print("\n❌ Weak password. Please choose a more complex one.")
