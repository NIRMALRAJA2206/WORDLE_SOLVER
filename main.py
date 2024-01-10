import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections

file_path = 'words_alpha.txt'
words = []

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) == 5:
            words.append(line)
print(len(words))
positions = {'first': {}, 'second': {}, 'third': {}, 'fourth': {}, 'fifth': {}}

for i in words:
    # first
    if i[0] not in positions['first']:
        positions['first'][i[0]] = 1
    else:
        positions['first'][i[0]] += 1

    # second
    if i[1] not in positions['second']:
        positions['second'][i[1]] = 1
    else:
        positions['second'][i[1]] += 1

    # Third
    if i[2] not in positions['third']:
        positions['third'][i[2]] = 1
    else:
        positions['third'][i[2]] += 1

    # fourth
    if i[3] not in positions['fourth']:
        positions['fourth'][i[3]] = 1
    else:
        positions['fourth'][i[3]] += 1

    # fifth
    if i[4] not in positions['fifth']:
        positions['fifth'][i[4]] = 1
    else:
        positions['fifth'][i[4]] += 1

for key in positions:
    positions[key] = dict(sorted(positions[key].items(), key=lambda item: item[1], reverse=True))

print(positions)

names = ['first', 'second', 'third', 'fourth', 'fifth']

sorted_positions = sorted(positions.items(), key=lambda item: list(item[1].values())[0], reverse=True)

wordx = words
word_lists = {
    'word_first': [],
    'word_second': [],
    'word_third': [],
    'word_fourth': [],
    'word_fifth': [],
}
for name, item in sorted_positions:
    wordname = "word_"+name
    alpha = list(item.keys())[:1]
    print(alpha)
    freq = list(item.values())[0]
    for k in alpha:
        # print(ini,end=" ")
        for ini in wordx:
            if str(ini[names.index(name)]) == str(k):
                if ini not in word_lists[wordname]:
                    # print(ini,end="*")
                    word_lists[wordname].append(ini)
    print(len(word_lists[wordname]),wordname)
    wordx = word_lists[wordname].copy()
print(wordx)