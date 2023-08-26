
"""
A little bit of context, I made this program due to wanting to something to teach me the Sanskrit alphabet. I thought it would be effective doing online flashcards and the learn mode given on websites
but soon enough I found myself stuck behind a paywall. I wanted to make this program to not only teach myself but others as well who are in my situation simply for free.
"""

"""
If this works out, I will keep adding more, my goal is to be able to use this to self teach or teach others Intermediate Sanskrit reading from scratch.

Make sure to install a Devanāgarī keyboard (the writing script used for Sanskrit)
"""

import random
import sys

sanskrit_alphabet_vowels = {
    'अ' : 'a',
    'आ' : 'ā',
    'इ' : 'i',
    'ई': 'ī',
    'उ': 'u',
    'ऊ': 'ū',
    'ऋ': 'ṛ',
    'ॠ': 'ṝ',
    'ऌ': 'ḷ',
    'ॡ': 'ḹ',
    'ए': 'e',
    'ऐ': 'ai',
    'ओ': 'o',
    'औ': 'au',
    'अं' : 'aṃ',
    'अः' : 'aḥ'
}

sanskrit_alphabet_consonants = {
    'क' : 'ka',
    'ख' : 'kha',
    'ग' : 'ga',
    'घ' : 'gha',
    'ङ' : 'ṅa',
    
    'च' : 'ca',
    'छ' : 'cha',
    'ज' : 'ja',
    'झ' : 'jha',
    'ञ' : 'ña',
    
    
    'ट' : 'ṭa',
    'ठ' : 'ṭha',
    'ड' : 'ḍa',
    'ढ' : 'ḍha',
    'ण' : 'ṇa',

    'त' : 'ta',
    'थ' : 'tha',
    'द' : 'da',
    'ध' : 'dha',
    'न' : 'na',

    'प' : 'pa',
    'फ' : 'pha',
    'ब' : 'ba',
    'भ' : 'bha',
    'म' : 'ma',

    'य' : 'ya',
    'र' : 'ra',
    'ल' : 'la',
    'व' : 'va',
    'श' : 'śa',
    'ष' : 'ṣa',
    'स' : 'sa',
    'ह' : 'ha',

}


# Functions for Vowel Practice
def pick_random_letter_sound_vowel():
    return random.choice(list(sanskrit_alphabet_vowels.values()))

def find_the_letter_of_sound_vowel(x):
    for key, value in sanskrit_alphabet_vowels.items():
        if value == x:
            return key
        

# Functions for Consonant Practice
def pick_random_letter_sound_consonant():
    return random.choice(list(sanskrit_alphabet_consonants.values()))

def find_the_letter_of_sound_consonant(x):
    for key, value in sanskrit_alphabet_consonants.items():
        if value == x:
            return key
        

while True:
    prac_type = input('Would you like to practice vowels only, consonants only, or both? Enter "v" to practice vowels only, enter "c" to practice consonants only, and enter "b" to practice both\nEnter "quit" to quit the program\n\nYour Answer: ')

    if prac_type == 'quit':
        sys.exit()

    if prac_type in ['v', 'c', 'b']:
        break

    else:
        print("\nInvalid Input Please Try Again\n\n")


if prac_type == 'v':
    while True:
        letter_sound = pick_random_letter_sound_vowel()
        print(f"\n\nType in the letter that makes the sound {letter_sound} (if you want to quit then type 'quit' without the quotations)\n")
        answer = input('Your Answer: ').lower().strip()

        if answer == 'quit':
            break

        if answer == find_the_letter_of_sound_vowel(letter_sound):
            print('Correct!')

        else:
            print('Incorrect Try again\n\n')
            y = letter_sound
            while True:
                print(f"Type in the letter that makes the sound {y} (if you want to quit then type 'quit' without the quotations)")
                answer = input('Your Answer: ').lower().strip()
                if answer == 'quit':
                    sys.exit()
                if answer != find_the_letter_of_sound_vowel(y):
                    print('Incorrect Try Again\n\n')
                if answer == find_the_letter_of_sound_vowel(y):
                    print("Correct!")
                    break

elif prac_type == 'c':
    while True:
        letter_sound = pick_random_letter_sound_consonant()
        print(f"\n\nType in the letter that makes the sound {letter_sound} (if you want to quit then type 'quit' without the quotations)\n")
        answer = input('Your Answer: ').lower().strip()

        if answer == 'quit':
            break

        if answer == find_the_letter_of_sound_consonant(letter_sound):
            print('Correct!')

        else:
            print('Incorrect Try again\n\n')
            y = letter_sound
            while True:
                print(f"Type in the letter that makes the sound {y} (if you want to quit then type 'quit' without the quotations)")
                answer = input('Your Answer: ').lower().strip()
                if answer == 'quit':
                    sys.exit()
                if answer != find_the_letter_of_sound_consonant(y):
                    print('Incorrect Try Again\n\n')
                if answer == find_the_letter_of_sound_consonant(y):
                    print('Correct!')
                    break

elif prac_type == 'b':
    
    pass 




