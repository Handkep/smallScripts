from random import random, randint

def überprüfe(zahl, generierteZahl):
    if(zahl==generierteZahl):
        return True
    return False


def startSpiel():
    randomZahl = randint(0,10)
    counter = 0
    while True:
        counter+=1
        eingabe = int(input("rate eine Zahl zwischen 0 und 10\n"))
        print(f"du hast die zahl {eingabe} eingegeben")
        if überprüfe(eingabe,randomZahl):
            print(f"WOW! Du hast die Zahl erraten!, du hast {counter} versuche gebraucht!")
            exit()
        else:
            print("Das ist leider falsch:(")
        




startSpiel()

    
