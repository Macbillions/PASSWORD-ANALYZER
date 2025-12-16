# 🤝 Contributing to Password Strength Checker

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [Getting Started](#-getting-started)
- [Making Changes](#-making-changes)
- [Submitting Changes](#-submitting-changes)
- [Coding Standards](#-coding-standards)
- [Testing](#-testing)
- [Documentation](#-documentation)

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful of others and their ideas.

### Expected Behavior

- Use welcoming and inclusive language
- Be respectful of differing opinions and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, discrimination, or derogatory comments
- Aggressive or abusive language
- Trolling or spam
- Unwelcome sexual attention or advances

---

## 🚀 Getting Started

### 1. Fork the Repository

```bash
# Visit https://github.com/yourusername/password-strength-checker
# Click the "Fork" button in the top-right corner
```

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/password-strength-checker.git
cd password-strength-checker
```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/yourusername/password-strength-checker.git
```

### 4. Create a Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 5. Install Dependencies

```bash
# This project only uses Python standard library
# No additional installation needed!
```

---

## 📝 Making Changes

### Create a Feature Branch

```bash
git checkout -b feature/YourFeatureName
```

Branch naming conventions:
- `feature/` for new features
- `bugfix/` for bug fixes
- `docs/` for documentation
- `test/` for tests
- `refactor/` for code refactoring

### Make Your Changes

1. Write clean, readable code
2. Follow the coding standards (see below)
3. Add/update tests as needed
4. Update documentation if necessary

### Commit Your Changes

```bash
git add .
git commit -m "Clear and descriptive commit message"
```

Commit message guidelines:
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 50 characters
- Reference issues and pull requests liberally after the first line
- Example: "Add crack time calculation\n\nFixes #123"

---

## 🔄 Submitting Changes

### 1. Push to Your Fork

```bash
git push origin feature/YourFeatureName
```

### 2. Create a Pull Request

1. Visit your fork on GitHub
2. Click "Compare & pull request"
3. Fill in the PR title and description
4. Reference any related issues
5. Submit the PR

### Pull Request Guidelines

**Title Format:**
```
[Type] Short description

Examples:
[Feature] Add password generator
[Bug] Fix entropy calculation
[Docs] Update README
[Test] Add unit tests for validation
```

**Description Template:**

```markdown
## Description
Brief description of what this PR does.

## Related Issues
Fixes #123

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
How to test these changes:
1. Step 1
2. Step 2
3. Step 3

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] All tests pass
- [ ] No new warnings generated
```

---

## 📐 Coding Standards

### Python Style Guide (PEP 8)

```python
# Good
def calculate_entropy(password: str) -> float:
    """Calculate password entropy in bits."""
    if not password:
        return 0.0
    char_space = get_character_space(password)
    return len(password) * math.log2(char_space)

# Bad
def calc_entropy(p):
    if p:
        cs = get_cs(p)
        return len(p) * math.log2(cs)
```

### Naming Conventions

```python
# Constants
MINIMUM_PASSWORD_LENGTH = 8
DEFAULT_GUESSING_RATE = 10e9

# Functions and variables
def validate_password(password: str) -> bool:
    is_valid = len(password) >= MINIMUM_PASSWORD_LENGTH
    return is_valid

# Classes
class PasswordStrengthChecker:
    """Analyzes password strength."""
    pass

# Private methods/variables
def _internal_helper() -> None:
    _private_var = "only for internal use"
```

### Documentation

```python
def calculate_strength_score(self) -> int:
    """
    Calculate password strength score (0-5).
    
    Scoring:
    - 1 point: Length >= 8
    - 1 point: Length >= 12
    - 0.5 points: Lowercase letters
    - 0.5 points: Uppercase letters
    - 0.5 points: Numbers
    - 0.5 points: Special symbols
    
    Returns:
        int: Strength score from 0 (very weak) to 5 (very strong)
    
    Example:
        >>> checker = PasswordStrengthChecker()
        >>> checker.password = "Test123!"
        >>> score = checker._calculate_strength_score()
        >>> print(score)
        4
    """
    score = 0
    # Implementation here
    return score
```

### Type Hints

```python
from typing import Dict, List, Tuple, Optional

def analyze_password(password: str) -> Dict[str, any]:
    """Analyze password and return results."""
    pass

def find_patterns(text: str, patterns: List[str]) -> Tuple[str, ...]:
    """Find matching patterns."""
    pass

def get_optional_value(key: str) -> Optional[str]:
    """Get optional value."""
    return None
```

---

## 🧪 Testing

### Writing Tests

```python
import unittest
from password_checker import PasswordStrengthChecker

class TestPasswordChecker(unittest.TestCase):
    """Test cases for PasswordStrengthChecker."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.checker = PasswordStrengthChecker()
    
    def test_length_calculation(self):
        """Test password length is correctly calculated."""
        result = self.checker.check_password("TestPass123")
        self.assertEqual(result['length'], 11)
    
    def tearDown(self):
        """Clean up after tests."""
        self.checker = None
```

### Running Tests

```bash
# Run all tests
python -m unittest test_password_checker.py

# Run with verbose output
python -m unittest test_password_checker.py -v

# Run specific test
python -m unittest test_password_checker.TestPasswordStrengthChecker.test_length_calculation

# Run with coverage
python -m pytest test_password_checker.py --cov
```

### Test Requirements

- Tests must be in `test_password_checker.py`
- All tests must pass before submitting PR
- Aim for >90% code coverage
- Test both positive and negative cases

---

## 📖 Documentation

### Updating README

Update `README_GITHUB.md` if your changes affect:
- Features
- Installation
- Usage
- Configuration

### Adding Examples

If adding a new feature:

1. Add example to `demo.py`
2. Update documentation with usage
3. Add docstring with examples

Example format:

```python
def new_feature(self, param: str) -> str:
    """
    Description of the feature.
    
    Args:
        param: Description of parameter
    
    Returns:
        Description of return value
    
    Example:
        >>> checker = PasswordStrengthChecker()
        >>> result = checker.new_feature("test")
        >>> print(result)
        'expected output'
    """
    pass
```

---

## 🎯 Contribution Ideas

### Easy (Good for first-time contributors)

- [ ] Add more test cases
- [ ] Improve code comments
- [ ] Update documentation
- [ ] Add examples to docstrings
- [ ] Create tutorials

### Medium (Intermediate)

- [ ] Add new password analysis rules
- [ ] Create visualization features
- [ ] Add configuration options
- [ ] Implement new suggestions
- [ ] Add export functionality

### Hard (Advanced)

- [ ] Build web interface
- [ ] Create password generator
- [ ] Implement breach database checking
- [ ] Add batch file analysis
- [ ] Create REST API

---

## 🔍 Review Process

### Before Submitting

- [ ] Code follows PEP 8 standards
- [ ] All tests pass locally
- [ ] No syntax errors
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No debug code left in

### During Review

Your PR will be reviewed by maintainers for:
- Code quality and standards
- Test coverage
- Documentation completeness
- Security considerations
- Performance implications

Feedback will be provided constructively. Please:
- Be open to suggestions
- Ask questions if unclear
- Make requested changes
- Respond to reviews promptly

---

## 🆘 Getting Help

- 💬 **GitHub Issues** - For bug reports and features
- 💡 **GitHub Discussions** - For questions and ideas
- 📧 **Email** - For sensitive issues
- 📚 **Documentation** - Check docs before asking

---

## 📊 Project Status

- **Status**: Active Development
- **Maintainers**: [Your Name/Team]
- **Response Time**: 48 hours

---

## 🎉 Recognition

All contributors are recognized in:
- CONTRIBUTORS.md file
- GitHub contributor list
- Project README

Thank you for contributing to Password Strength Checker! 🌟

---

<div align="center">

**Made with ❤️ by contributors like you**

[⬆ back to top](#-contributing-to-password-strength-checker)

</div>
