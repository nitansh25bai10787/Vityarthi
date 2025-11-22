import random
import string

def make_password(length, upper, lower, numbers, symbols):
    chars = ""
    if upper:
        chars = chars + string.ascii_uppercase
    if lower:
        chars = chars + string.ascii_lowercase
    if numbers:
        chars = chars + string.digits
    if symbols:
        chars = chars + "!@#$%^&*()-_=+"
    
    if chars == "":
        return ""
    
    password = ""
    for i in range(length):
        password = password + random.choice(chars)
    return password

def check_strength(password):
    strength = 0
    
    if len(password) >= 8:
        strength = strength + 1
    if len(password) >= 12:
        strength = strength + 2
    
    for char in password:
        if char.isupper():
            strength = strength + 1
            break
    for char in password:
        if char.islower():
            strength = strength + 1
            break
    for char in password:
        if char.isdigit():
            strength = strength + 1
            break
    
    if strength < 3:
        return "Weak"
    elif strength < 5:
        return "Medium"
    else:
        return "Strong"

print("\n" + "=" * 40)
print("   PASSWORD GENERATOR".center(40))
print("=" * 40 + "\n")

try:
    while True:
        pwd_length = int(input("Password length (8-50): "))
        
        if pwd_length < 8 or pwd_length > 50:
            print("Length must be between 8 and 50!\n")
            continue
        
        print("\nInclude in password:")
        use_upper = input("  Uppercase (A-Z)? (y/n): ") == "y"
        use_lower = input("  Lowercase (a-z)? (y/n): ") == "y"
        use_nums = input("  Numbers (0-9)? (y/n): ") == "y"
        use_symbols = input("  Symbols (!@#$)? (y/n): ") == "y"
        
        result = make_password(pwd_length, use_upper, use_lower, use_nums, use_symbols)
        
        if result == "":
            print("\nPlease select at least one option!\n")
            continue
        
        strength = check_strength(result)
        
        print("\n" + "-" * 40)
        print(f"Password: {result}")
        print(f"Strength: {strength}")
        print("-" * 40 + "\n")
        
        if input("Generate another? (y/n): ") != "y":
            break
    
    print("\nThank you for using Password Generator!")
    print("Stay secure!\n")

except:
    print("\nError occurred. Exiting...\n")