# This is to Decode or Encode
# To run this code Hit RUN
# Put in your seed of choice(numbers only)
# Then Choose 1, 2 or 3
# If you do 1 that will encode
# if you choose 2 it will decode your pre-encoded letter
# if you choose 3 it will quit the program
# Made by Sammyjam1
# Hope you enjoy!
#
#
#
#
#
#


def words():
    print(
        'This is to Decode or Encode\nTo run this code Hit RUN\nPut in your seed of choice(numbers only)')
    print('Then Choose 1, 2 or 3\nIf you do 1 that will encode')
    print('if you choose 2 it will decode your pre-encoded letter\nif you choose 3 it will quit the program\n'
          'At any time you can type qt to quit\n')
    print('Made by Sammyjam1\nHope you enjoy!\n')


words()

jr = input("Seed - ")
if jr == 'qt':
    quit()
elif jr != 'qt':
    jr = int(jr)


def stop():
    def coder():
        ler = input('Enter letter(lowercase only)(rs to restart or qt to quit): ')
        if ler == 'q':
            print(jr * 11)
        if ler == 'w':
            print(jr * 12)
        if ler == 'e':
            print(jr * 13)
        if ler == 'r':
            print(jr * 14)
        if ler == 't':
            print(jr * 15)
        if ler == 'y':
            print(jr * 16)
        if ler == 'u':
            print(jr * 17)
        if ler == 'i':
            print(jr * 18)
        if ler == 'o':
            print(jr * 19)
        if ler == 'p':
            print(jr * 20)
        if ler == 'a':
            print(jr * 21)
        if ler == 's':
            print(jr * 22)
        if ler == 'd':
            print(jr * 23)
        if ler == 'f':
            print(jr * 24)
        if ler == 'g':
            print(jr * 25)
        if ler == 'h':
            print(jr * 26)
        if ler == 'j':
            print(jr * 27)
        if ler == 'k':
            print(jr * 28)
        if ler == 'l':
            print(jr * 29)
        if ler == 'z':
            print(jr * 30)
        if ler == 'x':
            print(jr * 31)
        if ler == 'c':
            print(jr * 32)
        if ler == 'v':
            print(jr * 33)
        if ler == 'b':
            print(jr * 34)
        if ler == 'n':
            print(jr * 35)
        if ler == 'm':
            print(jr * 36)
        if ler == 'rs':
            stop()
        if ler == 'qt':
            quit()
        while True:
            coder()

    def decoder():
        ler = input('Encoded numbers (qt to quit or rs to restart):  ')
        if ler == str(jr * 11):
            print('q')
        if ler == str(jr * 12):
            print('w')
        if ler == str(jr * 13):
            print('e')
        if ler == str(jr * 14):
            print('r')
        if ler == str(jr * 15):
            print('t')
        if ler == str(jr * 16):
            print('y')
        if ler == str(jr * 17):
            print('u')
        if ler == str(jr * 18):
            print('i')
        if ler == str(jr * 19):
            print('o')
        if ler == str(jr * 20):
            print('p')
        if ler == str(jr * 21):
            print('a')
        if ler == str(jr * 22):
            print('s')
        if ler == str(jr * 23):
            print('d')
        if ler == str(jr * 24):
            print('f')
        if ler == str(jr * 25):
            print('g')
        if ler == str(jr * 26):
            print('h')
        if ler == str(jr * 27):
            print('j')
        if ler == str(jr * 28):
            print('k')
        if ler == str(jr * 29):
            print('l')
        if ler == str(jr * 30):
            print('z')
        if ler == str(jr * 31):
            print('x')
        if ler == str(jr * 32):
            print('c')
        if ler == str(jr * 33):
            print('v')
        if ler == str(jr * 34):
            print('b')
        if ler == str(jr * 35):
            print('n')
        if ler == str(jr * 36):
            print('m')
        if ler == 'rs':
            stop()
        if ler == 'qt':
            quit()
        while True:
            decoder()

    which = input('Encode or Decode or Quit?(1, 2, 3)- ')
    if which == '1':
        coder()
    elif which == '2':
        decoder()
    elif which == '3':
        quit()
    elif which != '1':
        print('U no listen')
        stop()
    elif which != '2':
        print('U no listen')
        stop()
    elif which != '3':
        print('U no listen')
        stop()


stop()
