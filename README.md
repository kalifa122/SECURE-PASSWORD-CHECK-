🔐 Secure Password Tool
A simple and secure Python-based password management tool with a graphical interface (Tkinter).
This tool allows you to:

Generate strong passwords.

Check their strength against predefined criteria.

Verify if the password has been compromised using the Have I Been Pwned API.

🚀 Features
✅ Generate secure passwords with:

Uppercase and lowercase letters

Digits (optional)

Special characters (optional)

Customizable length (minimum 6 characters)

✅ Password strength checker

Checks length and character variety

Shows how many criteria are met (out of 5)

✅ Pwned password check

Uses the Have I Been Pwned API to see if a password has appeared in known breaches

✅ Copy to clipboard

Quickly copy generated passwords

✅ User-friendly graphical interface (Tkinter)

🛠 Requirements
Python 3.x

Required libraries (install via requirements.txt):

tkinter (included with Python on most systems)

pyperclip

requests

📦 Installation   

Clone this repository:

git clone https://github.com/kalifa122/SECURE-PASSWORD-CHECK-.git
cd SECURE-PASSWORD-CHECK-

Create and activate a virtual environment:

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS / Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

📄 Usage
When you start the app, you will see:

A password entry field to check your password’s strength

A "Check" button to evaluate it

A "Check Pwned" button to see if it has been compromised

A "Generate Password" button to create a new one

Criteria list showing what’s met

Generated password display with a Copy button


🧪 Example Output

Example when checking a strong password:

Strength: Strong (5/5)
Pwned: Not found

Example generated password:

hT9#jLm@Q2vP

📌 Notes

Minimum password length: 6 characters

If no character types are selected in the generator, an error is raised

Internet connection is required for the "Check Pwned" feature

📝 License
This project is licensed under the MIT License — you can use and modify it freely.

