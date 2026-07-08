# Auxiliar: Verifica si un codigo existe (sin importar mayusculas/minusculas)
def buscar_codigo(juegos, codigo):
    for c in juegos:
        if c.upper() == codigo.upper():
            return True
    return False

# Op. 1: Stock por plataforma
def stock_plataforma(juegos, inventario, plataforma):
    total = 0
    for cod, datos in juegos.items():
        if datos[1].lower() == plataforma.lower():
            total += inventario[cod][1] # Se suma el stock (posición 1 de inventario)
    print(f"El total de stock disponibles es: {total}")

# Op. 2: Busqueda por precio
def busqueda_precio(juegos, inventario, p_min, p_max):
    encontrados = []
    for cod, inv in inventario.items():
        precio, stock = inv[0], inv[1]
        if p_min <= precio <= p_max and stock > 0:
            titulo = juegos[cod][0]
            encontrados.append(f"{titulo}--{cod}")
    
    encontrados.sort() # Ordena alfabeticamente por titulo
    
    if len(encontrados) == 0:
        print("No hay juegos en ese rango de precios.")
    else:
        print(f"Los juegos encontrados son: {encontrados}")

# Op. 3: Actualizar precio
def actualizar_precio(juegos, inventario, codigo, nuevo_precio):
    if buscar_codigo(juegos, codigo):
        # Buscar la clave exacta en el diccionario
        for c in inventario:
            if c.upper() == codigo.upper():
                inventario[c][0] = nuevo_precio
                return True
    return False

# Op. 4: Agregar juego
def agregar_juego(juegos, inventario, codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    if buscar_codigo(juegos, codigo):
        return False
    
    cod_up = codigo.upper()
    juegos[cod_up] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[cod_up] = [precio, stock]
    return True

# Op. 5: Eliminar juego
def eliminar_juego(juegos, inventario, codigo):
    if buscar_codigo(juegos, codigo):
        for c in list(juegos.keys()):
            if c.upper() == codigo.upper():
                del juegos[c]
                del inventario[c]
                return True
    return False


# Programa principal

def main():
    
    juegos = {
        'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
        'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
        'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
        'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
        'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
        'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
    }

    inventario = {
        'G001': [9990, 7],
        'G002': [19990, 0],
        'G003': [42990, 3],
        'G004': [14990, 5],
        'G005': [17990, 9],
        'G006': [39990, 2],
    }

    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Busqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")

        opc = input("Seleccione una opcion (1-6): ")

        # Validacion simple
        if not opc.isdigit() or int(opc) not in range(1, 7):
            print("Debe seleccionar una opcion valida")
            continue

        opcion = int(opc)

        if opcion == 1:
            plat = input("Ingrese plataforma a consultar: ")
            stock_plataforma(juegos, inventario, plat)
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    busqueda_precio(juegos, inventario, p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif opcion == 3:
            cod = input("Ingrese codigo del juego: ")
            try:
                precio = int(input("Ingrese nuevo precio: "))
                if actualizar_precio(juegos, inventario, cod, precio):
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")
            except ValueError:
                print("Precio invalido")

            resp = input("¿Desea actualizar otro precio? (s/n): ")
        elif opcion == 4:
            cod = input("Ingrese codigo del juego: ")
            titulo = input("Ingrese titulo del juego: ")
            plat = input("Ingrese plataforma del juego: ")
            gen = input("Ingrese genero del juego: ")
            clas = input("Ingrese clasificacion del juego: ")
            multi = input("¿Es multijugador? (s/n): ").lower() == 's'
            editor = input("Ingrese editor del juego: ")

            try:
                precio = int(input("Ingrese precio: "))
                stock = int(input("Ingrese stock: "))
                
                # Validaciones
                if clas not in ['E', 'T', 'M'] or precio <= 0 or stock < 0:
                    print("Datos no validos")
                elif agregar_juego(juegos, inventario, cod, titulo, plat, gen, clas, multi, editor, precio, stock):
                    print("Juego agregado")
                else:
                    print("El codigo ya existe")
            except ValueError:
                print("Error en datos numericos")
        elif opcion == 5:
            cod = input("Ingrese codigo del juego: ")
            if eliminar_juego(juegos, inventario, cod):
                print("Juego eliminado")
            else:
                print("El codigo no existe")
        elif opcion == 6:
            print("Programa Finalizado...")
            break

#Aqui se ejecuta el programa
main()




