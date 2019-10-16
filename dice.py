
import random
p_pos = 1
c_pos = 1

grid = 30

def field(pos, p):
    print('◯' * (pos-1) + p + '◯' * (grid-pos))
# field(p_pos, 'P')
# field(c_pos, 'C')

iter = 10
for i in range(iter):
    field(p_pos, 'P')
    field(c_pos, 'C')
    print('role dice !\nsay yes to continue' )
    cont = input()
    if cont == "yes":
        p_dice = random.randint(0,6)
        c_dice = random.randint(0,6)
        print('your dice number is {} !'.format(p_dice))
        # input('hit enter')
        print('your dice number is {} !'.format(c_dice))
        p_pos += p_dice
        c_pos += c_dice

        if p_pos >= 30:
            print('you win congrat!')
            break
        elif c_pos >= 30:
            print('you lose !')
            break

    else:
        print('are you sure?\nsay yes to quit')
        cont == 'yes'
        break
print('game is over')
        
