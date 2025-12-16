<div align="center">

# 🔐 PASSWORD ANALYZER

```
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
     █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗ 
    ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗
    ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝
    ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗
    ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
```

### 🚀 A powerful CLI tool that analyzes password strength with entropy calculation and intelligent suggestions

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

---

## ✨ Features

✨ **Core Features:**
- 📥 **CLI Input**: Enter passwords interactively via command-line
- 📊 **Length Analysis**: Checks password length and provides recommendations
- 🔤 **Character Variety**: Detects uppercase, lowercase, numbers, and special symbols
- 🔢 **Entropy Calculation**: Measures password randomness/security level
- 💡 **Smart Suggestions**: Provides specific improvement recommendations
- ⚠️ **Pattern Detection**: Identifies weak patterns like repeating characters and sequences

## How It Works

The tool analyzes passwords across multiple dimensions:

### 1. **Length Analysis**
- Checks if password meets minimum length requirements
- Recommends increasing length for stronger security

### 2. **Character Variety**
- Detects presence of lowercase letters (a-z)
- Detects presence of uppercase letters (A-Z)
- Detects presence of numbers (0-9)
- Detects presence of special symbols (!@#$%^&*, etc.)

### 3. **Entropy Calculation**
```
Entropy = log₂(character_space ^ password_length)
```
- Measures the randomness and unpredictability of the password
- Higher entropy = more secure password
- Calculated based on character space and length

### 4. **Strength Scoring**
- 0/5: Very Weak
- 1/5: Weak
- 2/5: Fair
- 3/5: Good
- 4/5: Strong
- 5/5: Very Strong

### 5. **Pattern Detection**
- Detects repeating characters (aaa, 111)
- Detects sequential patterns (123, abc)
- Provides warnings for these weak patterns

## 🚀 Quick Start

### Prerequisites
- Python 3.7+

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Macbillions/PASSWORD-ANALYZER.git
cd PASSWORD-ANALYZER
```

2. Run the tool:
```bash
python password_checker.py
```

Or use the CLI version:
```bash
python cli.py "YourPassword123!"
```

### 🎯 Demo

```
============================================================
🔐 PASSWORD STRENGTH ANALYSIS
============================================================

📝 Password Length: 12 characters

📊 Character Variety:
   ✓ Lowercase letters: Yes
   ✓ Uppercase letters: Yes
   ✓ Numbers: Yes
   ✓ Special symbols: No

🔢 Entropy Score: 39.86 bits
   (Measures randomness/security level; higher is better)

💪 Strength Level: Good (3/5)

💡 Suggestions:
   💡 Add special symbols (!@#$%^&*, etc.)

============================================================
```

## Learning Outcomes

This project teaches you several important programming concepts:

### 1. **Regular Expressions (Regex)**
- Pattern matching for character detection
- Learning to use `re.search()` for flexible pattern matching
- Understanding character classes and escape sequences
- Example patterns:
  - `[a-z]` - lowercase letters
  - `[A-Z]` - uppercase letters
  - `\d` - digits
  - `[!@#$%^&*()...]` - special characters

### 2. **String Manipulation**
- Length calculations
- Character-by-character analysis
- String formatting and output
- Working with escape sequences

### 3. **Object-Oriented Programming**
- Class design and structure
- Encapsulation of related functionality
- State management with instance variables
- Method organization and single responsibility

### 4. **Mathematical Concepts**
- Entropy calculation using logarithms
- Understanding security mathematics
- Applying algorithmic thinking

### 5. **Security Best Practices**
- Password strength requirements
- Character variety importance
- Pattern weaknesses to avoid
- Why entropy matters in security
- The role of length in password security

### 6. **Code Organization**
- Separating concerns (analysis, scoring, suggestions)
- Using type hints for clarity
- Writing clear docstrings
- Implementing helper methods

## Security Best Practices

1. **Length Matters**: Aim for at least 12 characters
2. **Variety is Key**: Use mix of uppercase, lowercase, numbers, symbols
3. **Avoid Patterns**: Don't use sequential numbers or letters
4. **No Repetition**: Avoid repeating characters
5. **Entropy Matters**: Higher entropy = harder to crack
6. **Unique Passwords**: Use different passwords for different accounts

## Technical Details

### Entropy Calculation
The entropy formula measures how many bits of randomness a password has:
- Each character type (lowercase, uppercase, numbers, symbols) adds to the character space
- Larger character space = higher entropy
- Longer passwords = higher entropy
- Example: A 12-character password using all character types has ~79 bits of entropy

### Strength Score Calculation
Points awarded for:
- 1 point: Length ≥ 8
- 1 point: Length ≥ 12
- 0.5 points: Lowercase letters
- 0.5 points: Uppercase letters
- 0.5 points: Numbers
- 0.5 points: Special symbols
- Maximum score: 5

## Example Passwords

**Very Weak (0/5):**
```
password
12345678
```

**Weak (1/5):**
```
Password
password123
```

**Fair (2/5):**
```
Password123
MyPass2024
```

**Good (3/5):**
```
MyPass2024!
Secure@Pwd9
```

**Strong (4/5):**
```
MySecure@Pass2024
K7$mPx#9nL2wQ!
```

**Very Strong (5/5):**
```
X9@kL$2mN#vP7wQ!Rs
Tr0pic@lThunder$2024!
```

## Code Structure

```
password_checker.py
├── PasswordStrengthChecker (class)
│   ├── check_password() - Main analysis method
│   ├── _calculate_entropy() - Calculates security level
│   ├── _calculate_strength_score() - Determines strength (0-5)
│   ├── _generate_suggestions() - Creates improvement tips
│   └── display_results() - Formats and displays output
└── main() - CLI interface
```

## Extending the Tool

You can enhance this tool by adding:

1. **Password Generation**: Generate random strong passwords
2. **Common Password List**: Check against known weak passwords
3. **Breach Database**: Check if password appears in known breaches
4. **Keyboard Pattern Detection**: Detect QWERTY sequences
5. **File Input**: Analyze multiple passwords from a file
6. **Batch Testing**: Check multiple passwords at once
7. **Configuration**: Allow users to set custom rules
8. **Export Results**: Save analysis results to file

## 📚 Resources

- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [Python regex documentation](https://docs.python.org/3/library/re.html)
- [Password Security Best Practices](https://www.owasp.org/index.php/Authentication_Cheat_Sheet)
- [Entropy in Cryptography](https://en.wikipedia.org/wiki/Entropy_(information_theory))

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

### 🌟 Star this repository if you found it helpful!

**Made with ❤️ by [Macbillions](https://github.com/Macbillions)**

*Learn password security • Build better tools • Stay secure* 🔐

</div>
#   P A S S W O R D - A N A L Y Z E R 
 

 
