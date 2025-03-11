# Prueba de indices
frase = "Esta es una prueba, donde vamos a poner a prueba los indices"
print(f"de la frase: \"{frase}\"")
indice = frase.index("prueba")
print(f"La primer aparicion de prueba esta en: {indice}")
rindice = frase.rindex("prueba")
print(f"La ultima aparicion de prueba esta en: {rindice}")

# framentar o extraer strings
print(" Extraigamos lo que hay despues de la ultima aparicion de prueba:")
extraccion = frase[rindice:]
print(f"{extraccion}")
print("Ahora lo que hay antes de la primer aparicion de prueba:")
lodemas = frase[:rindice]
print(f"{lodemas}")
print("Vamor a imprimir toda la frase pero alreves:")
# [inicio:final:de cuanto en cuanto]
alreves = frase[::-1]
print(f"{alreves}")