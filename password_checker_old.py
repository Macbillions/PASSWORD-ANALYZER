import re
import math
from typing import Dict, List, Tuple
from datetime import timedelta


class PasswordStrengthChecker:
    """Analyzes password strength and provides improvement suggestions."""
    
    # Strength levels
    STRENGTH_LEVELS = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    
    def __init__(self):
        """Initialize the password strength checker."""
        self.password = ""
        self.analysis = {}
    
    def check_password(self, password: str) -> Dict:
        """
        Analyze password strength and return detailed analysis.
        
        Args:
            password: The password to analyze
            
        Returns:
            Dictionary containing analysis results
        """
        self.password = password
        self.analysis = {
            'length': len(password),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_digits': bool(re.search(r'\d', password)),
            'has_symbols': bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>?/`~]', password)),
        }
        self.analysis['entropy'] = self._calculate_entropy()
        self.analysis['strength_score'] = self._calculate_strength_score()
        self.analysis['suggestions'] = self._generate_suggestions()
        self.analysis['crack_time'] = self._calculate_crack_time()
        return self.analysis
    
    def _calculate_entropy(self) -> float:
        """
        Calculate password entropy (randomness/security level).
        
        Entropy = log2(character_space ^ password_length)
        Higher entropy = more secure password
        """
        char_space = 0
        
        if re.search(r'[a-z]', self.password):
            char_space += 26
        if re.search(r'[A-Z]', self.password):
            char_space += 26
        if re.search(r'\d', self.password):
            char_space += 10
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>?/`~]', self.password):
            char_space += 32
        
        if char_space == 0:
            return 0
        
        entropy = len(self.password) * math.log2(char_space)
        return round(entropy, 2)
    
    def _calculate_strength_score(self) -> int:
        """
        Calculate password strength score (0-5).
        
        Returns:
            Strength score from 0 (very weak) to 5 (very strong)
        """
        score = 0
        
        # Length check
        if len(self.password) >= 8:
            score += 1
        if len(self.password) >= 12:
            score += 1
        
        # Character variety checks
        if self.analysis['has_lowercase']:
            score += 0.5
        if self.analysis['has_uppercase']:
            score += 0.5
        if self.analysis['has_digits']:
            score += 0.5
        if self.analysis['has_symbols']:
            score += 0.5
        
        return min(int(score), 5)
    
    def _generate_suggestions(self) -> List[str]:
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
        
        if not self.analysis['has_uppercase']:
            suggestions.append("⚠️  Add uppercase letters (A-Z)")
        
        if not self.analysis['has_lowercase']:
            suggestions.append("⚠️  Add lowercase letters (a-z)")
        
        if not self.analysis['has_digits']:
            suggestions.append("⚠️  Add numbers (0-9)")
        
        if not self.analysis['has_symbols']:
            suggestions.append("⚠️  Add special symbols (!@#$%^&*, etc.)")
        
        # Check for common patterns
        if re.search(r'(.)\1{2,}', self.password):
            suggestions.append("⚠️  Avoid repeating characters (aaa, 111, etc.)")
        
        if re.search(r'(123|234|345|456|567|678|789|890|abc|bcd|cde)', self.password):
            suggestions.append("⚠️  Avoid sequential patterns (123, abc, etc.)")
        
        if not suggestions:
            suggestions.append("✅ Great! Your password is strong. No improvements needed.")
        
        return suggestions
    
    def _calculate_crack_time(self) -> Dict:
        """
        Calculate how long it would take to crack the password.
        
        Based on:
        - Entropy (randomness)
        - Guessing rate: assumes 10 billion guesses per second (modern GPU cracking)
        - Average: it takes 50% of total attempts to crack
        
        Returns:
            Dictionary with crack time in various units
        """
        if self.analysis['entropy'] == 0:
            return {
                'seconds': 0,
                'minutes': 0,
                'hours': 0,
                'days': 0,
                'years': 0,
                'formatted': 'Instantly',
                'description': 'Password is empty'
            }
        
        # 10 billion guesses per second (modern GPU cracking speed)
        guesses_per_second = 10e9
        
        # Total possible combinations = 2^entropy
        total_combinations = 2 ** self.analysis['entropy']
        
        # Average time to crack (50% of total combinations)
        average_guesses_needed = total_combinations / 2
        
        # Time in seconds
        seconds_to_crack = average_guesses_needed / guesses_per_second
        
        # Convert to different time units
        minutes = seconds_to_crack / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365.25
        
        # Format human-readable time
        if seconds_to_crack < 1:
            formatted = f"< 1 second"
        elif seconds_to_crack < 60:
            formatted = f"{seconds_to_crack:.1f} seconds"
        elif minutes < 60:
            formatted = f"{minutes:.1f} minutes"
        elif hours < 24:
            formatted = f"{hours:.1f} hours"
        elif days < 365:
            formatted = f"{days:.1f} days"
        elif years < 1000:
            formatted = f"{years:.1f} years"
        elif years < 1e6:
            millions = years / 1e6
            formatted = f"{millions:.1f} million years"
        elif years < 1e9:
            billions = years / 1e9
            formatted = f"{billions:.1f} billion years"
        else:
            trillions = years / 1e12
            formatted = f"{trillions:.1f} trillion years"
        
        # Description based on crack time
        if seconds_to_crack < 1:
            description = "🔴 Extremely vulnerable - instant crack"
        elif seconds_to_crack < 60:
            description = "🔴 Very vulnerable - cracks in seconds"
        elif minutes < 60:
            description = "🟠 Vulnerable - cracks in minutes"
        elif hours < 24:
            description = "🟠 Weak - cracks in hours"
        elif days < 30:
            description = "🟡 Fair - cracks in days/weeks"
        elif days < 365:
            description = "🟢 Good - would take months to crack"
        elif years < 100:
            description = "🟢 Strong - would take decades to crack"
        else:
            description = "🟢🟢 Very Strong - practically uncrackable"
        
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
        
        print("\n" + "="*60)
        print("🔐 PASSWORD STRENGTH ANALYSIS")
        print("="*60)
        
        print(f"\n📝 Password Length: {self.analysis['length']} characters")
        
        print("\n📊 Character Variety:")
        print(f"   ✓ Lowercase letters: {'Yes' if self.analysis['has_lowercase'] else 'No'}")
        print(f"   ✓ Uppercase letters: {'Yes' if self.analysis['has_uppercase'] else 'No'}")
        print(f"   ✓ Numbers: {'Yes' if self.analysis['has_digits'] else 'No'}")
        print(f"   ✓ Special symbols: {'Yes' if self.analysis['has_symbols'] else 'No'}")
        
        print(f"\n🔢 Entropy Score: {self.analysis['entropy']} bits")
        print("   (Measures randomness/security level; higher is better)")
        
        strength_level = self.STRENGTH_LEVELS[self.analysis['strength_score']]
        print(f"\n💪 Strength Level: {strength_level} ({self.analysis['strength_score']}/5)")
        
        # Display crack time information
        crack_time = self.analysis['crack_time']
        print(f"\n⏱️  Time to Crack:")
        print(f"   {crack_time['description']}")
        print(f"   Estimated time: {crack_time['formatted']}")
        print(f"   (Assumes 10 billion guesses/second with modern GPU)")
        
        print("\n💡 Suggestions:")
        for suggestion in self.analysis['suggestions']:
            print(f"   {suggestion}")
        
        print("\n" + "="*60 + "\n")


def main():
    """Main function to run the password strength checker."""
    checker = PasswordStrengthChecker()
    
    print("\n" + "="*60)
    print("🔐 PASSWORD STRENGTH CHECKER")
    print("="*60)
    print("\nThis tool analyzes your password strength and provides")
    print("suggestions for improvement.\n")
    
    while True:
        password = input("Enter a password to analyze (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("\nThank you for using Password Strength Checker! 👋\n")
            break
        
        if len(password) == 0:
            print("❌ Password cannot be empty. Please try again.\n")
            continue
        
        checker.check_password(password)
        checker.display_results()


if __name__ == "__main__":
    main()
