📌 Password Strength Checker
A simple Python script to evaluate the strength of a password based on its length, character composition, and complexity.

🚀 Features
🔹 Checks if the password is at least 8 characters long
🔹 Ensures the password includes both uppercase and lowercase letters
🔹 Verifies the presence of at least one special character (!@#$%^&)
🔹 Confirms the password contains at least one number
🔹 Provides feedback on password strength

📂 Project Structure
bash
Copy
Edit
📦 Password-Strength-Checker
 ├── 📜 password_checker.py  # Main Python script
 ├── 📜 README.md            # Documentation
🛠️ Installation
Ensure you have Python 3 installed on your system.

Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/Password-Strength-Checker.git
Navigate to the directory
bash
Copy
Edit
cd Password-Strength-Checker
Run the script
bash
Copy
Edit
python password_checker.py
📌 How It Works
1️⃣ User Input: The script prompts the user to enter a password.
2️⃣ Validation Checks: The script analyzes the password based on:

Length ✅
Uppercase & lowercase letters ✅
Special characters (!@#$%^&) ✅
Numbers ✅
3️⃣ Scoring System:
4/4 Points → ✅ Strong Password
3/4 Points → ⚠️ Needs Improvement
Less than 3 Points → ❌ Weak Password
4️⃣ Feedback: The script prints recommendations if the password is weak.
📜 Code Breakdown
python
Copy
Edit
if len(password) >= 8:
    user_score +=1
else:
    print("Password must be at least 8 characters long")
✔️ Ensures the password has a minimum length of 8 characters.

python
Copy
Edit
if re.search (r"[A-Z]", password) and re.search (r"[a-z]", password):
    user_score +=1
else:
    print("Password must contain at least one uppercase and one lowercase letter")
✔️ Checks for both uppercase and lowercase letters.

python
Copy
Edit
if re.search(r"[!@#$%^&]", password):
    user_score +=1
else:
    print("Password must contain at least one special character (!@#$%^&)")
✔️ Ensures the password includes at least one special character.

python
Copy
Edit
if re.search(r"\d", password):
    user_score +=1
else:
    print("Password must contain at least one number")
✔️ Ensures the password contains at least one digit.

📝 Example Usage
✅ Input:

graphql
Copy
Edit
Enter Your Password: Secure@123
✅ Output:

pgsql
Copy
Edit
Your Password is strong ✔️👏🙌
📌 Future Improvements
🔹 Allow users to generate strong passwords automatically
🔹 Support for customizable password rules
🔹 GUI version for better user experience

👨‍💻 Contributing
Want to improve this project? Feel free to submit a pull request or open an issue!
