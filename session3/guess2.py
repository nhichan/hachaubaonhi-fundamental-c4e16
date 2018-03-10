from random import shuffle, choice
array = ['hedonistic','epicurean','astonishing','intriguing','versatile']
word=choice(array)
split=list(word)
shuffle(split)
print(*split,sep=' ')
count=0
playing=True
while playing:
    guess=str(input('guess the word: '))
    if guess!=word:
        print('wrong')
    else:
        print('right answer!')
        playing=False
    count +=1
    if count ==4:
        print ('you lose')
        playing = False
