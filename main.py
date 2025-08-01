from password_checker import check_password_strength, is_strong_password
from pwned_check import check_password_strength, is_strong_password
from password_generator import generate_password

def main():
    print("🔐 Password Strength Checker")
    password = input("\nEnter a password to evaluate: ").strip()

    if not password:
        print("⚠️ No password entered.")
        return

    results = check_password_strength(password)

    print("\n🔎 Password Evaluation:")
    for criterion, is_valid in results.items():
        print(f" - {criterion:<35} : {'✅' if is_valid else '❌'}")

    if is_strong_password(password):
        print("\n✅ Strong password!")
    else:
        print("\n❌ Weak password. Please choose a more complex one.")
        
        # Suggest a strong generated password
        print("\n💡 Suggestion: Here is a strong password generated for you:")
        suggestion = generate_password(length=14, use_digits=True, use_specials=True)
        print(f"🔐 {suggestion}")

if __name__ == "__main__":
    main()
