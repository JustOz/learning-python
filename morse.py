import sys


morse_dict = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", 
            "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", '/']
abc_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


def morse_encode(text: str) -> str:
    encodedText = ""
    text = text.lower()
    for char in text:
        encodedText += morse_dict[abc_dict.index(char)] + " "
    
    return encodedText

def morse_decode(text: str) -> str:
    decodedText = ""
    text = text.split(' ')
    for i in range(len(text) - 1):
        decodedText += abc_dict[morse_dict.index(text[i])]

    return decodedText


def main() -> int:
    try:
        text = sys.argv[1]
        morse_encoded = morse_encode(text.lower())
        print("{} >> {}".format(text, morse_encoded))
    except :
       print(">> Please enter argument [a-z]")

    return 0


if __name__ == "__main__":
    main()
