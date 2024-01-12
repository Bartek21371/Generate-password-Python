# Password generator to file

import random
import string 

print("Input number of passwords to generate: ")
num_passwords = int(input())
print("Input length of passwords: ")
length = int(input())
print("Should the passwords contain uppercase letters?")
letters = str(input()).lower()
print("Should the passwords contain special characters?")
special_char = str(input()).lower()
print("Should the passwords contain numbers?")
nums = str(input()).lower()

letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
letters_with_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "!@#$%^&*()-_+=<>?/"


def create_password(length,letters,special_char,nums):
    characters = ""
    
    if letters == "yes":
        characters += letters_with_uppercase
    elif letters == "no":
        characters += letters_lowercase
    
    if special_char == "yes":
        characters += special
    
    if nums == "yes":
        characters += numbers
        
    password = "".join(random.choice(characters) for i in range(length))
    return password

generated_passwords = []

for i in range(num_passwords):
    generated_password = create_password(length, letters, special_char, nums)
    generated_passwords.append(generated_password)


file_name = "C:\\Users\\barto\\Documents\\Generator passwords\\Generated Password.txt"
with open(file_name, "x") as file:
    for password in generated_passwords:
        file.write("Generated password: "+ password+ "\n")
print(f"Your passwords has been saved in {file_name}")