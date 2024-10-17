# complejidad O(n)  n: cantidad de monedas
# Devuelve la suma de sophie y mateo
def jugar_fila_monedas_greedy(monedas):
    sophia_suma = 0
    mateo_puntos = 0
    mejor_opcion = 0
    peor_opcion = 0
    turno_sophia = True
    while monedas:
        if monedas[0] >= monedas[-1]:
            if turno_sophia:
                mejor_opcion = monedas.pop(0)
            else:
                peor_opcion = monedas.pop(-1)
            
        else:
            if turno_sophia:
                mejor_opcion = monedas.pop(-1)
            else:
                peor_opcion = monedas.pop(0)
            
            
        
        if turno_sophia:
            sophia_suma += mejor_opcion
        else:
            mateo_puntos += peor_opcion
    
        turno_sophia = not turno_sophia

    return sophia_suma, mateo_puntos

# Complejidad O(n), recorre la lista entera de monedas una vez
def fila_de_monedas(monedas: list):
    puntaje_sophia= 0
    puntaje_mateo = 0
    inicio = 0
    fin = len(monedas) - 1
    turno_sophia = True

    while inicio <= fin:
        if turno_sophia == True:
            if monedas[inicio] > monedas[fin]:
                puntaje_sophia += monedas[inicio]
                inicio += 1
            else:
                puntaje_sophia += monedas[fin]
                fin -= 1
        else:
            if monedas[inicio] > monedas[fin]:
                puntaje_mateo += monedas[fin]
                fin -= 1
            else:
                puntaje_mateo += monedas[inicio]
                inicio += 1
        turno_sophia = not turno_sophia

    return puntaje_sophia, puntaje_mateo

#Para probar los distintos txt
def extraer_monedas_archivo(nombre_archivo: str) -> list:
    arch = open(nombre_archivo, "r")
    arch.readline()
    linea_numeros = arch.readline()
    numeros = [int(num) for num in linea_numeros.split(';')]

    return numeros


#Caso de ejemplo
monedas = extraer_monedas_archivo("TP1/100.txt")

print(jugar_fila_monedas_greedy([72, 165, 794, 892, 880, 341, 882, 570, 679, 725, 979, 375, 459, 603, 112, 436, 587, 699, 681, 83]))
print(fila_de_monedas(monedas))