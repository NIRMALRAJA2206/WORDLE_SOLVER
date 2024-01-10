file_path = 'words_alpha.txt'
words = []

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) == 5:
            words.append(line)
print(len(words))
new_words_1=[]
new_words_2 = []
new_words_3 = []
letter_not_ext = ['n']
letter_in_wrg_pl = {'s': 4}
letter_in_crt_pl = {'s': 0, 'a': 1, 'e': 3}

for a in words:
    for b in letter_not_ext:
        if b not in a:
            new_words_1.append(a)

for c in new_words_1:
    x = 0
    for d in letter_in_crt_pl.keys():
        if d == c[letter_in_crt_pl[d]]:
            x += 1
    if x == len(letter_in_crt_pl.keys()):
        print(c)
        new_words_2.append(c)

for e in new_words_2:
    for f in letter_in_wrg_pl.keys():
        if f in e[:letter_in_wrg_pl[f]] or f in e[letter_in_wrg_pl[f] + 1:]:
            new_words_3.append(e)

print(len(new_words_1),len(new_words_2),len(new_words_3))
print(new_words_3)





