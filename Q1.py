def validaConjunto(entrada):
	validos = {".","0","1","2","3","4","5","6","7","8","9"}
	if validos in entrada:
		auxiliar = true
	else:
		return false
	return auxiliar

def valida(entrada):
	if entrada.isDigit:
		return true
	elif "+" == entrada[0] or "-" == entrada[0]:
		if entrada[1:len(entrada)].isDigit:
			return true
		else:
			return validaConjunto(entrada[1:len(entrada)])
	else:
		if validaConjunto(entrada):
			return true
		else:
			return false
			
numerosIntReal = input()
lista = [None]
aux = 0
if numerosIntReal != "" :
    while (numerosIntReal != ""):
        if valida(numerosIntReal):
            lista.append() = numerosIntReal
            aux += 1
            numerosIntReal = input()           
    print("Lista de Números Válidos Lidos = ", lista)
else:
    print("Lista de Números Válidos Lidos = []")