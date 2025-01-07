# def greet():
#     print("Hello")
#     c = (1+2) + 3*2
#     print(c)


# greet()


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How's it like in {location}")


# greet_with("Choco", "Eket")


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How's it like in {location}")


# greet_with(location="Eket", name="Choco")


# from math import ceil


# def paint(width, height, coverage):
#     return ceil((height*width)/(coverage))


# height = int(input("Height of wall: "))
# width = int(input("Width of wall: "))
# coverage = int(input("Coverage of each bucket: "))
# b_of_paints = paint(height=height, width=width, coverage=coverage)
# if b_of_paints > 1:
#     print(f"You need {b_of_paints} buckets for this job")
# else:
#     print(f"You need {b_of_paints} bucket for this job")


# def prime_checker():
#     n = int(input("Check this number: "))

#     is_prime = True
#     if n <= 1:
#         is_prime = False
#     if n == 2:
#         is_prime = True
#     # for i in range(2, n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is not a prime number")


# prime_checker()

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


# def encrypt(plain_text, shift):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     return cipher_text


# def decrypt(cipher_text, shift):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     return plain_text


# if direction == "encode":
#     print(encrypt(plain_text=text, shift=shift))

# elif direction == "decrypt":
#     print(decrypt(cipher_text=text, shift=shift))


def caesar(text, shift, direction):
    message = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % 26
            message += alphabet[new_position]
        else:
            message += letter
    return message


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    message = caesar(text=text, shift=shift, direction=direction)
    print(f"Here's the {direction}d result: {message}")

    result = input(
        "\nWould you like to restart the program? Type 'yes' or 'no': \n"
    ).lower()
    if result != "yes":
        should_continue = False
        print("Goodbye")
