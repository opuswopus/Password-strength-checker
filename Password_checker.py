import re

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "letmein", "admin", "welcome"
}

def check_password_strength(pw: str) -> dict:
    checks = {
        "length_12_plus": len(pw) >= 12,
        "has_uppercase": bool(re.search(r"[A-Z]", pw)),
        "has_lowercase": bool(re.search(r"[a-z]", pw)),
        "has_number": bool(re.search(r"\d", pw)),
        "has_special": bool(re.search(r"[^A-Za-z0-9]", pw)),
        "not_common": pw.lower() not in COMMON_PASSWORDS,
    }

    score = sum(checks.values())

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Okay"
    else:
        rating = "Strong"

    missing = [name for name, passed in checks.items() if not passed]

    return {
        "rating": rating,
        "score": score,
        "checks": checks,
        "missing": missing
    }

def pretty_name(check_key: str) -> str:
    mapping = {
        "length_12_plus": "Use 12+ characters",
        "has_uppercase": "Add an uppercase letter (A-Z)",
        "has_lowercase": "Add a lowercase letter (a-z)",
        "has_number": "Add a number (0-9)",
        "has_special": "Add a special character (!@#$ etc.)",
        "not_common": "Avoid common passwords (password/123456/admin)",
    }
    return mapping.get(check_key, check_key)

def main():
    print("=== Password Strength Checker ===")
    pw = input("Enter a password to test: ").strip()

    result = check_password_strength(pw)

    print("\nResult:")
    print(f"Rating: {result['rating']}  |  Score: {result['score']}/6")

    if result["missing"]:
        print("\nTo improve your password:")
        for item in result["missing"]:
            print(f"- {pretty_name(item)}")
    else:
        print("\nNice — your password meets all checks.")

if __name__ == "__main__":
    main()
