#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Creation of a vocabulary dataset
"""

vocabs = {'programming':['The activity or job of writing computer programs','______mming'],
    'python':['A very large snake that kills animals','____hon'],
    'fun':['Pleasure, enjoyment or entretainment','__n']}

def list_all_words():
    print('Your Vocab List\n')
    for key, value in vocabs.items():
        print('  {} ({})\n    - {}\n'.format(key, value[1], value[0]))

def new_word():
    try:
        word, definition, hint=input('Enter your new word(word|meaning|hint):\n').split('|')
        if word in vocabs:
            print('{} is already in the Vocaob builder'.format(word))
        else:
            vocabs[word]= [definition, hint]
            print('word {} added.'.format(word))
    except ValueError:
        print('Please make sure the format is correct')
    except:
        print('Unexpected Error!')

def remove_a_word():
    word = input('Enter a word to remove: ')
    if word in vocabs:
        del(vocabs[word])
        print('{} has been removed.'.format(word))
    else:
        print('Cannot find the word {} in your Vocab builder.'.format(word))

def test_yourself():
    points =0
    incorrect_word_list=[]
    want_to_quit=False

    for key, value in vocabs.items():
        while True:
            answer=input('\nWhat is {}\n or [p]ass, [h]int, [q]uit\n'.format(value[0]))
            if answer==key :
                print('Correct!!')
                points +=1
                break
            elif answer == 'p':
                print('The correct answer is {}'.format(key))
                incorrect_word_list.append(key)
            elif answer=='h':
                print(value[1])
            elif answer =='q':
                want_to_quit = True
                break
            else:
                print('It\'s not correct :(')
                incorrect_word_list.append(key)
        if want_to_quit:
            break

    print('\Score: {}/{}'.format(points, len(vocabs)))
    print('Incorrect word list:')
    for key in incorrect_word_list:
        values=vocabs[key]
        print('  {}\n'.format(key, values[0]))


def main():
    """
    Calling the functions
    """
    while True:
        cmd = input("""\nWelcome to Vocab Builder!
        1)Test yourself!
        2)Add a new word
        3)Remove a word
        4)List all words
        5)Exit\n""")

        if cmd =='1':
            test_yourself()
        elif cmd== '2':
            new_word()
        elif cmd == '3':
            remove_a_word()
        elif cmd=='4':
            list_all_words()
        elif cmd == '5':
            break



if __name__ == "__main__":
    main()

