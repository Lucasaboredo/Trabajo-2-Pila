def ejercicio16(pila1, pila2):
    interseccion = []
    pilatemporal = []

    # Pasamos los personajes de la pila episodio V a una pila temporal.
    while pila1:
        pilatemporal.append(pila1.pop())

    # Y ahora comparamos esa temporal, con la pila episodio VII.
    while pilatemporal:
        elemento = pilatemporal.pop()
        if elemento in pila2:
            interseccion.append(elemento)

    return interseccion


#Despues cargamos ambas pila, llamamos a la funcion y la imprimimos.
pilaepV = ["Luke Skywalker", "Princess Leia", "Han Solo", "Darth Vader"]
pilaepVII = ["Rey", "Finn", "Kylo Ren", "Poe Dameron", "Han Solo"]

resultadointerseccion = ejercicio16(pilaepV, pilaepVII)

print("Intersección de pilas:", resultadointerseccion)

print("")
print("-----------------------------------------------------------------")
print("")
