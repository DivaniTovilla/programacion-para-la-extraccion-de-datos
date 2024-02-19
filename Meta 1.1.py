#################################### EJERCICO 1 ####################################################
semana1 = [20, 23, 35, 22, 35] #true

def duplicados (semana1):
    return len(semana1)!= len(set(semana1))
print (duplicados(semana1))

#################################### EJERCICO 2 ####################################################
print("------------------EJERCICO 2-------------------")
def encontrar_suma_dos_numeros(nums, target):
    # diccionario para almacenar los numeros
    num_indices = {}

    for i, num in enumerate(nums):
        complemento = target - num
        if complemento in num_indices:
            # si encontramos el complemento, retornamos los indices de los dos numeros
            return (num_indices[complemento], i)
        # Si no se encuentra, almacenamos el número actual y su indice
        num_indices[num] = i

    else: ValueError("No se encontraron dos numeros que sumen el objetivo")

nums = [10, 20, 30, 40, 50]
target = 80
try:
    indices = encontrar_suma_dos_numeros(nums, target)
    print(f"Los números en los indices {indices} suman el objetivo.")
except ValueError as e:
    print(e)

#################################### EJERCICO 3 ####################################################
print("-------------------EJERCICO 3-------------------")
def calcular_densidades(ciudades):
    #calcular la densidad de poblacion para cada ciudad
    densidades = {}
    for ciudad, poblacion, zona in ciudades:
        densidad = poblacion / zona
        densidades[ciudad] = densidad
    return densidades

def mayor_densidad(ciudades):
    #cuididad con la mayor densidad
    densidades = calcular_densidades(ciudades)
    ciudad_mayor_densidad = max(densidades, key=densidades.get)
    return ciudad_mayor_densidad

ciudades = [
    ("Tijuana", 5, "NoroEste"),
    ("Ciudad de Mexico", 8, "Centro"),
    ("Ensenada", 3, "NoroEste"),
    ("Puebla", 3, "Centro"),
    ("Cancun", 4, "Sur")
]
#zona en valor numerico
zonas = {"NoroEste": 100, "Centro": 150, "Sur": 200}
#conversion de zona a valor numérico
ciudades_con_zona_valor = [(ciudad, poblacion, zonas[zona]) for ciudad, poblacion, zona in ciudades]
densidades = calcular_densidades(ciudades_con_zona_valor)
mayor = mayor_densidad(ciudades_con_zona_valor)
print(densidades)
print(mayor)

#################################### EJERCICO 4 ####################################################
print("-------------------EJERCICO 4-------------------")
class Estadistica:
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros

    def frecuencia_numeros(self):
        frecuencia = {}
        for num in self.lista_numeros:
            if num in frecuencia:
                frecuencia[num] += 1
            else:
                frecuencia[num] = 1
        return frecuencia

    def moda(self):
        frecuencia = self.frecuencia_numeros()
        moda = max(frecuencia, key=frecuencia.get)
        return moda

    def histograma(self):
        frecuencia = self.frecuencia_numeros()
        for num, freq in frecuencia.items():
            print(f"{num}: {'*' * freq}")
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
estadistica = Estadistica(numeros)

# Frecuencia de numeros
print("Frecuencia de Números:")
print(estadistica.frecuencia_numeros())

# Moda
print("\nModa:")
print(estadistica.moda())

# Histograma
print("\nHistograma:")
estadistica.histograma()

####################################EJERCICO 5####################################################
print("-------------------EJERCICO 5-------------------")
def detectar_cambios(estado_anterior, estado_actual):
    cambios = {}
    # verificar elementos que han sido eliminados o modificados en el estado actual
    for elemento in estado_anterior:
        if elemento not in estado_actual:
            cambios[elemento] = (estado_anterior[elemento], None)  # Elemento eliminado
        elif estado_anterior[elemento] != estado_actual[elemento]:
            cambios[elemento] = (estado_anterior[elemento], estado_actual[elemento])  # Elemento modificado
    # Verificar elementos que han sido añadidos en el estado actual
    for elemento in estado_actual:
        if elemento not in estado_anterior:
            cambios[elemento] = (None, estado_actual[elemento])  # Elemento añadido
    return cambios

estado_anterior = {'a': 1, 'b': 2, 'c': 3}
estado_actual = {'a': 1, 'b': 5, 'd': 4}
cambios = detectar_cambios(estado_anterior, estado_actual)
print(cambios)

#################################### EJERCICO 6 ####################################################
print("-------------------EJERCICO 6-------------------")
class SistemaReserva:
    def __init__(self, total_habitaciones):
        #sistema de reserva y el numero de habitaciones
        self.total_habitaciones = total_habitaciones
        #habitaciones disponibles, todas estan disponibles.
        self.habitaciones_disponibles = set(range(1, total_habitaciones + 1))
        #habitaciones reservadas, vacio.
        self.habitaciones_reservadas = set()

    def realizar_reserva(self, habitacion):
        #reserva en una habitacion
        if habitacion in self.habitaciones_disponibles:
            # Si la habitación esta disponible se reserva
            self.habitaciones_disponibles.remove(habitacion)
            self.habitaciones_reservadas.add(habitacion)
            print(f"Se ha reservado la habitacion {habitacion}")
        else:
            print(f"La habitacion {habitacion} no esta disponible")

    def liberar_habitacion(self, habitacion):
        #liberar una habitacion reservada
        if habitacion in self.habitaciones_reservadas:
            self.habitaciones_reservadas.remove(habitacion)
            self.habitaciones_disponibles.add(habitacion)
            print(f"Se ha liberado la habitacion {habitacion}")
        else:
            print(f"La habitacion {habitacion} no esta reservada")
    def mostrar_disponibilidad(self):
        #disponiblilidad de habitaciones
        print("Habitaciones disponibles:", self.habitaciones_disponibles)
        print("Habitaciones reservadas:", self.habitaciones_reservadas)
