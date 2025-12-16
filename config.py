"""
Configuration settings for Password Strength Checker
"""

# Guessing rates (in guesses per second)
GUESSING_RATES = {
    'slow': 1e6,      # 1 million guesses/sec (old hardware)
    'medium': 1e9,    # 1 billion guesses/sec (modern CPU)
    'fast': 10e9,     # 10 billion guesses/sec (modern GPU) - DEFAULT
}

# Default guessing rate
DEFAULT_GUESSING_RATE = GUESSING_RATES['fast']

# Strength level names
STRENGTH_LEVELS = {
    0: "Very Weak",
    1: "Weak",
    2: "Fair",
    3: "Good",
    4: "Strong",
    5: "Very Strong"
}

# Crack time thresholds for color coding
CRACK_TIME_THRESHOLDS = {
    'instant': 1,           # < 1 second
    'seconds': 60,          # < 1 minute
    'minutes': 3600,        # < 1 hour
    'hours': 86400,         # < 1 day
    'days': 2592000,        # < 30 days
    'months': 31536000,     # < 1 year
    'years': 3153600000,    # < 100 years
}

# Emoji indicators
EMOJIS = {
    'lock': '🔐',
    'analysis': '📊',
    'length': '📝',
    'variety': '📊',
    'entropy': '🔢',
    'strength': '💪',
    'crack_time': '⏱️',
    'suggestions': '💡',
    'check': '✓',
    'warning': '⚠️',
    'success': '✅',
    'error': '❌',
}

# Color indicators for vulnerability
VULNERABILITY_COLORS = {
    'instant': '🔴',
    'seconds': '🔴',
    'minutes': '🟠',
    'hours': '🟠',
    'days': '🟡',
    'months': '🟢',
    'years': '🟢',
    'uncrackable': '🟢🟢',
}

# Common weak passwords to check
COMMON_PASSWORDS = [
    'password', '123456', 'qwerty', 'abc123', 'letmein',
    'monkey', 'dragon', 'master', 'admin', 'sunshine',
    '111111', '123123', '1234567', '12345678', 'welcome',
]

# Regex patterns
PATTERNS = {
    'lowercase': r'[a-z]',
    'uppercase': r'[A-Z]',
    'digits': r'\d',
    'symbols': r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>?/`~]',
    'repeating': r'(.)\1{2,}',
    'sequential': r'(123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',
}

# Minimum recommendations
MINIMUM_REQUIREMENTS = {
    'length': 12,
    'entropy': 50,
    'strength_score': 3,
}
