alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text, shift):
#     cipher_text = ""
#     # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     for letter in text:
#
#         position = alphabet.index(letter)
#         newPosition = position + shift
#         newletter = alphabet[newPosition]
#         cipher_text += newletter
#     print(f"the encrypted message is : {cipher_text}")
#
# # e.g.
# # plain_text = "hello"
# # shift = 5
# # cipher_text = "mjqqt"
# # print output: "The encoded text is mjqqt"
#
# ##HINT: How do you get the index of an item in a list:
# # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
# #decryption
#
# def decrypt(text, shift):
#   orignal_text = ""
#   for letter in text:
#       position = alphabet.index(letter)
#       new_position = position - shift
#       orignal_text += alphabet[new_position]
#   print(f"the decoded text is {orignal_text}")
#
#
#
# ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Invalid input")


# single function for the ceser ciphre :)

def cypher(text, shift, direction):
    orignal_text = ""

    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
        elif direction == "decode":
            new_position = position - shift
        orignal_text += alphabet[new_position]
    print(f"the {direction}d message is {orignal_text}")

from cipher_art import logo
print(logo)

cypher(text,shift,direction)