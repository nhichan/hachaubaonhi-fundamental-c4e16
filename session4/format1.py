s=str(input('nhap vao ten: '))
words = s.split()
for i in range(len(words)):
    words[i] = words[i].capitalize()
print(' '.join(words))
