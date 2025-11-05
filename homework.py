import random
import string

def generate_password(length=12):
    # Combine all characters (uppercase, lowercase, digits)
    characters = string.ascii_letters + string.digits
    
    # Randomly choose characters
    password = [random.choice(characters) for _ in range(length)]
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

# Example usage
print("Generated Password:", generate_password(12))
