import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}!@#$%^&*()_"

all_chars = lower + upper + symbols + numbers
length = 8  # Length should be an integer

for i in range(2):  # Added missing colon here
    password = "".join(random.sample(all_chars, length))  # Generate a new password each time
    print(f"Generated Password {i+1}: {password}")  # Indented correctly