# BruteForce-Password-Cracker-Python
# 🔐 BruteForce Password Cracker (Python)

> "Hello INDIAN CYBER CLUB ARMY. I AM PASSWORD BABA CODED BY THE CYBER BABA."

This project is a simulation of a brute-force password attack built using Python. It attempts to guess a given password by trying all possible combinations of printable characters up to a specified maximum length.

---

## 🚀 Features

- Attempts all combinations using brute force.
- Uses `itertools.product` and `string.printable` to generate candidates.
- Tracks time taken to crack the password.
- Pure Python implementation with no external dependencies.
- Educational purpose only – for cybersecurity awareness.

---

## 🛠️ Technologies Used

- Python 3
- Standard Libraries: `itertools`, `string`, `time`

---

## 📄 How It Works

1. The user inputs a password.
2. The script begins generating all combinations from length 1 up to 10.
3. Each combination is compared against the user’s password.
4. Once a match is found, the script outputs the matched password and time taken.


## 🧪 Example Output
Trying password: a
Trying password: b
...
HEY ICC ARMY YOUR I Password found: abc123
Time taken: 5.23 seconds

