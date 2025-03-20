diccionario= [{"nombre": "mar","edad":32,"ciudad": "madrid"}, {"nombre": "juan","edad": 25,"ciudad": "barcelona"},
    { "nombre": "Juan", "edad": 30, "ciudad": "Bogotá" }]
k=int(input('ingrese un numero para encontrar el nombre: '))
v=str(input('ingrese el valor que busca: '))
print( diccionario[k][v] )  