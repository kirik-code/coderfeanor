import random
import rubailer

def GnrtRubai():
    x = random.choice(rubailer.poems)
    print(x)

print('*' * 100)
print('''Rastegele rubai görüntüleyiciye hoş geldiniz.''')
print('*' * 100)
print('-\n')

while True:
    print('#' * 100)
    gnrt = input('Rubai için "1" çıkmak için "0":')
    print('#' * 100)

    if gnrt == '1':
        GnrtRubai()

    elif gnrt == '0':
        print('\nİyi günler...\n')
        break

    else:
        print('\nLütfen yalnızca "1" yada "0" kullanınız...\n')


'''50 şiir'''