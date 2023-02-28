import random
import string


def generate_password(min_length, numbers = True , speciel_charecters= True):
    letters = string.ascii_letters
    digits = string.digits
    speciel = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if speciel_charecters:
        characters += speciel

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in speciel:
            has_special = True


        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if speciel_charecters:
            meets_criteria = meets_criteria and has_special

        return pwd




pwd = generate_password(100)
print (pwd)