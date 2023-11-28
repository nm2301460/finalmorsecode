# Making a class for the errors
class MorseError(Exception):
    pass

# A dictinary to link between each letter and its morse
MORSECODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}
# Making a function to turn from text to morse
def text_to_morse(text):
    text = text.upper()  # converting the text into upper case
    result = []
    for char in text:
        if char in MORSECODE:
            result.append(MORSECODE[char])  # Append Morse code for the character
        elif char == " ":
            result.append("/")  # Append space for space in the input
        else:
            raise MorseError(f"The '{char}' key doesn't exist in the dictionary")  # Raise an error if the character is not in the dictionary
    return ' '.join(result)  # Join Morse code representations with spaces between characters
