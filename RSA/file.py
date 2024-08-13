from typing import List
from rsa import *


def store_password():
    p = askForPrime()
    q = askForPrime()
    public, private = generate_keypair(p, q)
    print(f"Public Key: {public}")
    print(f"Private Key: {private}")
    password = askForPassword()
    encrypted_password = encrypt(public, password)
    print(f"Encrypted Message: {encrypted_password}")
    encryptedListAsString = encryptedListToString(encrypted_password)
    appendToFile(encryptedListAsString)


def encryptedListToString(encrypted_msg: List[int]) -> str:
    return ' '.join(map(str, encrypted_msg))


def appendToFile(content: str) -> None:
    # Open the file in append mode
    with open('passwords.txt', 'a') as file:
        file.write(content)
        file.write("\n")


def retrieve_password():
    # Open the file in read mode
    with open('passwords.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:

            # Prompt the user for input
            user_input = input("Enter integers separated by commas: ")

            # Split the input string by commas and convert each value to an integer
            values = [int(value.strip()) for value in user_input.split(',')]

            # Create a tuple from the list of integers
            private = tuple(values)

            # Convert the string to a list of integers using a list comprehension
            numbers_list = [int(num) for num in line.split()]
            
            decrypted_msg = decrypt(private, numbers_list)

            print(decrypted_msg)


if __name__ == "__main__":

    # Example Usage: p = 61 q = 53

    #store_password()
    retrieve_password()
