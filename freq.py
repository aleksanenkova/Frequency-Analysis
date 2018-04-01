# -*- encoding: utf-8 -*-

import io
import sys
import locale

spaces = 0
ALPH = u'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТТЬБЮ'

def to_unicode(source):
    return source.decode(sys.stdin.encoding or locale.getprefferedencoding(True))


text = io.open(sys.argv[1], mode='r', encoding='UTF-8').read().upper()
l = len(text)

for x in range (0,l):
    a = text[x]
    if a == " ":
        spaces+=1
count = 0
freq = {}
for sym in text:
    if sym not in ALPH: continue

    if freq.get(sym, None) == None:
        freq[sym] = 1.
    else:
        freq[sym] += 1.

    count += 1.


print u'Всего символов: %d' %(len(text))
print u'Всего слов: %d' %(count)
print u'Пробелов: %d' %(spaces)
print u'Частотный анализ записан в файл'
for sym in ALPH:
    if freq.get(sym, None) == None:
        freq[sym] = 0.

with open(sys.argv[2], 'wb') as F:
    data = sorted(freq.items(), key=lambda x: x[1])
    # data.reverse()
    for k,v in data:
        F.write((u"%s: %d | %.3f\n" % (k, v, v*100/count)).encode('UTF-8'))


