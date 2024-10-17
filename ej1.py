def sumatoria_maxima(arr: list, conjunto_sophia: list):
    if(arr[0] > arr[-1]):
        conjunto_sophia.append(arr.pop(0))
    else:
        conjunto_sophia.append(arr.pop(-1))
    return

def sumatoria_minima(arr: list, conjunto_mateo: list):
    if(arr[0] > arr[-1]):
        conjunto_mateo.append(arr.pop(-1))
    else:
        conjunto_mateo.append(arr.pop(0))
    return

def jugar(arr: list, conjunto_sophia: list, conjunto_mateo: list):
    for _n in range(len(arr) // 2):
        sumatoria_maxima(arr, conjunto_sophia)
        sumatoria_minima(arr, conjunto_mateo)
    if len(arr) == 1:
        conjunto_sophia.append(arr.pop())
    
    return (conjunto_sophia, conjunto_mateo)
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










#Caso de ejemplo
monedas = [72, 165, 794, 892, 880, 341, 882, 570, 679, 725, 979, 375, 459, 603, 112, 436, 587, 699, 681, 83]
conjunto_sophia = []
conjunto_mateo = []

print(monedas)
print(jugar(monedas, conjunto_sophia, conjunto_mateo))
print(sum(conjunto_sophia), sum(conjunto_mateo))

print(jugar_fila_monedas_greedy([72, 165, 794, 892, 880, 341, 882, 570, 679, 725, 979, 375, 459, 603, 112, 436, 587, 699, 681, 83]))
