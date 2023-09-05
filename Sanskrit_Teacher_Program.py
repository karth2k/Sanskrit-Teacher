
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
import os
import openai
from local_profile import LocalProfile
from fuzzywuzzy import fuzz
import tkinter as tk

api_key = '' # Paste your api key here

openai.api_key = api_key

sanskrit_alphabet_vowels = { # Dictionary of all Vowels
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

sanskrit_alphabet_consonants = { # Dictionary of all Consonants
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
    'क्ष' : 'kṣa',
    'ज्ञ' : 'jña',
    'त्र' : 'tra'
}

sanskrit_alphabet_full = { # Dictionary of the Entire Sanskrit Alphabet
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
    'अः' : 'aḥ',

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
    'क्ष' : 'kṣa',
    'ज्ञ' : 'jña',
    'त्र' : 'tra'

}






def get_username(): # Function takes a username to create a profile
    return input('\nCreate a profile (See readme on deleting profiles).\nEnter your username for your profile: ').strip()

def display_scores(): # Displays all the scores by iterating through each element in the JSON file and printing it out
    all_profiles = localprofile.get_all_profiles()
    print("\n\nAll User Scores:\n")
    for username, profile_data in all_profiles.items():
        if username not in ['View_All', 'Profile_Deletion']:
            score = profile_data.get("score", {})
            correct = score.get("correct", 0)
            wrong = score.get("wrong", 0)
            print(f"Username: {username}, Correct: {correct}, Wrong: {wrong}\n")
            print()

localprofile = LocalProfile('profiles.json') # Initializes the LocalProfile class from the local_profile file

print('Welcome to the Sanskrit Teacher program developed by Karthik Muthukumar, to start please create a profile.\nTo view the total progress board of all profiles simply type, "View_All" without the quotations (keep the capitalization and underscore)\n')

while True:
    username = get_username() # The next 5 lines create and check if the profile currently exists
    profile_exists = localprofile.get_score(username)['correct'] > 0 or localprofile.get_score(username)['wrong'] > 0 
    if not profile_exists:
        localprofile.create_profile(username)

    if username == 'Profile_Deletion': # If the user wants to delete their profile, they are prompted with steps on if they would like to delete just 1 or all profile (they can select which one)
        prof_delete = input('\nWould you like to delete one profile or all profiles? Enter "1" for one profile to be deleted and "a" for all profiles to be deleted: ')
        while prof_delete not in ['1', 'a']:
            print('\nInvalid Input Please Try Again')
            prof_delete = input('\nWould you like to delete one profile or all profiles? Enter "1" for one profile to be deleted and "a" for all profiles to be deleted: ')

        if prof_delete == 'a':
            localprofile.delete_profiles()
            print('\nAll Profiles Deleted Successfully.')
            sys.exit() 
            
        elif prof_delete == '1':
            select_delete = input('\nEnter the profile you would like to delete: ')
            localprofile.delete_one_profile(select_delete)
            print('\nProfile has been deleted.')
            sys.exit() 

    if username == 'View_All': # Displays all progress for writing and reading if the user enters the input "View_All"
        progress_check = input('\nWould you like to see the progress for reading or writing, enter "w" for writing and enter "r" for reading: ')
        while progress_check not in ['w', 'r']:
            print('\nInvalid Input Please Try Again')
            progress_check = input('\nWould you like to see the progress for reading or writing, enter "w" for writing and enter "r" for reading: ')

        if progress_check == 'r':
            pass #work here later

        elif progress_check == 'w':
            display_scores()
            sys.exit()
            

    

    write_or_read = input('\nWould you like to practice writing or reading Sanskrit? Enter "r" for reading "w" for writing. Type "quit" to quit (make sure to enter all values without the quotations).\n\nYour Answer: ')

    if write_or_read not in ['r', 'w', 'quit']: # If the input isn't one of the three allowed inputs, then the user must try again until it is a valid input
        print("\nInvalid Input Please Try Again\n")


    elif write_or_read == 'quit': # If the user wants to quit, this closes the proram
        print("\nExiting program...\n")
        sys.exit()




    elif write_or_read == 'r': # If the user wants to practice their reading

        easy_or_hard = input('\nWould you like to practice on easy mode or hard mode? (Type "h" for hard, "e" for easy, and "quit" for quit).\n\nYour Answer: ')
        if easy_or_hard not in ['h', 'e', 'quit']:
            print("\nInvalid Input Please Try Again\n")

        elif easy_or_hard == "quit":
            print("\nExiting program...\n")
            sys.exit()

        elif easy_or_hard == "e":
            pass

        elif easy_or_hard == "h":
            pass





    elif write_or_read == 'w': #If the user wants to practice their writing

        # Functions for Vowel Practice
        def pick_random_letter_sound_vowel(): # Picks a random letter sound
            return random.choice(list(sanskrit_alphabet_vowels.values()))

        def find_the_letter_of_sound_vowel(x): # Compares the sounds letter equivalent with the inputted value
            for key, value in sanskrit_alphabet_vowels.items():
                if value == x:
                    return key
                

        # Functions for Consonant Practice
        def pick_random_letter_sound_consonant(): # Picks a random letter sound
            return random.choice(list(sanskrit_alphabet_consonants.values())) 

        def find_the_letter_of_sound_consonant(x): # Compares the sounds letter equivalent with the inputted value
            for key, value in sanskrit_alphabet_consonants.items():
                if value == x:
                    return key
                
        # Functions for Full Alphabet Practice
        def pick_random_letter_sound(): # Picks a random letter sound
            return random.choice(list(sanskrit_alphabet_full.values())) 

        def find_the_letter_of_sound(x): # Compares the sounds letter equivalent with the inputted value
            for key, value in sanskrit_alphabet_full.items():
                if value == x:
                    return key
                

        while True: # Asks the user if they want to practice vowels, consonants, or writing the full alphabet
            prac_type = input('\n\nWould you like to practice vowels only, consonants only, or both? Enter "v" to practice vowels only, enter "c" to practice consonants only, and enter "b" to practice both\nEnter "quit" to quit the program\n\nYour Answer: ')

            if prac_type == 'quit':
                current_score = localprofile.get_score(username)
                print(f'\nHere is your writing progress:\nCorrect answers: {current_score["correct"]}, Wrong answers: {current_score["wrong"]}')
                print("\nExiting program...\n")
                sys.exit()

            if prac_type in ['v', 'c', 'b']:
                break

            else:
                print("\nInvalid Input Please Try Again\n\n")


        if prac_type == 'v': # Helps the user practice vowels
            while True:
                letter_sound = pick_random_letter_sound_vowel() 
                print(f"\n\nType in the letter that makes the sound {letter_sound} (if you want to quit then type 'quit' without the quotations)\n")
                answer = input('Your Answer: ').lower().strip()

                if answer == 'quit': # Quits the program and gives the user their progress
                    current_score = localprofile.get_score(username)
                    print(f'\nHere is your writing progress:\nCorrect answers: {current_score["correct"]}, Wrong answers: {current_score["wrong"]}')
                    print("\nExiting program...\n")
                    sys.exit()

                if answer == find_the_letter_of_sound_vowel(letter_sound):
                    print('Correct!')
                    localprofile.update_score(username, is_correct=True)


                else: #If the answer is incorrect, it keeps asking the user the same question until the right answer is given
                    print('Incorrect Try again\n\n')
                    localprofile.update_score(username, is_correct=False)
                    y = letter_sound
                    while True:
                        print(f"Type in the letter that makes the sound {y} (if you want to quit then type 'quit' without the quotations)")
                        answer = input('Your Answer: ').lower().strip()
                        if answer == 'quit':
                            current_score = localprofile.get_score(username)
                            print(f'\nHere is your writing progress:\nCorrect answers: {current_score["correct"]}, Wrong answers: {current_score["wrong"]}')
                            print("\nExiting program...\n")
                            sys.exit()
                        if answer != find_the_letter_of_sound_vowel(y):
                            print('Incorrect Try Again\n\n')
                            localprofile.update_score(username, is_correct=False)
                        if answer == find_the_letter_of_sound_vowel(y):
                            print("Correct!")
                            localprofile.update_score(username, is_correct=True)
                            break

        elif prac_type == 'c': # Helps the user practice consonants 
            while True:
                letter_sound = pick_random_letter_sound_consonant()
                print(f"\n\nType in the letter that makes the sound {letter_sound} (if you want to quit then type 'quit' without the quotations)\n")
                answer = input('Your Answer: ').lower().strip()

                if answer == 'quit': # Quits the program and gives the user their progress
                    current_score = localprofile.get_score(username)
                    print(f'\nHere is your writing progress:\nCorrect answers: {current_score["correct"]}, Wrong answers: {current_score["wrong"]}')
                    print("\nExiting program...\n")
                    sys.exit()

                if answer == find_the_letter_of_sound_consonant(letter_sound):
                    print('Correct!')
                    localprofile.update_score(username, is_correct=True)

                else:
                    print('Incorrect Try again\n\n')
                    localprofile.update_score(username, is_correct=False)
                    y = letter_sound
                    while True:
                        print(f"Type in the letter that makes the sound {y} (if you want to quit then type 'quit' without the quotations)")
                        answer = input('Your Answer: ').lower().strip()
                        if answer == 'quit':
                            current_score = localprofile.get_score(username)
                            print(f'\nHere is your writing progress:\nCorrect answers: {current_score["correct"]}, Wrong answers: {current_score["wrong"]}')
                            print("\nExiting program...\n")
                            sys.exit()

                        if answer != find_the_letter_of_sound_consonant(y):
                            print('Incorrect Try Again\n\n')
                            localprofile.update_score(username, is_correct=False)

                        if answer == find_the_letter_of_sound_consonant(y):
                            print('Correct!')
                            localprofile.update_score(username, is_correct=True)
                            break

        elif prac_type == 'b': # Helps the user practice the full alphabet
            while True:
                letter_sound = pick_random_letter_sound()
                print(f"\n\nType in the letter that makes the sound {letter_sound} (if you want to quit then type 'quit' without the quotations)\n")
                answer = input('Your Answer: ').lower().strip()

                if answer == 'quit':
                    current_score = localprofile.get_score(username)
                    print(f'\nHere is your writing progress:\nCorrect answers: {current_score["correct"]}, Wrong answers: {current_score["wrong"]}')
                    print("\nExiting program...\n")
                    sys.exit()

                if answer == find_the_letter_of_sound(letter_sound):
                    print('Correct!')
                    localprofile.update_score(username, is_correct=True)

                else:
                    print('Incorrect Try again\n\n')
                    localprofile.update_score(username, is_correct=False)
                    y = letter_sound
                    while True:
                        print(f"Type in the letter that makes the sound {y} (if you want to quit then type 'quit' without the quotations)")
                        answer = input('Your Answer: ').lower().strip()
                        if answer == 'quit':
                            current_score = localprofile.get_score(username)
                            print(f'\nHere is your writing progress:\nCorrect answers: {current_score["correct"]}, Wrong answers: {current_score["wrong"]}')
                            print("\nExiting program...\n")
                            sys.exit()

                        if answer != find_the_letter_of_sound(y):
                            print('Incorrect Try Again\n\n')
                            localprofile.update_score(username, is_correct=False)

                        if answer == find_the_letter_of_sound(y):
                            print('Correct!')
                            localprofile.update_score(username, is_correct=True)
                            break
        else:
            print("\nInvalid Input Please Try Again\n\n")