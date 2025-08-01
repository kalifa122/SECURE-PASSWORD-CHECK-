import hashlib
import string
import requests

def check_password_strength(password: str) -> dict:
    """
    Vérifie la complexité du mot de passe.
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
    Retourne True si le mot de passe respecte tous les critères.
    """
    return all(check_password_strength(password).values())

def check_pwned_api(password: str) -> int:
    """
    Vérifie si le mot de passe a été compromis dans une fuite (via l'API Have I Been Pwned).
    Retourne le nombre de fois que le mot de passe est apparu dans des fuites.
    """
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError("Erreur lors de la connexion à l'API Have I Been Pwned")

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

if __name__ == "__main__":
    try:
        pwd = input("🔐 Entrez un mot de passe à tester : ").strip()

        if not pwd:
            print("\n⚠️ Aucun mot de passe saisi.")
        else:
            print("\n🔍 Vérification de la complexité...")
            results = check_password_strength(pwd)
            for critère, est_valide in results.items():
                print(f" - {critère:<35} : {'✅' if est_valide else '❌'}")

            if is_strong_password(pwd):
                print("\n✅ Complexité suffisante !")
            else:
                print("\n❌ Mot de passe trop faible.")

            print("\n🔎 Vérification dans les bases de données compromises...")
            try:
                count = check_pwned_api(pwd)
                if count:
                    print(f"⚠️ Ce mot de passe a été trouvé {count} fois dans des fuites de données.")
                    print("❗ Choisissez un mot de passe différent.")
                else:
                    print("✅ Ce mot de passe ne figure pas dans les bases compromises (jusqu’à aujourd’hui).")
            except Exception as e:
                print(f"Erreur lors de la vérification Pwned : {e}")

    except KeyboardInterrupt:
        print("\n⛔ Interruption par l'utilisateur.")