sistema_reserva = SistemaReserva(total_habitaciones=10)
#reservas
sistema_reserva.realizar_reserva(3)
sistema_reserva.realizar_reserva(5)
#disponibilidad actual
sistema_reserva.mostrar_disponibilidad()
#liverar habitacion
sistema_reserva.liberar_habitacion(3)
#muestra la disponibilidad
sistema_reserva.mostrar_disponibilidad()

#################################### EJERCICO 7 ####################################################
print("-------------------EJERCICO 7-------------------")

class SistemaEncriptacion:
    def __init__(self):
        #diccionario de encriptacion
        self.diccionario_encriptacion = {
            'a': '$%3', 'b': '8@*', 'c': '2&9', 'd': '!#7', 'e': '+*4',
            'f': '5@&', 'g': '9!$', 'h': '&*1', 'i': '^%6', 'j': '7#*',
            'k': '*@8', 'l': '3$!', 'm': '6&^', 'n': '@7%', 'o': '1&*',
            'p': '&5@', 'q': '#^2', 'r': '!4$', 's': '4*%', 't': '2#^',
            'u': '8^&', 'v': '%6!', 'w': '$9*', 'x': '^+3', 'y': '7!@',
            'z': '*%5'}

    def encriptar_mensaje(self, mensaje):
        #Encripta un mensajeutilizando el diccionario
        return ''.join(self.diccionario_encriptacion.get(caracter.lower(), caracter) for caracter in mensaje)

    def desencriptar_mensaje(self, mensaje_encriptado):
        #Desencripta un mensaje
        diccionario_desencriptacion = {valor: clave for clave, valor in self.diccionario_encriptacion.items()}
        codigo_secreto_actual = ''
        mensaje_desencriptado = ''
        for caracter in mensaje_encriptado:
            codigo_secreto_actual += caracter
            if codigo_secreto_actual in diccionario_desencriptacion:
                mensaje_desencriptado += diccionario_desencriptacion[codigo_secreto_actual]
                codigo_secreto_actual = ''
        return mensaje_desencriptado

    def obtener_diccionario_encriptacion(self):
        #retorna el diccionario
        return self.diccionario_encriptacion

sistema = SistemaEncriptacion()

mensaje_original = "hola"
mensaje_encriptado = sistema.encriptar_mensaje(mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = sistema.desencriptar_mensaje(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

#################################### EJERCICO 8 ####################################################
print("-------------------EJERCICO 8-------------------")
class InventarioProductos:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, codigo, nombre, precio, cantidad):
        #agrega un nuevo producto al inventario
        if codigo not in self.inventario:
            self.inventario[codigo] = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
            print(f"Producto {nombre} agregado al inventario")
        else:
            print("El producto ya se encuentra en el inventario.")

    def editar_producto(self, codigo, **kwargs):
        #edita el producto
        if codigo in self.inventario:
            for key, value in kwargs.items():
                if key in self.inventario[codigo]:
                    self.inventario[codigo][key] = value
            print("Producto actualizado correctamente")
        else:
            print("El producto no existe en el inventario")

    def eliminar_producto(self, codigo):
        #Elimina un producto del inventario
        if codigo in self.inventario:
            del self.inventario[codigo]
            print("Producto eliminado del inventario.")
        else:
            print("El producto no existe en el inventario.")

    def realizar_venta(self, codigo, cantidad):
        #se realiza la venta y se actuliza el inventario
        if codigo in self.inventario:
            if self.inventario[codigo]['cantidad'] >= cantidad:
                self.inventario[codigo]['cantidad'] -= cantidad
                print("Venta realizada correctamente")
            else:
                print("No hay suficiente stock para realizar la venta")
        else:
            print("El producto no existe en el inventario.")

    def imprimir_inventario(self):
        #se imprime el inventario
        print("Inventario de Productos:")
        for codigo, producto in self.inventario.items():
            print(f"Código: {codigo}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

inventario = InventarioProductos()
#agregar productos al inventario
inventario.agregar_producto('001', 'Camisa', 20.99, 50)
inventario.agregar_producto('002', 'Pantalón', 30.50, 30)
#imprime inventario
inventario.imprimir_inventario()
#realiza una venta
inventario.realizar_venta('001', 10)
#imprime inventario despues de la venta
inventario.imprimir_inventario()
#editar un producto
inventario.editar_producto('002', precio=35.0)
#imprimir inventario actualizado
inventario.imprimir_inventario()
#elimina un producto
inventario.eliminar_producto('002')
# Imprime nuevamente
inventario.imprimir_inventario()
