import string

import itertools

def brute_force_cracker(target_password):
    chars = string.ascii_lowercase + string.digits  # Abhi sirf chote letters aur numbers try kar rahe hain
    attempts = 0
    
    # Ye loop 1 se 4 character wale sare combinations try karega
    for length in range(1, 5): 
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = "".join(guess)
            if guess == target_password:
                return f"Password cracked: {guess} in {attempts} attempts!"
    return "Password too strong for this simple cracker."

# Test karne ke liye (sirf 3-4 letters ka password dalna varna time lagega)
test_pass = input("\nEnter a small 3-4 digit password to crack: ")
print(brute_force_cracker(test_pass))

    