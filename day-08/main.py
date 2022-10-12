art = """
..####....####...######...####....####...#####............####...######..#####...##..##..######..#####..
.##..##..##..##..##......##......##..##..##..##..........##..##....##....##..##..##..##..##......##..##.
.##......######..####.....####...######..#####...........##........##....#####...######..####....#####..
.##..##..##..##..##..........##..##..##..##..##..........##..##....##....##......##..##..##......##..##.
..####...##..##..######...####...##..##..##..##...........####...######..##......##..##..######..##..##.
........................................................................................................
"""


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


print(art)


def encrypt(text, shift):
    cipher_text = ""

    for char in text:

        if char.isalpha():
            char_index_shifted = alphabet.index(char) + shift

            shift_pos = (
                char_index_shifted - len(alphabet)
                if char_index_shifted > 25
                else char_index_shifted
            )

            cipher_text += alphabet[shift_pos]

        else:
            cipher_text += char

    return cipher_text


def decrypt(text, shift):
    cipher_text = ""

    for char in text:

        if char.isalpha():
            char_index_shifted = alphabet.index(char) - shift
            cipher_text += alphabet[char_index_shifted]
        else:
            cipher_text += char

    return cipher_text


while True:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    if direction == "encode":
        encrypted_text = encrypt(text, shift)
        print(f"\nEncryted result: {encrypted_text}")

    elif direction == "decode":
        dencrypted_text = decrypt(text, shift)
        print(f"\nDecryted result: {dencrypted_text}")

    print("\nDo you want to run the program again")
    run_again_user_input = input("'yes' or 'no': ").lower()

    if run_again_user_input == "no":
        break

print("Have a nice day :)")
