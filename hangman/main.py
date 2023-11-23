import random
from setings import *


def words(string):
    lis = list(string.split(' '))
    return lis


# print(words(str_words))

def the_game():
    
    cheat = False
    num_of_found_letters = 0
    num_of_mistakes = 0
    bottom_of_letters = []
    random_word = random.choice(words(str_words))
    num_of_letters = len(random_word)
    difficulty = input('''difficulty: easy/medium/hard
''')
    if difficulty == 'easy':
        pics = [no_mistake, one_mistake, two_mistakes, three_mistakes, 
        four_mistakes, five_mistakes, six_mistakes, seven_mistake, eight_mistakes, nine_mistakes]

    if difficulty == 'medium':
        pics = [no_mistake, two_mistakes, four_mistakes, six_mistakes]

    if difficulty == 'hard':
        pics = [no_mistake, one_mistake, two_mistakes, three_mistakes, 
                                    four_mistakes, five_mistakes]

    for x in range(num_of_letters):
        bottom_of_letters.insert(0, "___ ")    

    while 1:
        if num_of_mistakes == len(pics) - 1:
            print(''.join(bottom_of_letters))
            print(pics[num_of_mistakes])
            print('you lost!!!')
            print('the word was %s' % random_word)
            break
        elif num_of_found_letters == num_of_letters:
            if cheat:
                print('the word was %s' % random_word)

            print(''.join(bottom_of_letters))
            print(pics[num_of_mistakes])
            print('you win!!!')
            break
            
        num_of_repeated_letters = 0
        incorect = True
        # print(random_word)
        print(to_split)
        print(''.join(bottom_of_letters))
        print(pics[num_of_mistakes])
        guess = input('your guess:')
        for x in range(0, num_of_letters):
            if guess == 'cheat':
                num_of_found_letters = num_of_letters
                cheat = True
            elif guess == random_word[x]:
                num_of_found_letters += 1
                bottom_of_letters[x] = ('%s ') % guess
                if num_of_repeated_letters == 0:
                    print('corect')
                    num_of_repeated_letters += 1
                incorect = False
                
        if incorect and not cheat:
            print('incorect')
            num_of_mistakes += 1

    event = input('do you want to play again ?  yes/no  :')
    if event == 'yes':
        the_game()
    else:
        return

the_game()