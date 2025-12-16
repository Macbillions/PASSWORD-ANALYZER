<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=2800&pause=2000&color=6A5ACD&center=true&vCenter=true&width=600&lines=PASSWORD+ANALYZER+%F0%9F%94%90;Secure+Your+Digital+Life" alt="Typing SVG" />

<br/>

```
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗   ║
║   ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗  ║
║   ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║  ║
║   ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║  ║
║   ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝  ║
║   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝   ║
║                                                                       ║
║        █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗  ║
║       ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚══███╔╝██╔════╝██╔══██╗ ║
║       ███████║██╔██╗ ██║███████║██║   ╚████╔╝   ███╔╝ █████╗  ██████╔╝ ║
║       ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝   ███╔╝  ██╔══╝  ██╔══██╗ ║
║       ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████╗███████╗██║  ██║ ║
║       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝  ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

<h3>🚀 Analyze password strength with advanced entropy calculations and intelligent security recommendations</h3>

[![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Macbillions/PASSWORD-ANALYZER?style=for-the-badge)](https://github.com/Macbillions/PASSWORD-ANALYZER/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Macbillions/PASSWORD-ANALYZER?style=for-the-badge)](https://github.com/Macbillions/PASSWORD-ANALYZER/network)

<br/>

**✨ Your Ultimate Password Security Companion ✨**

</div>

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [Security Best Practices](#security-best-practices)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

PASSWORD ANALYZER is a sophisticated command-line tool designed to evaluate password strength using industry-standard security metrics. It provides real-time analysis, entropy calculations, and actionable recommendations to help users create stronger, more secure passwords.

## ✨ Features

- 🔒 **Multi-Factor Analysis** - Evaluates length, character variety, and pattern complexity
- 📊 **Entropy Calculation** - Mathematical measurement of password randomness
- 🎯 **Smart Suggestions** - Context-aware recommendations for improvement
- ⚡ **Real-Time Feedback** - Instant password strength assessment
- 🎨 **Beautiful CLI Interface** - Color-coded, easy-to-read output
- 🔍 **Pattern Detection** - Identifies weak patterns like repeating characters and sequences

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/Macbillions/PASSWORD-ANALYZER.git

# Navigate to the project directory
cd PASSWORD-ANALYZER

# Run the tool
python password_checker.py
```

## 💻 Usage

### Interactive Mode
```bash
python password_checker.py
```

### CLI Mode
```bash
python cli.py "YourPassword123!"
```

### Demo Script
```bash
python demo.py
```

## 🔬 How It Works

### Strength Scoring Algorithm

The tool uses a comprehensive 5-point scoring system:

| Score | Rating | Description |
|-------|--------|-------------|
| 5/5 | 🟢 Very Strong | Exceeds all security requirements |
| 4/5 | 🟢 Strong | Meets all security requirements |
| 3/5 | 🟡 Good | Meets most requirements |
| 2/5 | 🟠 Fair | Basic security only |
| 1/5 | 🔴 Weak | Multiple weaknesses |
| 0/5 | 🔴 Very Weak | Extremely vulnerable |

### Entropy Calculation

Password entropy measures unpredictability using the formula:

```
Entropy = log₂(character_space^password_length)
```

**Character Space:**
- Lowercase only: 26 characters
- + Uppercase: 52 characters
- + Numbers: 62 characters
- + Symbols: 94+ characters

**Example:**
- 8-character password (all types): ~52.4 bits
- 12-character password (all types): ~78.7 bits
- 16-character password (all types): ~105.0 bits

## 📊 Example Output

```
============================================================
🔐 PASSWORD STRENGTH ANALYSIS
============================================================

📝 Password Length: 15 characters

📊 Character Variety:
   ✓ Lowercase letters: Yes
   ✓ Uppercase letters: Yes
   ✓ Numbers: Yes
   ✓ Special symbols: Yes

🔢 Entropy Score: 99.15 bits
   (Measures randomness/security level; higher is better)

💪 Strength Level: Very Strong (5/5)

✅ Excellent! Your password is very strong.

============================================================
```

## 🛡️ Security Best Practices

### Password Recommendations

1. **Minimum Length:** 12+ characters (16+ recommended)
2. **Character Variety:** Mix uppercase, lowercase, numbers, and symbols
3. **Avoid Common Patterns:**
   - Sequential characters (abc, 123)
   - Repeated characters (aaa, 111)
   - Dictionary words
   - Personal information
4. **Uniqueness:** Use different passwords for different accounts
5. **Regular Updates:** Change passwords periodically
6. **Password Manager:** Consider using a password manager for complex passwords

### Entropy Guidelines

| Entropy (bits) | Strength Level | Recommendation |
|---------------|----------------|----------------|
| < 28 | Very Weak | ❌ Do not use |
| 28-35 | Weak | ⚠️ Improve immediately |
| 36-59 | Fair | 🟡 Can be better |
| 60-127 | Strong | ✅ Good for most uses |
| 128+ | Very Strong | ✅ Excellent for sensitive data |

## 📁 Project Structure

```
PASSWORD-ANALYZER/
├── password_checker.py    # Main password analysis class
├── cli.py                 # Command-line interface
├── demo.py                # Demo script with examples
├── utils.py               # Utility functions
├── config.py              # Configuration settings
├── test_password_checker.py  # Unit tests
├── LICENSE                # MIT License
└── README.md             # This file
```

## 🧪 Testing

Run the test suite:
```bash
python test_password_checker.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Resources

- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [OWASP Password Security](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Password Entropy Explained](https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Macbillions**
- GitHub: [@Macbillions](https://github.com/Macbillions)
- Email: annorsamuel208@gmail.com

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ for better password security**

[Report Bug](https://github.com/Macbillions/PASSWORD-ANALYZER/issues) · [Request Feature](https://github.com/Macbillions/PASSWORD-ANALYZER/issues)

</div>

