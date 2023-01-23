f = open('mat_dv.txt', 'r')

for i in f:
    s = i.split()
    m = max(s[3])
    m2 = max(s[4])
    if (s[3][4] < m + m2) and (int(s[2]) = '8'):
        print('Победитель 8 класса:', s[0][1], m + m2)
    elif (s[3][4] < m + m2) and (int(s[2]) = '9'):
        print('Победитель 9 класса:', s[0][1], m + m2)
    elif (s[3][4] < m + m2) and (int(s[2]) = '10'):
        print('Победитель 10 класса:', s[0][1], m + m2)
f.close()

f = open('mat_dv.txt', 'r')

for i in f:
    s = i.split()
    m = max(s[3])
    m2 = max(s[4])
    if (s[3] < m) and (int(s[2]) = '8'):
        print('Победитель 8 класса:', s[0][1], m)
    elif (s[3] < m) and (int(s[2]) = '9'):
        print('Победитель 9 класса:', s[0][1], m)
    elif (s[3] < m) and (int(s[2]) = '10'):
        print('Победитель 10 класса:', s[0][1], m)
    elif (s[4] < m2) and (int(s[2]) = '8'):
        print('Победитель 8 класса:', s[0][1], m2)
    elif (s[4] < m2) and (int(s[2]) = '9'):
        print('Победитель 9 класса:', s[0][1], m2)
    elif (s[4] < m2) and (int(s[2]) = '10'):
        print('Победитель 10 класса:', s[0][1], m2)

f.close()









