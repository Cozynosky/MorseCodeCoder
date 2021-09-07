from morse_alphabet import symbols


def encode(message: str) -> str:
    """
    This function takes sentence as string parameter, encode it with Morse Code, and returns encoded message
    :param message: sentence to encode
    :type message: str
    :return: encoded message
    :rtype: str
    """
    encoded_message = ""
    for symbol in message:
        if symbol == " ":
            # Space between words should have length of 7 single dot, but after every symbol there is already 3 dots
            # space
            encoded_message += " " * 4
        # this elif is only for better formated sentence
        elif symbol == '\n':
            encoded_message += "\n"
        else:
            encoded_message += symbols[symbol] + " " * 3
    return encoded_message


while continue_encoding := input("Would you like to encode some words? [y/n]: ") == 'y':
    sentence = input("Write your sentence: \n").upper()
    encoded_sentence = encode(sentence)
    print(f"Your ENCODED message:\n{encoded_sentence}")
