import sys
import argparse
from password_checker import PasswordStrengthChecker


def main():
    parser = argparse.ArgumentParser(
        description="Password Strength Checker CLI"
    )
    parser.add_argument(
        "password",
        nargs="?",
        help="Password to check. If omitted, reads from stdin.")
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Output only the score (0-5)."
    )
    parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="Output full result as JSON."
    )

    args = parser.parse_args()

    if args.password:
        pwd = args.password
    else:
        # Read from stdin to support piping
        pwd = sys.stdin.read().strip()
        if not pwd:
            print("No password provided. Pass an argument or pipe stdin.")
            sys.exit(2)

    checker = PasswordStrengthChecker()
    result = checker.check_password(pwd)

    if args.json:
        import json
        print(json.dumps(result, ensure_ascii=False))
        return

    if args.quiet:
        print(result.get("strength_score", 0))
        return

    # Pretty output
    print("Password Strength Report")
    print("------------------------")
    print(f"Password: {'*' * len(pwd)} ({len(pwd)} chars)")
    print(f"Strength: {result.get('strength_score', 0)}/5")
    entropy = result.get("entropy")
    if entropy is not None:
        print(f"Entropy: {entropy:.2f} bits")

    suggestions = result.get("suggestions") or []
    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"- {s}")


if __name__ == "__main__":
    main()
