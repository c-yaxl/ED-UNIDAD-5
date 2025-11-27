import time

def ordenamiento_burbuja(arr):
    lista = arr.copy()
    n = len(lista)
    pasos = 0 # Contador de operaciones
    
    print(f"\n--- Iniciando Burbuja con: {lista} ---")
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            pasos += 1 # Contamos la comparación que sigue
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                pasos += 1 # Contamos el intercambio
                swapped = True
        
        print(f"🔄 Pasada {i+1}: {lista}")
        
        if not swapped:
            break
            
    return lista, pasos

def ordenamiento_insercion(arr):
    lista = arr.copy()
    pasos = 0
    print(f"\n--- Iniciando Inserción con: {lista} ---")
    
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        
        # El while hace comparaciones
        while j >= 0 and key < lista[j]:
            pasos += 1 # Contamos la comparación exitosa y el movimiento
            lista[j + 1] = lista[j]
            j -= 1
        
        pasos += 1 # Contamos la comparación que falló (rompió el while) o la inserción final
        lista[j + 1] = key
        
        print(f"➡️ Insertando el '{key}': {lista}")
        
    return lista, pasos

def ordenamiento_seleccion(arr):
    lista = arr.copy()
    n = len(lista)
    pasos = 0
    print(f"\n--- Iniciando Selección con: {lista} ---")
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            pasos += 1 # Contamos la comparación
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
            pasos += 1 # Contamos el intercambio
        
        print(f"📍 Posición {i} asegurada: {lista}")
        
    return lista, pasos

def main():
    print("--- 🚀 SORTING MASTER: STEP COUNTER EDITION ---")
    
    try:
        entrada = input("Ingresa números separados por comas (ej: 5,1,3,8): ")
        if not entrada: return
        datos = [int(x.strip()) for x in entrada.split(',')]
    except ValueError:
        print("❌ Error: Solo números enteros.")
        return

    while True:
        print("\n" + "="*40)
        print("¿Qué método quieres analizar?")
        print("1. Burbuja (Bubble Sort)")
        print("2. Inserción (Insertion Sort)")
        print("3. Selección (Selection Sort)")
        print("4. Salir")
        
        opcion = input("👉 Elige: ")

        if opcion == '4':
            print("Bye. 👋")
            break

        algoritmo = None
        
        if opcion == '1': algoritmo = ordenamiento_burbuja
        elif opcion == '2': algoritmo = ordenamiento_insercion
        elif opcion == '3': algoritmo = ordenamiento_seleccion
        else: continue

        # Medición de tiempo
        inicio = time.perf_counter()
        resultado_lista, total_pasos = algoritmo(datos) # Desempaquetamos los 2 valores que retorna
        fin = time.perf_counter()
        
        tiempo_total = fin - inicio

        print("-" * 40)
        print(f"✅ LISTA ORDENADA: {resultado_lista}")
        print(f"🔢 TOTAL DE PASOS (Op. Básicas): {total_pasos}")
        print(f"⏱️ TIEMPO REAL: {tiempo_total:.8f} seg")
        print("-" * 40)

if __name__ == "__main__":
    main()