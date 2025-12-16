"""
Demonstration and Example Script for Password Strength Checker

This script shows how to use the PasswordStrengthChecker class
programmatically (not through the CLI).
"""

from password_checker import PasswordStrengthChecker


def demo_basic_usage():
    """Demonstrate basic usage of the password checker."""
    print("\n" + "="*70)
    print("DEMO 1: Basic Usage")
    print("="*70 + "\n")
    
    checker = PasswordStrengthChecker()
    
    # Example passwords to test
    passwords = [
        "weak",
        "password",
        "Password123",
        "MySecure@Pass2024",
        "X9@kL$2mN#vP7wQ!Rs"
    ]
    
    for pwd in passwords:
        print(f"\nTesting password: '{pwd}'")
        result = checker.check_password(pwd)
        print(f"  Strength: {result['strength_score']}/5")
        print(f"  Entropy: {result['entropy']} bits")
        print(f"  Length: {result['length']} characters")
        print()


def demo_strength_comparison():
    """Compare different passwords side-by-side."""
    print("\n" + "="*70)
    print("DEMO 2: Strength Comparison")
    print("="*70 + "\n")
    
    checker = PasswordStrengthChecker()
    
    print("Comparing 5 passwords of increasing strength:\n")
    
    passwords = [
        ("pass", "Too short, no variety"),
        ("password123", "Missing uppercase"),
        ("Password123", "Missing symbols"),
        ("Password123!", "Good overall"),
        ("X9@kL$2mN#vP7wQ!Rs", "Excellent"),
    ]
    
    print(f"{'Password':<20} {'Score':<8} {'Entropy':<10} {'Description':<25}")
    print("-" * 65)
    
    for pwd, desc in passwords:
        result = checker.check_password(pwd)
        score = result['strength_score']
        entropy = result['entropy']
        print(f"{pwd:<20} {score}/5     {entropy:<10.1f} {desc:<25}")


def demo_character_variety():
    """Show how character variety affects strength."""
    print("\n" + "="*70)
    print("DEMO 3: Character Variety Impact")
    print("="*70 + "\n")
    
    checker = PasswordStrengthChecker()
    
    print("Same length (12 chars), different variety:\n")
    
    passwords = [
        ("aaaaaaaaaaaa", "Only lowercase"),
        ("AAAAAAAAAAAA", "Only uppercase"),
        ("aaaaaa111111", "Lowercase + digits"),
        ("AaBbCc123456", "Mixed variety"),
        ("Aa1!Bb2@Cc3#", "All character types"),
    ]
    
    for pwd, desc in passwords:
        result = checker.check_password(pwd)
        print(f"Password: {pwd}")
        print(f"  Description: {desc}")
        print(f"  Strength: {result['strength_score']}/5")
        print(f"  Entropy: {result['entropy']} bits")
        print()


def demo_length_impact():
    """Show how password length affects entropy."""
    print("\n" + "="*70)
    print("DEMO 4: Length Impact on Entropy")
    print("="*70 + "\n")
    
    checker = PasswordStrengthChecker()
    
    print("Adding 'X' to 'Aa1!' progressively:\n")
    
    base = "Aa1!"
    for i in range(1, 6):
        pwd = base * i
        result = checker.check_password(pwd)
        print(f"Length {len(pwd):2d}: {'X' * len(pwd):<20} "
              f"Score: {result['strength_score']}/5  Entropy: {result['entropy']:6.1f} bits")


def demo_pattern_detection():
    """Show pattern detection for weak passwords."""
    print("\n" + "="*70)
    print("DEMO 5: Weak Pattern Detection")
    print("="*70 + "\n")
    
    checker = PasswordStrengthChecker()
    
    weak_patterns = [
        ("aaaaaa", "Repeating characters"),
        ("Abcdef123", "Sequential letters"),
        ("Pass1234", "Sequential numbers"),
        ("Qwerty123!", "Keyboard pattern"),
        ("Admin@123", "Common word"),
    ]
    
    print("Passwords with weak patterns:\n")
    
    for pwd, issue in weak_patterns:
        result = checker.check_password(pwd)
        print(f"Password: {pwd}")
        print(f"  Issue: {issue}")
        print(f"  Strength: {result['strength_score']}/5")
        if result['suggestions']:
            for suggestion in result['suggestions']:
                if '⚠️' in suggestion:
                    print(f"  Warning: {suggestion}")
        print()


def demo_entropy_calculation():
    """Demonstrate entropy calculation details."""
    print("\n" + "="*70)
    print("DEMO 6: Understanding Entropy")
    print("="*70 + "\n")
    
    import math
    
    print("Entropy Formula: log₂(character_space ^ password_length)\n")
    
    checker = PasswordStrengthChecker()
    
    examples = [
        ("aaaaaaaa", "Only lowercase (26 chars)"),
        ("AaBbCcDd", "Uppercase + lowercase (52 chars)"),
        ("Aa1!Bb2@", "All types (94 chars)"),
    ]
    
    for pwd, desc in examples:
        result = checker.check_password(pwd)
        
        # Calculate character space
        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_symbol = any(c in "!@#$%^&*()_+-=[]{}\\|;:'\",.<>?/`~" for c in pwd)
        
        char_space = 0
        char_space += 26 if has_lower else 0
        char_space += 26 if has_upper else 0
        char_space += 10 if has_digit else 0
        char_space += 32 if has_symbol else 0
        
        # Manual entropy calculation
        entropy_calc = len(pwd) * math.log2(char_space)
        
        print(f"Password: {pwd}")
        print(f"  {desc}")
        print(f"  Length: {len(pwd)}")
        print(f"  Character space: {char_space}")
        print(f"  Entropy: {entropy_calc:.2f} bits (can withstand 2^{entropy_calc:.0f} guesses)")
        print()


