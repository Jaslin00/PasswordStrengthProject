from zxcvbn import zxcvbn

def check_strength(password):
    result = zxcvbn(password)
    print(f"\nPassword: {password}")
    print(f"Score (0–4): {result['score']}")  # 0 = very weak, 4 = very strong
    print("Feedback:", result['feedback']['suggestions'])

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    check_strength(pwd)
# This script checks the strength of a password using the zxcvbn library.
# It provides a score from 0 to 4 and gives feedback on how to improve the