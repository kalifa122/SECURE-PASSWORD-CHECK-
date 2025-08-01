🔐 Secure Password Generator
This is a simple and secure Python-based password generator that allows users to create strong and customizable passwords. It includes options to choose the length of the password and whether to include digits and special characters.

🚀 Features

Generate random passwords with:

Uppercase and lowercase letters

Digits (optional)

Special characters (optional)

Set the desired password length (minimum 6 characters)

Command-line interface for ease of use

🛠 Requirements

Python 3.x

No additional libraries are required — only Python’s standard library is used.

📦 Installation

Clone or download this repository:

git clone https://github.com/kalifa122/SECURE-PASSWORD-CHECK-.git

cd secure-password-tool

Run the program:

python main.py

📄 Usage

When you run the script, it will generate and display a secure password using default settings:

$ python main.py

Generated password: Kd!3vLp@2qRs

To customize the password generation, you can modify the parameters in the generate_password function in main.py:

generate_password(length=16, use_digits=False, use_specials=True)

🧪 Example Output

Generated password: mB9!pz3$Fk2L

📌 Notes

The minimum password length is set to 6 characters.

If no character types are selected, the program will raise an error.

📝 License

This project is licensed under the MIT License — feel free to use and modify it as needed.

