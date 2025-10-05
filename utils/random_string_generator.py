import random
import string

def random_string_generator():
    # First part: 6 random letters (uppercase and lowercase)
    letters_part = ''.join(random.choices(string.ascii_letters, k=6))
    
    # Second part: 3 random digits
    digits_part = ''.join(random.choices(string.digits, k=3))
    
    # Combine and reverse
    combined = letters_part + digits_part
    reversed_combined = combined[::-1]
    
    return reversed_combined

# Example usage
print(random_string_generator())  # e.g. "652DRoeGs"
