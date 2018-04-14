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

	return(tah(m,pozice,"o"))

def tahpocitace(m):

	for i in range(20):

		pozice = None

		if i<18 and m[i:i+3]=="xx-":
			pozice = i + 2
		elif i<18 and m[i:i+3]=="-xx":
			pozice = i
		elif i<18 and m[i:i+3]=="x-x":
			pozice = i + 1
		elif i<18 and m[i:i+3]=="o-o":
			pozice = i + 1
		elif i<18 and m[i:i+3]=="oo-":
			pozice = i + 2
		elif i<18 and m[i:i+3]=="-oo":
			pozice = i
		elif i<19 and m[i] == "x" and (m[i+1])== "-":
			pozice = i + 1
		elif  i>0 and m[i] == "x" and (m[i-1])== "-":
			pozice = i -1

		else :
			continue

		return(tah(m,pozice,"x"))

	while True:
		pozice = randrange (20)
		if m[pozice] == "-" :
			return(tah(m,pozice,"x"))


while True:

	m = tahhrace(m)
	m = tahpocitace(m)
	print(m)

	if ("xxx" in m) and ("ooo" in m):
		print("Remíza")
		break

	if "xxx" in m:
		print("Vyhrál počítač")
		break

	if "ooo" in m:
		print("Vyhráli hráč")
		break

	if "-" not in m:
		print("Nikdo nevyhrál")
		break

print(m)
