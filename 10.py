file = open("hightemp.txt", "r")
line = file.readline()
cont = 0
while line :
	cont += 1
	line = file.readline()
print(cont)
file.close
