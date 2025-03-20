palabras=['mono', 'casa','mesa']
cantPalabras=len(palabras)
cant=0
def cantPal(palabras,cant,cantPalabras):
    for palabra in palabras:
        cant+=1
    return cant
print(cantPal(palabras,cant,cantPalabras))