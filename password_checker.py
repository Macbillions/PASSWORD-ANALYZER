"""
Password Strength Checker - Main Module

A comprehensive tool for analyzing password strength and providing
security recommendations based on entropy, character variety, and
estimated crack time.

Author: Password Security Project
Version: 2.0
"""

import math
import re
from dataclasses import dataclass
from typing import Dict, List
from config import (
    STRENGTH_LEVELS, PATTERNS, COMMON_PASSWORDS,
    DEFAULT_GUESSING_RATE, MINIMUM_REQUIREMENTS
)
from utils import (
    format_crack_time_human,
    get_vulnerability_status,
    print_header,
    print_section,
    print_item,
)


@dataclass(frozen=True)
class CharacterProfile:
    """Represents which character classes are present in a password."""

    has_lowercase: bool
    has_uppercase: bool
    has_digits: bool
    has_symbols: bool

    @property
    def space_size(self) -> int:
        """Return the total character space implied by the present classes."""
        return (
            (26 if self.has_lowercase else 0)
            + (26 if self.has_uppercase else 0)
            + (10 if self.has_digits else 0)
            + (32 if self.has_symbols else 0)
        )


class PasswordStrengthChecker:
    """Analyzes password strength and provides improvement suggestions."""
    
    def __init__(self):
        """Initialize the password strength checker."""
        self.password: str = ""
        self.analysis: Dict = {}
    
    def check_password(self, password: str) -> Dict:
        """
        Analyze password strength and return detailed analysis.
        
        Args:
            password: The password to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        self.password = password
        profile = self._build_profile(password)

        self.analysis = {
            'length': len(password),
            'has_lowercase': profile.has_lowercase,
            'has_uppercase': profile.has_uppercase,
            'has_digits': profile.has_digits,
            'has_symbols': profile.has_symbols,
        }

        entropy = self._calculate_entropy(profile.space_size, len(password))
        strength_score = self._calculate_strength_score(profile, len(password))

        self.analysis['entropy'] = entropy
        self.analysis['strength_score'] = strength_score
        self.analysis['suggestions'] = self._generate_suggestions(profile)
        self.analysis['crack_time'] = self._calculate_crack_time(entropy)

        return self.analysis

    def _build_profile(self, password: str) -> CharacterProfile:
        """Return the presence of character classes for the password."""
        return CharacterProfile(
            has_lowercase=bool(re.search(PATTERNS['lowercase'], password)),
            has_uppercase=bool(re.search(PATTERNS['uppercase'], password)),
            has_digits=bool(re.search(PATTERNS['digits'], password)),
            has_symbols=bool(re.search(PATTERNS['symbols'], password)),
        )
    
    def _calculate_entropy(self, character_space: int, length: int) -> float:
        """
        Calculate password entropy (randomness/security level).
        
        Entropy = log2(character_space ^ password_length)
        Higher entropy = more secure password
        
        Returns:
            Entropy score in bits
        """
        if character_space == 0 or length == 0:
            return 0

        entropy = length * math.log2(character_space)
        return round(entropy, 2)
    
    def _calculate_strength_score(self, profile: CharacterProfile, length: int) -> int:
        """
        Calculate password strength score (0-5).
        
        Returns:
            Strength score from 0 (very weak) to 5 (very strong)
        """
        score = 0
        
        # Length check
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        
        # Character variety checks
        if profile.has_lowercase:
            score += 0.5
        if profile.has_uppercase:
            score += 0.5
        if profile.has_digits:
            score += 0.5
        if profile.has_symbols:
            score += 0.5
        
        return min(int(score), 5)
    
    def _generate_suggestions(self, profile: CharacterProfile) -> List[str]:
        """
        Generate improvement suggestions based on weaknesses.
        
        Returns:
            List of suggestions for password improvement
        """
        suggestions = []

        if len(self.password) < 8:
            suggestions.append("⚠️  Increase password length to at least 8 characters")
        elif len(self.password) < 12:
            suggestions.append("💡 Consider increasing length to 12+ characters for stronger security")
        
        if not profile.has_uppercase:
            suggestions.append("⚠️  Add uppercase letters (A-Z)")
        
        if not profile.has_lowercase:
            suggestions.append("⚠️  Add lowercase letters (a-z)")
        
        if not profile.has_digits:
            suggestions.append("⚠️  Add numbers (0-9)")
        
        if not profile.has_symbols:
            suggestions.append("⚠️  Add special symbols (!@#$%^&*, etc.)")
        
        # Check for common patterns
        if re.search(PATTERNS['repeating'], self.password):
            suggestions.append("⚠️  Avoid repeating characters (aaa, 111, etc.)")
        
        if re.search(PATTERNS['sequential'], self.password):
            suggestions.append("⚠️  Avoid sequential patterns (123, abc, etc.)")
        
        # Check for common passwords
        if self.password.lower() in COMMON_PASSWORDS:
            suggestions.append("⚠️  This is a commonly used password - choose something more unique")
        
        if not suggestions:
            suggestions.append("✅ Great! Your password is strong. No improvements needed.")
        
        return suggestions
    
    def _calculate_crack_time(self, entropy: float) -> Dict:
        """
        Calculate how long it would take to crack the password.
        
        Based on:
        - Entropy (randomness)
        - Guessing rate: 10 billion guesses per second (modern GPU)
        - Average: it takes 50% of total attempts to crack
        
        Returns:
            Dictionary with crack time in various units
        """
        if entropy == 0:
            return {
                'seconds': 0,
                'minutes': 0,
                'hours': 0,
                'days': 0,
                'years': 0,
                'formatted': 'Instantly',
                'description': 'Password is empty'
            }
        
        # Total possible combinations = 2^entropy
        # Use logarithms to avoid overflow with large numbers
        try:
            if entropy > 100:
                # For very large entropy, use logarithmic calculation
                # log10(2^entropy) = entropy * log10(2)
                # Average guesses = 2^entropy / 2 = 2^(entropy-1)
                log_avg_guesses = (entropy - 1) * 0.30103
                # seconds = guesses / rate
                seconds_to_crack = (10 ** log_avg_guesses) / DEFAULT_GUESSING_RATE
            else:
                total_combinations = 2 ** entropy
                # Average time to crack (50% of total combinations)
                average_guesses_needed = total_combinations / 2
                # Time in seconds
                seconds_to_crack = average_guesses_needed / DEFAULT_GUESSING_RATE
        except (OverflowError, ValueError):
            # For extremely large values, approximate
            seconds_to_crack = float('inf')
        
        # Convert to different time units
        minutes = seconds_to_crack / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365.25
        
        # Format human-readable time
        formatted = format_crack_time_human(seconds_to_crack)
        
        # Get vulnerability description
        color, description = get_vulnerability_status(seconds_to_crack)
        
        return {
            'seconds': round(seconds_to_crack, 2),
            'minutes': round(minutes, 2),
            'hours': round(hours, 2),
            'days': round(days, 2),
            'years': round(years, 2),
            'formatted': formatted,
            'description': description
        }
    
    def display_results(self):
        """Display formatted password analysis results."""
        if not self.analysis:
            print("❌ No password analyzed yet. Use check_password() first.")
            return

        analysis = self.analysis
        
        print_header("PASSWORD STRENGTH ANALYSIS")
        
        # Password Length
        print_item("📝 Password Length", f"{analysis['length']} characters")
        
        # Character Variety
        print_section("📊 Character Variety")
        print_item("Lowercase letters", "✓ Yes" if analysis['has_lowercase'] else "✗ No", "  ")
        print_item("Uppercase letters", "✓ Yes" if analysis['has_uppercase'] else "✗ No", "  ")
        print_item("Numbers", "✓ Yes" if analysis['has_digits'] else "✗ No", "  ")
        print_item("Special symbols", "✓ Yes" if analysis['has_symbols'] else "✗ No", "  ")
        
        # Entropy
        print()
        print_item("🔢 Entropy Score", f"{analysis['entropy']} bits")
        print("   (Measures randomness/security level; higher is better)")
        
        # Strength Level
        strength_level = STRENGTH_LEVELS[analysis['strength_score']]
        print()
        print_item("💪 Strength Level", f"{strength_level} ({analysis['strength_score']}/5)")
        
        # Crack Time
        crack_time = analysis['crack_time']
        print_section("⏱️  Time to Crack")
        print(f"   {crack_time['description']}")
        print_item("Estimated time", crack_time['formatted'], "  ")
        print("   (Assumes 10 billion guesses/second with modern GPU)")
        
        # Suggestions
        print_section("💡 Suggestions")
        for suggestion in analysis['suggestions']:
            print(f"   {suggestion}")
        
        print("\n" + "="*60 + "\n")
    
    def get_security_rating(self) -> str:
        """
        Get a detailed security rating.
        
        Returns:
            Detailed security assessment
        """
        if not self.analysis:
            return "No password analyzed"
        
        score = self.analysis['strength_score']
        entropy = self.analysis['entropy']
        crack_years = self.analysis['crack_time']['years']
        
        if score >= 4 and entropy >= 80 and crack_years >= 1e6:
            return "🟢🟢 Excellent - Highly Secure"
        elif score >= 3 and entropy >= 50 and crack_years >= 100:
            return "🟢 Good - Secure"
        elif score >= 2 and entropy >= 40:
            return "🟡 Fair - Could Be Better"
        elif score >= 1:
            return "🟠 Weak - Needs Improvement"
        else:
            return "🔴 Very Weak - Immediately Upgrade"


def main():
    """Main function to run the password strength checker."""
    checker = PasswordStrengthChecker()
    _print_banner()
    _print_intro()

    while True:
        password = input("\nEnter a password to analyze (or 'quit' to exit): ")

        if password.lower() == 'quit':
            print("\nThank you for using Password Strength Checker! 👋\n")
            break

        if not password:
            print("❌ Password cannot be empty. Please try again.\n")
            continue

        checker.check_password(password)
        checker.display_results()
        print(f"Security Rating: {checker.get_security_rating()}\n")

def _print_banner() -> None:
    """Render the ASCII art banner in green."""
    green = "\033[92m"
    reset = "\033[0m"
    banner = r"""
88888888ba      db         ad88888ba    ad88888ba             88  888b      88  88888888888  ,ad8888ba,    
88      "8b    d88b       d8"     "8b  d8"     "8b            88  8888b     88  88          d8"'    '8b   
88      ,8P   d8''8b      Y8,          Y8,                    88  88 '8b    88  88         d8'        '8b  
88aaaaaa8P'  d8'  '8b     'Y8aaaaa,    'Y8aaaaa,              88  88  '8b   88  88aaaaa    88          88  
88''''''    d8YaaaaY8b      '''''8b,    '''''8b,  aaaaaaaa  88  88   '8b  88  88'''''    88          88  
88         d8"  "  "8b           '8b          '8b  "  "  "  88  88    '8b 88  88         Y8,        ,8P  
88        d8'        '8b  Y8a     a8P  Y8a     a8P            88  88     '8888  88          Y8a.    .a8P   
88       d8'          '8b  "Y88888P"    "Y88888P"             88  88      '888  88           'Y8888Y'    
"""
    print("\n" + green + banner + reset)


def _print_intro() -> None:
    """Print the one-line tool intro."""
    print("This tool analyzes your password strength and provides")
    print("suggestions for improvement.\n")
    print("=" * 60)


if __name__ == "__main__":
    main()
