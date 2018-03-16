letter = 'ThiS is String with Upper and lower case Letters'
split_letter = list(letter.lower())
letters = {}

for chu in split_letter:
    letters[chu] = 0

for i in range(len(split_letter)):
    letters[split_letter[i]]+=1

for key in sorted(letters):
    print(key,letters[key])
