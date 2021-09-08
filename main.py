from pydub import AudioSegment
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
        if symbol == " " or symbol == "\n":
            # Space between words should have length of 7 single dot, but after every symbol there is already 3 dots
            # space
            encoded_message += " " * 4
        else:
            encoded_message += symbols[symbol] + " " * 3
    return encoded_message


def make_audio(encoded_message: str) -> None:
    """
    Takes encoded message as str input and makes .mp3 with Morse coded message
    :param encoded_message: Encoded message
    :type encoded_message: str
    """
    di_s = AudioSegment.from_file("sounds/di_sound.wav", format="wav")
    dah_s = AudioSegment.from_file("sounds/dah_sound.wav", format="wav")
    morse_code_audio = AudioSegment.silent(duration=0)

    pause_time = len(di_s)

    for symbol in encoded_message:
        if symbol == '•':
            morse_code_audio += di_s
        elif symbol == '—':
            morse_code_audio += dah_s
        elif symbol == ' ':
            morse_code_audio += AudioSegment.silent(pause_time)
        else:
            continue

    morse_code_audio.export("output.mp3", format="mp3")


while continue_encoding := input("Would you like to encode some words? [y/n]: ") == 'y':
    sentence = input("Write your sentence: \n").upper()
    encoded_sentence = encode(sentence)
    print(f"Your ENCODED message:\n{encoded_sentence}")

    if export_opt := input("Would you like to export it as .mp3? [y/n]: ") == 'y':
        make_audio(encoded_message=encoded_sentence)