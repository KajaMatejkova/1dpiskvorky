from random import randrange

m = "--------------------"

def tah(m, pozice , znak):
    return m[:pozice] + znak + m[pozice + 1:]

def tahhrace(m):
    while True:
        pozice = int(input("Zadej číslo pole: "))-1 #0-19
        if (pozice <0) or (pozice >19) :
            print("Zadej číslo mezi 1 a 20, prosím")
        elif m[pozice] == "-" :
            break

    return tah(m,pozice,"o")

def tahpocitace(m):
    pozice = None
    for i in range(20):

        if i<18 and m[i:i+3]=="xx-":
            pozice = i + 2
        elif i<18 and m[i:i+3]=="-xx":
            pozice = i
        elif i<18 and m[i:i+3]=="x-x":
            pozice = i + 1

    if pozice is not None:
        return tah(m, pozice,"x")

    for i in range(20):
        if i<18 and m[i:i+3]=="o-o":
            pozice = i + 1
        elif i<18 and m[i:i+3]=="oo-":
            pozice = i + 2
        elif i<18 and m[i:i+3]=="-oo":
            pozice = i

    if pozice is not None:
        return tah(m, pozice,"x")

    for i in range(20):
        if i<18 and m[i:i+3]=="-o-":
            pozice = i
    if pozice is not None:
        return tah(m, pozice,"x")

    for i in range(20):
        if i<19 and m[i] == "x" and (m[i+1])== "-":
            pozice = i + 1
        elif  i>0 and m[i] == "x" and (m[i-1])== "-":
            pozice = i -1
    if pozice is not None:
        return tah(m, pozice,"x")

        
    while True:
        pozice = randrange (20)
        if m[pozice] == "-" :
            return(tah(m,pozice,"x"))

def poznejviteze ():

    if "xxx" in m:
        print("Vyhrál počítač")
        return True

    if "ooo" in m:
        print("Vyhráli hráč")
        return True

    if "-" not in m:
        print("Nikdo nevyhrál")
        return True
    return False


while True:

    m = tahhrace(m)
    if poznejviteze() :
        break
    print(m)
    m = tahpocitace(m)
    if poznejviteze() :
        break

    print(m)
