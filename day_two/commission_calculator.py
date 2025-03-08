# On this lession you learn about data types and math operations
# floor division is a good one //, module is %

print(" * * * Calculadora de Comisiones del 13%  * * *")
nombre = input(" Cual es el nombre del empleado: ")
ventas = input(" Cuanto vendio en total?: ")

comision = 13/100

total_recibido = round(float(ventas) * comision, 2)

print(f" - El empleado {nombre}, que vendio un total de ${ventas}.00 pesos recibira:")
print(f"      ${total_recibido} pesos")
