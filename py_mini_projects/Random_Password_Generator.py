import random
import string

# Function to generate password
def generate_password(length, strength):
    weak_chars = string.ascii_lowercase
    medium_chars = string.ascii_letters
    strong_chars = string.ascii_letters + string.digits + string.punctuation

    if strength == 'weak':
        characters = weak_chars
    elif strength == 'medium':
        characters = medium_chars
    else:
        characters = strong_chars

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to check the strength of the password
def validate_password(password):
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    symbol_criteria = any(char in string.punctuation for char in password)

    if all([length_criteria, digit_criteria, upper_criteria, lower_criteria, symbol_criteria]):
        return "Strong"
    elif length_criteria and digit_criteria and (upper_criteria or lower_criteria):
        return "Medium"
    else:
        return "Weak"

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))
    strength = input("Choose strength (weak, medium, strong): ").lower()

    password = generate_password(length, strength)
    print(f"\nGenerated Password: {password}")

    strength_check = validate_password(password)
    print(f"Password Strength: {strength_check}")

if __name__ == "__main__":
    main()
