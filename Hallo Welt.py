from random import shuffle

liste = "amazing excited amazing gorgeous blazing stunning bold stunning biggest tremendous \
    greatest fantastic phenomenal delightful ambitious exciting staggering outstanding \
    fantastic smarter gorgeous best massive incredible spectacular excited cool \
    magical revolutionary beautiful".upper().split()
shuffle(liste)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("SPAM ", end='') 
        print()

    print("{}  SPAM,  {}  SPAM!".format(liste.pop(), liste.pop()))
    print()