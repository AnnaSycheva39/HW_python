# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

import re
from types import NoneType
s = "мама родина мир сын дочь отец дом ветер"

#words = s.split()
words = re.split('\W+', s)

ex = ["а", "б", "в"]

# for i in range(len(words)):
#     if words[i].find(ex[0]) != -1 and words[i].find(ex[1]) != -1 and words[i].find(ex[2]) != -1:
#         words[i] = None
for i in range(len(words)-1, -1, -1):
    print (i)
    if words[i].find(ex[0]) != -1 and words[i].find(ex[1]) != -1 and words[i].find(ex[2]) != -1:
        #print(words.pop(i))
        del words[i]
print(words)
#print (' '.join(words))
# words = [txt for txt in words if txt]
# print(*words)