import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Pass Crakr")
print(ascii_banner)

def crack_password(hash_to_crack, password_dictionary):
    with open(password_dictionary, 'r') as file:
        for line in file.readlines():
            password = line.strip()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password

            if hashed_password == hash_to_crack:
                print(f"Password cracked: {password}")
                return password

    print("Password not found in the dictionary.")
    return None

# Example usage:
hashed_password_to_crack = '6a1d3b7b09f1ae1d6a19cda157f6c7fcd615f4e7b4807a0cf5dcab6e0728ab2b'  # Replace with the hash to crack
dictionary_file = '/home/bella/Documents/SecLists/SecLists-master/Passwords/xato-net-10-million-passwords-100000.txt'  # Replace with the path to your password dictionary file

crack_password(hashed_password_to_crack, dictionary_file)
