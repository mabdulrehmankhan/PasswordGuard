import random
import string


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    # Define criteria for password strength
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    is_length_valid = len(password) >= 8

    # Calculate the strength score
    strength_score = sum([has_upper, has_lower, has_digit, has_special, is_length_valid])

    if strength_score >= 4:
        return "Strong"
    elif strength_score >= 3:
        return "Moderate"
    else:
        return "Weak"


def main():
    print("Welcome to the Password Generator and Strength Checker!")

    while True:
        choice = input("Enter '1' to generate a random password, '2' to input your own password, or '3' to exit: ")

        if choice == '1':
            password = generate_random_password()
            print(f"Generated Password: {password}")
            strength = check_password_strength(password)
            print(f"Password Strength: {strength}")
        elif choice == '2':
            user_password = input("Enter your own password: ")
            strength = check_password_strength(user_password)
            print(f"Password Strength: {strength}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")


if __name__ == "__main__":
    main()
