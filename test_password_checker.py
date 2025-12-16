import unittest
from password_checker import PasswordStrengthChecker


class TestPasswordStrengthChecker(unittest.TestCase):
    """Unit tests for the PasswordStrengthChecker class."""
    
    def setUp(self):
        """Initialize a fresh checker instance for each test."""
        self.checker = PasswordStrengthChecker()
    
    # Length tests
    def test_length_analysis(self):
        """Test password length calculation."""
        result = self.checker.check_password("Test1234")
        self.assertEqual(result['length'], 8)
    
    def test_short_password(self):
        """Test detection of short passwords."""
        result = self.checker.check_password("Test")
        self.assertEqual(result['length'], 4)
    
    # Character variety tests
    def test_lowercase_detection(self):
        """Test detection of lowercase letters."""
        result = self.checker.check_password("password")
        self.assertTrue(result['has_lowercase'])
    
    def test_uppercase_detection(self):
        """Test detection of uppercase letters."""
        result = self.checker.check_password("PASSWORD")
        self.assertTrue(result['has_uppercase'])
    
    def test_digit_detection(self):
        """Test detection of numbers."""
        result = self.checker.check_password("12345678")
        self.assertTrue(result['has_digits'])
    
    def test_symbol_detection(self):
        """Test detection of special symbols."""
        result = self.checker.check_password("Pass!@#$")
        self.assertTrue(result['has_symbols'])
    
    def test_no_lowercase(self):
        """Test when password lacks lowercase letters."""
        result = self.checker.check_password("PASSWORD123!")
        self.assertFalse(result['has_lowercase'])
    
    def test_no_uppercase(self):
        """Test when password lacks uppercase letters."""
        result = self.checker.check_password("password123!")
        self.assertFalse(result['has_uppercase'])
    
    def test_no_digits(self):
        """Test when password lacks numbers."""
        result = self.checker.check_password("Password!")
        self.assertFalse(result['has_digits'])
    
    def test_no_symbols(self):
        """Test when password lacks special symbols."""
        result = self.checker.check_password("Password123")
        self.assertFalse(result['has_symbols'])
    
    # Entropy tests
    def test_entropy_calculation(self):
        """Test that entropy is calculated and positive."""
        result = self.checker.check_password("TestPass123!")
        self.assertGreater(result['entropy'], 0)
    
    def test_entropy_increases_with_length(self):
        """Test that longer passwords have higher entropy."""
        result1 = self.checker.check_password("Test123!")
        result2 = self.checker.check_password("Test123!Test123!")
        self.assertGreater(result2['entropy'], result1['entropy'])
    
    def test_entropy_increases_with_variety(self):
        """Test that more character types increase entropy."""
        result1 = self.checker.check_password("aaaabbbb")
        result2 = self.checker.check_password("AaBb12!@")
        self.assertGreater(result2['entropy'], result1['entropy'])
    
    # Strength score tests
    def test_strength_score_range(self):
        """Test that strength score is between 0 and 5."""
        for password in ["a", "password", "Pass123", "Pass123!", "X9@kL$2mN#vP7wQ!Rs"]:
            result = self.checker.check_password(password)
            self.assertGreaterEqual(result['strength_score'], 0)
            self.assertLessEqual(result['strength_score'], 5)
    
    def test_very_weak_password(self):
        """Test detection of very weak passwords."""
        result = self.checker.check_password("pass")
        self.assertEqual(result['strength_score'], 0)
    
    def test_weak_password(self):
        """Test detection of weak passwords."""
        result = self.checker.check_password("password123")
        self.assertLessEqual(result['strength_score'], 2)
    
    def test_strong_password(self):
        """Test detection of strong passwords."""
        result = self.checker.check_password("MySecure@Pass2024")
        self.assertGreaterEqual(result['strength_score'], 3)
    
    # Suggestion tests
    def test_suggestions_provided(self):
        """Test that suggestions are always provided."""
        result = self.checker.check_password("test")
        self.assertIsInstance(result['suggestions'], list)
        self.assertGreater(len(result['suggestions']), 0)
    
    def test_length_suggestion(self):
        """Test that length suggestions are provided for short passwords."""
        result = self.checker.check_password("abc")
        suggestions_text = ' '.join(result['suggestions']).lower()
        self.assertIn('length', suggestions_text)
    
    def test_uppercase_suggestion(self):
        """Test that uppercase suggestion is provided when missing."""
        result = self.checker.check_password("password123!")
        suggestions_text = ' '.join(result['suggestions']).lower()
        self.assertIn('uppercase', suggestions_text)
    
    def test_symbol_suggestion(self):
        """Test that symbol suggestion is provided when missing."""
        result = self.checker.check_password("Password123")
        suggestions_text = ' '.join(result['suggestions']).lower()
        self.assertIn('symbol', suggestions_text)
    
    def test_repeating_character_warning(self):
        """Test detection of repeating characters."""
        result = self.checker.check_password("Passsword123!")
        suggestions_text = ' '.join(result['suggestions']).lower()
        self.assertIn('repeat', suggestions_text)
    
    def test_sequential_pattern_warning(self):
        """Test detection of sequential patterns."""
        result = self.checker.check_password("Pass123abc!")
        suggestions_text = ' '.join(result['suggestions']).lower()
        self.assertIn('sequential', suggestions_text)
    
    def test_strong_password_feedback(self):
        """Test that strong passwords get positive feedback."""
        result = self.checker.check_password("X9@kL$2mN#vP7wQ!Rs")
        suggestions_text = ' '.join(result['suggestions']).lower()
        self.assertIn('great', suggestions_text)
    
    # Edge cases
    def test_empty_password_handling(self):
        """Test handling of edge cases."""
        result = self.checker.check_password("")
        self.assertEqual(result['length'], 0)
        self.assertFalse(result['has_lowercase'])
    
    def test_single_character(self):
        """Test single character password."""
        result = self.checker.check_password("a")
        self.assertEqual(result['length'], 1)
        self.assertTrue(result['has_lowercase'])
    
    def test_very_long_password(self):
        """Test very long password."""
        long_pass = "A" * 100
        result = self.checker.check_password(long_pass)
        self.assertEqual(result['length'], 100)
    
    def test_unicode_characters(self):
        """Test password with unicode characters."""
        result = self.checker.check_password("Пароль123!")
        self.assertGreater(result['length'], 0)
    
    # Integration tests
    def test_complete_analysis(self):
        """Test that complete analysis runs without errors."""
        result = self.checker.check_password("MySecure@Pass2024")
        self.assertIn('length', result)
        self.assertIn('has_lowercase', result)
        self.assertIn('has_uppercase', result)
        self.assertIn('has_digits', result)
        self.assertIn('has_symbols', result)
        self.assertIn('entropy', result)
        self.assertIn('strength_score', result)
        self.assertIn('suggestions', result)
    
    def test_multiple_passwords_analysis(self):
        """Test analyzing multiple passwords sequentially."""
        passwords = ["weak", "Better1", "Strong@Pass123", "X9@kL$2mN#vP7wQ!"]
        scores = []
        for pwd in passwords:
            result = self.checker.check_password(pwd)
            scores.append(result['strength_score'])
        
        # Verify scores generally increase with better passwords
        self.assertGreater(scores[1], scores[0])
        self.assertGreater(scores[2], scores[1])
    
    # Crack time tests
    def test_crack_time_calculation(self):
        """Test that crack time is calculated."""
        result = self.checker.check_password("TestPass123!")
        self.assertIn('crack_time', result)
        self.assertIn('formatted', result['crack_time'])
        self.assertIn('description', result['crack_time'])
    
    def test_weak_password_crack_time(self):
        """Test that weak passwords have short crack times."""
        result = self.checker.check_password("pass")
        crack_seconds = result['crack_time']['seconds']
        self.assertLess(crack_seconds, 1000)  # Should be quick to crack
    
    def test_strong_password_crack_time(self):
        """Test that strong passwords have long crack times."""
        result = self.checker.check_password("X9@kL$2mN#vP7wQ!Rs")
        crack_years = result['crack_time']['years']
        self.assertGreater(crack_years, 1e15)  # Should take many years to crack
    
    def test_crack_time_increases_with_entropy(self):
        """Test that crack time increases with entropy."""
        result1 = self.checker.check_password("weak")
        result2 = self.checker.check_password("VeryStr0ng@Pass!")
        
        time1 = result1['crack_time']['seconds']
        time2 = result2['crack_time']['seconds']
        
        self.assertGreater(time2, time1)
    
    def test_crack_time_description(self):
        """Test that crack time has appropriate description."""
        result = self.checker.check_password("password123")
        description = result['crack_time']['description']
        self.assertIsInstance(description, str)
        self.assertGreater(len(description), 0)


