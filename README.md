A Simple Python login system that features password hashing & account lockout.

About This Project:
This Project was created as a learning experience. Built step-by-step to learn about password hashing, file I/O, and basic authentication concepts in Python.

This project includes:
- User registration
- Secure Password hashing using SHA-256
- Account lockout after 3 failed login attempts

Software used:
- Python 3
- hashlib (SHA-256 password hashing)
- os library (handling files)

Tutorials/Resources used 
- Python hashlib doc: https://docs.python.org/3/library/hashlib.html) - for SHA-256 hashing
- Real Python: https://realpython.com/) - Python tutorials 
- GeeksforGeeks: https://www.geeksforgeeks.org/) - Programming tutorials & examples
- Various YouTube tutorials on creating a login system project for python


How to run:
```bash
python login.py

example: 
SIMPLE LOGIN SYSTEM
	1.	Register
	2.	Login
	3.	Exit
Enter choice (1-3): 1
=== REGISTRATION ===
Enter username: avarae
Enter password: 123
Registration successful!
========================================
SIMPLE LOGIN SYSTEM
	1.	Register
	2.	Login
	3.	Exit
Enter choice (1-3): 2
=== LOGIN ===
Enter username: avarae
Enter password: 123
Login successful! Welcome, ava!
========================================
SIMPLE LOGIN SYSTEM
	1.	Register
	2.	Login
	3.	Exit
Enter choice (1-3): 2
=== LOGIN ===
Enter username: avarae
Enter password: wrongpassword
Incorrect password. 2 attempt(s) remaining.
Enter password: wrongagain
Incorrect password. 1 attempt(s) remaining.
Enter password: stillwrong
Account locked due to too many failed attempts!
