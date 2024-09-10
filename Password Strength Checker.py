import re

def is_strong_password(password):
    """
    Check if the given password is strong.
    Requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (e.g., @, #, $, %)
    """
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):  # Check for uppercase letter
        return False
    
    if not re.search(r'[a-z]', password):  # Check for lowercase letter
        return False
    
    if not re.search(r'[0-9]', password):  # Check for digit
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # Check for special character
        return False
    
    return True

# Example usage
password = "Password123!"
print("Is the password strong?", is_strong_password(password))