class TestLearningExamples(unittest.TestCase):
    """Examples demonstrating learning outcomes."""
    
    def setUp(self):
        """Initialize checker."""
        self.checker = PasswordStrengthChecker()
    
    # Regex learning examples
    def test_regex_lowercase_pattern(self):
        """Learning: Regex pattern for lowercase letters."""
        import re
        password = "HelloWorld"
        has_lowercase = bool(re.search(r'[a-z]', password))
        self.assertTrue(has_lowercase)
    
    def test_regex_uppercase_pattern(self):
        """Learning: Regex pattern for uppercase letters."""
        import re
        password = "helloworld"
        has_uppercase = bool(re.search(r'[A-Z]', password))
        self.assertFalse(has_uppercase)
    
    def test_regex_digit_pattern(self):
        """Learning: Regex pattern for digits using \\d."""
        import re
        password = "Password123"
        has_digits = bool(re.search(r'\d', password))
        self.assertTrue(has_digits)
    
    # String manipulation learning examples
    def test_string_length_calculation(self):
        """Learning: String length in Python."""
        password = "TestPassword"
        length = len(password)
        self.assertEqual(length, 12)
    
    def test_entropy_mathematical_formula(self):
        """Learning: Mathematical calculation for entropy."""
        import math
        password = "Abc123!"
        char_space = 26 + 26 + 10 + 32  # lowercase, uppercase, digits, symbols
        entropy = len(password) * math.log2(char_space)
        self.assertGreater(entropy, 0)
    
    # Security learning examples
    def test_character_variety_importance(self):
        """Learning: Why character variety matters."""
        result1 = self.checker.check_password("aaaabbbbcccc")
        result2 = self.checker.check_password("AaBbCcDd1!@#")
        # Same length, but result2 should have higher entropy and strength due to variety
        self.assertGreater(result2['entropy'], result1['entropy'])
        self.assertGreater(result2['strength_score'], result1['strength_score'])


if __name__ == '__main__':
    unittest.main()
