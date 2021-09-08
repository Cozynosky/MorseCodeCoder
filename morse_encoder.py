import sys
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
    encoded = ""
    for symbol in message:
        if symbol == " " or symbol == "\n":
            # Space between words should have length of 7 single dot, but after every symbol there is already 3 dots
            # space
            encoded += " " * 4
        else:
            encoded += symbols[symbol] + " " * 3
    return encoded


def make_audio(encoded_message: str, output_path: str = "out.mp3") -> None:
    """
    Takes encoded message as str input and makes .mp3 with Morse coded message
    :param encoded_message: Encoded message
    :type encoded_message: str
    :param output_path: path to where will exported file be
    :type output_path: str
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

    morse_code_audio.export(output_path, format="mp3")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sentence = input("Write your sentence: \n").upper()
        encoded_sentence = encode(sentence)
        print(f"Your ENCODED message:\n{encoded_sentence}")

        if export_opt := input("Would you like to export it as .mp3? [y/n]: ") == 'y':
            make_audio(encoded_message=encoded_sentence)

    if len(sys.argv) > 1:
        if sys.argv[3] == "-t":
            with open(sys.argv[1], "r") as f:
                text_input = f.read().upper()

            encoded_message = encode(text_input)

            with open(sys.argv[2], "w", encoding='utf-8') as f:
                f.write(encoded_message)

        elif sys.argv[3] == "-a":
            with open(sys.argv[1], "r") as f:
                text_input = f.read().upper()

            encoded_message = encode(text_input)
            make_audio(encoded_message, sys.argv[2])

        else:
            print("""
            USAGE:
            python morse_encoder.py [input_file_name] [output_file_name] [export_option]

            DESCRIPTION
            input_file_name      - path to .txt file with message to encode
            output_file_name     - path where output file will be exported
            export_option   :
                -t - export to a text file
                -a - export to a .mp3 file
            """)
