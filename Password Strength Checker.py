import re
def check_password_strength(password):
    length_ok = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    if all([length_ok, has_upper, has_lower, has_digit, has_special]):
        return "Strong password"
    elif length_ok and ((has_upper and has_lower) or (has_digit and has_special)):
        return "Medium strength password"
    else:
        return "Weak password. Try adding more variety."
user_password = input("Enter your password: ")
print(check_password_strength(user_password))
