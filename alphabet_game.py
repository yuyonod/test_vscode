import random
import datetime
alpha = []

for a in 'ABCDEFG':
    alpha.append(a)

r = random.choice(alpha)
ans = ''
for i in alpha:

    if r != i:
        ans= ans+i

print(ans)
st = datetime.datetime.now()
inp = input('whats is unknown alphabet in this sequence?')
et = datetime.datetime.now()

if inp ==r:
    print('correct ! you took {} second'.format((et-st).seconds) )