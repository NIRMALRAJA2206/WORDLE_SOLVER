import random
def generate_words_list(file_path):
    words = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 5:
                words.append(line)
    return words


def generate_position_dictionary(words):
    positions = {'first': {}, 'second': {}, 'third': {}, 'fourth': {}, 'fifth': {}}

    for i in words:
        for j in range(5):
            position_name = ['first', 'second', 'third', 'fourth', 'fifth'][j]
            if i[j] not in positions[position_name]:
                positions[position_name][i[j]] = 1
            else:
                positions[position_name][i[j]] += 1

    for key in positions:
        positions[key] = dict(sorted(positions[key].items(), key=lambda item: item[1], reverse=True))

    return positions

def filter_words_by_frequencies(words, position_dict):
    sorted_positions = sorted(position_dict.items(), key=lambda item: list(item[1].values())[0], reverse=True)
    wordx = words.copy()

    word_lists = {
        'word_first': [],
        'word_second': [],
        'word_third': [],
        'word_fourth': [],
        'word_fifth': [],
    }

    for name, item in sorted_positions:
        z = 1
        flag = False
        wordname = "word_" + name
        while not flag:
            alpha = list(item.keys())[:z]
            for k in alpha:
                for ini in wordx:
                    if str(ini[['first', 'second', 'third', 'fourth', 'fifth'].index(name)]) == str(k):
                        if ini not in word_lists[wordname]:
                            word_lists[wordname].append(ini)

            if len(word_lists["word_" + name]) == 0:
                z += 1
                # print("z increase")
            else:
                flag = True
                wordx = word_lists["word_" + name].copy()
    return wordx



def display():
    global cursor_position
    for i in list_of_guesses:
        for key, value in i:
            if value == 1:
                print(f"\x1b[1;97m{key}\x1b[0m", end=' ')
            elif value == 2:
                print(f"\x1b[1;93m{key}\x1b[0m", end=' ')
            elif value == 3:
                print(f"\x1b[1;95m{key}\x1b[0m", end=' ')
        print()
        cursor_position += 1

list_of_words = generate_words_list('words_alpha.txt')

crt_word = random.choice(list_of_words)
letter_in_crt_pl = {}
letter_in_wrg_pl = {}
letter_not_ext = []

words = generate_words_list('words_alpha.txt')
# Generate the position dictionary
position_dict = generate_position_dictionary(words)

# Filter words based on frequencies
suggested_words = filter_words_by_frequencies(words, position_dict)
my_guess = suggested_words[0]

guesses =[]
list_of_guesses =[]
global cursor_position
cursor_position = 0


count = 1
if my_guess==crt_word:
    print("Cool",crt_word)
    exit()
else:
    for i, j in zip(my_guess, crt_word):
        if i == j:
            guesses.append((i, 1))
        elif i in crt_word:
            guesses.append((i, 2))
        else:
            guesses.append((i, 3))
    list_of_guesses.append(guesses)
    if len(list_of_guesses) > 1:
        print(f"\x1b[{cursor_position}A", end='')
        print("\x1b[0J", end='')
        cursor_position = 1

    while my_guess != crt_word and count<=6:
        guesses =[]
        count+=1
        # print(my_guess)
        for i in range(5):
            if my_guess[i] not in crt_word and my_guess[i] not in letter_not_ext:
                letter_not_ext.append(str(my_guess[i]))
            elif crt_word[i] == my_guess[i]:
                if crt_word[i] not in letter_in_crt_pl.keys():
                    letter_in_crt_pl[crt_word[i]] = []
                    if i not in letter_in_crt_pl[crt_word[i]]:
                        letter_in_crt_pl[crt_word[i]].append(i)
                else:
                    if i not in letter_in_crt_pl[crt_word[i]]:
                        letter_in_crt_pl[crt_word[i]].append(i)
            else:
                if my_guess[i] not in letter_in_wrg_pl.keys():
                    letter_in_wrg_pl[my_guess[i]] = []
                    if i not in letter_in_wrg_pl[my_guess[i]]:
                        letter_in_wrg_pl[my_guess[i]].append(i)
                else:
                    if i not in letter_in_wrg_pl[my_guess[i]]:
                        letter_in_wrg_pl[my_guess[i]].append(i)
        new_words_1 = []
        new_words_2 = []
        new_words_3 = []

        new_words_1 = [word for word in words if not any(letter in word for letter in letter_not_ext)]

        for c in new_words_1:
            conditions_met = True
            for d, positions in letter_in_crt_pl.items():
                for pos in positions:
                    if pos >= len(c) or d != c[pos]:
                        conditions_met = False
                        break
                if not conditions_met:
                    break
            if conditions_met:
                new_words_2.append(c)
        # print(new_words_2)

        for e in new_words_2:
            conditions_met = True
            for f, expected_positions in letter_in_wrg_pl.items():
                for expected_pos in expected_positions:
                    if (f in e and len(e) > expected_pos and e[expected_pos] == f):
                        conditions_met = False
                        break
            if conditions_met:
                new_words_3.append(e)
        #print(new_words_3)

        position_dict1 = generate_position_dictionary(new_words_3)
        suggested_words1 = filter_words_by_frequencies(new_words_3, position_dict1)
        # print(new_words_2)
        # print(new_words_3)
        # print(suggested_words1)
        my_guess = suggested_words1[0]
        # print(letter_not_ext)
        # print(letter_in_wrg_pl)
        # print(letter_in_crt_pl)

        for i, j in zip(my_guess, crt_word):
            if i == j:
                guesses.append((i, 1))
            elif i in crt_word:
                guesses.append((i, 2))
            else:
                guesses.append((i, 3))
        list_of_guesses.append(guesses)
        if len(list_of_guesses) > 1:
            print(f"\x1b[{cursor_position}A", end='')
            print("\x1b[0J", end='')
            cursor_position = 1

    display()
    # print(my_guess)

