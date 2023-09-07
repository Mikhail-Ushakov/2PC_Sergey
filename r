from collections import Counter
with open('text.txt', 'r') as text:
    a = text.read()
ban = [',','-','!','.','?',' ']
lyrics_list = []
lyrics_word = ''
a = a.lower()
for i in a:
    if i == '\n':
        if lyrics_word:
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    elif i not in ban:
        lyrics_word += i
    else:
        if lyrics_word:
            lyrics_list.append(lyrics_word)
        lyrics_word = ''
b = {}
for i in lyrics_list:
    if i not in b:
        b[i] = 1
    if i in b:
        b[i] += 1
c = Counter(b)
print(c.most_common(6))
        

        




