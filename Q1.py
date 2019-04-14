def validaConjunto(entrada):
	validos= set(".","0","1","2","3","4","5","6","7","8","9")
	if validos in entrada:
		return true
	else:
		return false

def valida(entrada):
	if entrada.isDigit:
		return true
	elif "+" == entrada[0] or "-" == entrada[0]:
		if entrada[1:len(entrada)].isDigit:
			return true
		else:
			validaConjunto(entrada[1:len(entrada)])
	else:
		if validaConjunto(entrada):
			return true
		else:
			return false