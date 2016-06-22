"""
Pangrams
"""

alphabet = []

def pangram_detector(sentence):
    global alphabet
    for letter in sentence:
        if letter.isalpha():
            alphabet += letter
    unique_alphabet = set(alphabet)
    if len(unique_alphabet) == 26:
        return 'A'


def pan_detector(sentence):
    alphabett = []
    for letter in sentence:
        if 122 >= ord(letter) >= 97:
            alphabett += letter
    unique_alphabett = set(alphabett)
    if len(unique_alphabett) == 26:
        return 'Pangram'
    else:
        return 'Not a pangram'


print pangram_detector(raw_input("Please enter your sentence:").lower())
print pan_detector(raw_input("Please enter your sentence:").lower())





"""
def pangram_detector(sentence):
    pngrm = re.findall('[a-z]', sentence)

    if len(set(pngrm)) == 26:
        return True
    else:
        return False


print pangram_detector(raw_input("Please enter your sentence:").lower())
"""