def demo_security_recommendations():
    """Show real-world security recommendations."""
    print("\n" + "="*70)
    print("DEMO 7: Security Recommendations")
    print("="*70 + "\n")
    
    print("Based on NIST Guidelines (SP 800-63B):\n")
    
    recommendations = {
        "Minimum Requirements": [
            "✓ At least 12 characters",
            "✓ Mix of uppercase and lowercase",
            "✓ Include at least one number",
            "✓ Include at least one special character",
        ],
        "What NOT to do": [
            "✗ Don't use common passwords (password, 123456, qwerty)",
            "✗ Don't repeat characters (aaa, 111)",
            "✗ Don't use sequential patterns (123, abc, qwerty)",
            "✗ Don't use personal information (name, birthdate)",
            "✗ Don't reuse passwords across accounts",
        ],
        "Best Practices": [
            "✓ Use passphrases (sentences are stronger and more memorable)",
            "✓ Use unique passwords for each account",
            "✓ Enable two-factor authentication (2FA)",
            "✓ Use a password manager to store passwords securely",
            "✓ Aim for 15+ characters for high-security accounts",
        ],
    }
    
    for category, items in recommendations.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  {item}")


def demo_wordlist_checking():
    """Demonstrate checking against common password lists."""
    print("\n" + "="*70)
    print("DEMO 8: Common Password Detection")
    print("="*70 + "\n")
    
    # List of commonly used passwords
    common_passwords = [
        'password', '123456', 'qwerty', 'abc123', 'letmein',
        'monkey', 'dragon', 'master', 'admin', 'sunshine'
    ]
    
    test_passwords = [
        'password123',
        'MyPassw0rd!',
        'Qwerty@2024',
        'SuperSecure#123',
    ]
    
    checker = PasswordStrengthChecker()
    
    print("Checking for common password substrings:\n")
    print(f"{'Password':<20} {'Contains Common?':<20} {'Strength':<10}")
    print("-" * 50)
    
    for pwd in test_passwords:
        result = checker.check_password(pwd)
        
        contains_common = any(common in pwd.lower() for common in common_passwords)
        common_status = "Yes ⚠️" if contains_common else "No ✓"
        strength = result['strength_score']
        
        print(f"{pwd:<20} {common_status:<20} {strength}/5")


def demo_api_usage():
    """Show how to use the checker programmatically in code."""
    print("\n" + "="*70)
    print("DEMO 9: Using the Checker in Your Code")
    print("="*70 + "\n")
    
    print("Example: Validate a user's password during registration\n")
    
    print("Code:")
    print("""
from password_checker import PasswordStrengthChecker

def register_user(username, password):
    checker = PasswordStrengthChecker()
    result = checker.check_password(password)
    
    # Enforce minimum strength requirement
    if result['strength_score'] < 3:
        return {
            'success': False,
            'message': 'Password too weak',
            'suggestions': result['suggestions']
        }
    
    # Check for common passwords
    if result['entropy'] < 50:
        return {
            'success': False,
            'message': 'Password not random enough'
        }
    
    # Password is strong - proceed with registration
    return {
        'success': True,
        'message': 'User registered successfully'
    }
    """)
    
    print("\nResult of using this in practice:\n")
    
    checker = PasswordStrengthChecker()
    
    test_cases = [
        ("simple", "Weak password"),
        ("Password123", "Moderate password"),
        ("SecurePass@2024", "Strong password"),
    ]
    
    for pwd, desc in test_cases:
        result = checker.check_password(pwd)
        would_accept = result['strength_score'] >= 3 and result['entropy'] >= 50
        status = "✓ ACCEPTED" if would_accept else "✗ REJECTED"
        print(f"Password: {pwd}")
        print(f"  ({desc})")
        print(f"  Status: {status}")
        print()


def run_all_demos():
    """Run all demonstrations."""
    print("\n" + "="*70)
    print("PASSWORD STRENGTH CHECKER - COMPREHENSIVE DEMO")
    print("="*70)
    
    demos = [
        demo_basic_usage,
        demo_strength_comparison,
        demo_character_variety,
        demo_length_impact,
        demo_pattern_detection,
        demo_entropy_calculation,
        demo_security_recommendations,
        demo_wordlist_checking,
        demo_api_usage,
    ]
    
    for demo in demos:
        demo()
    
    print("\n" + "="*70)
    print("END OF DEMONSTRATIONS")
    print("="*70 + "\n")


if __name__ == "__main__":
    # You can run individual demos or all of them
    
    # Run all demos:
    run_all_demos()
    
    # Or run specific demos:
    # demo_basic_usage()
    # demo_strength_comparison()
    # demo_entropy_calculation()
