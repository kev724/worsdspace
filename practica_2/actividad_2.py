class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Lista de tuplas (hora_inicio, hora_fin)

    def agregar_horario(self, hora_inicio, hora_fin):
        if hora_inicio < hora_fin:
            self.horarios.append((hora_inicio, hora_fin))
        else:
            print("Error: La hora de inicio debe ser menor que la hora de fin.")

    def esta_disponible(self, hora_inicio, hora_fin):
        for horario in self.horarios:
            if not (hora_fin <= horario[0] or hora_inicio >= horario[1]):
                return False
        return True


class Buses:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []
        self.conductor_asignado = None

    def agregar_ruta(self, ruta):
        self.ruta = ruta

    def agregar_horario(self, hora_inicio, hora_fin):
        if hora_inicio < hora_fin:
            self.horarios.append((hora_inicio, hora_fin))
        else:
            print("Error: La hora de inicio debe ser menor que la hora de fin.")

    def asignar_conductor(self, conductor):
        if self.conductor_asignado is None:
            for horario in self.horarios:
                if not conductor.esta_disponible(horario[0], horario[1]):
                    print(f"Error: El conductor {conductor.nombre} no está disponible en el horario {horario}.")
                    return
            self.conductor_asignado = conductor
            for horario in self.horarios:
                conductor.agregar_horario(horario[0], horario[1])
            print(f"Conductor {conductor.nombre} asignado al bus {self.placa}.")
        else:
            print(f"Error: El bus {self.placa} ya tiene un conductor asignado.")


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self):
        placa = input("Ingrese la placa del bus: ")
        bus = Buses(placa)
        self.buses.append(bus)
        print(f"Bus {placa} agregado correctamente.")

    def agregar_ruta_a_bus(self):
        placa = input("Ingrese la placa del bus: ")
        bus = self._buscar_bus(placa)
        if bus:
            ruta = input("Ingrese la ruta: ")
            bus.agregar_ruta(ruta)
            print(f"Ruta {ruta} agregada al bus {placa}.")
        else:
            print(f"Error: No se encontró el bus con placa {placa}.")

    def registrar_horario_a_bus(self):
        placa = input("Ingrese la placa del bus: ")
        bus = self._buscar_bus(placa)
        if bus:
            hora_inicio = int(input("Ingrese la hora de inicio (formato 24h): "))
            hora_fin = int(input("Ingrese la hora de fin (formato 24h): "))
            bus.agregar_horario(hora_inicio, hora_fin)
            print(f"Horario {hora_inicio}-{hora_fin} agregado al bus {placa}.")
        else:
            print(f"Error: No se encontró el bus con placa {placa}.")

    def agregar_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado correctamente.")

    def agregar_horario_a_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = self._buscar_conductor(nombre)
        if conductor:
            hora_inicio = int(input("Ingrese la hora de inicio (formato 24h): "))
            hora_fin = int(input("Ingrese la hora de fin (formato 24h): "))
            conductor.agregar_horario(hora_inicio, hora_fin)
            print(f"Horario {hora_inicio}-{hora_fin} agregado al conductor {nombre}.")
        else:
            print(f"Error: No se encontró el conductor {nombre}.")

    def asignar_bus_a_conductor(self):
        placa = input("Ingrese la placa del bus: ")
        bus = self._buscar_bus(placa)
        if bus:
            nombre = input("Ingrese el nombre del conductor: ")
            conductor = self._buscar_conductor(nombre)
            if conductor:
                bus.asignar_conductor(conductor)
            else:
                print(f"Error: No se encontró el conductor {nombre}.")
        else:
            print(f"Error: No se encontró el bus con placa {placa}.")

    def _buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus
        return None

    def _buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None

    def menu(self):
        while True:
            print("\n--- Menú de Administración ---")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_bus()
            elif opcion == "2":
                self.agregar_ruta_a_bus()
            elif opcion == "3":
                self.registrar_horario_a_bus()
            elif opcion == "4":
                self.agregar_conductor()
            elif opcion == "5":
                self.agregar_horario_a_conductor()
            elif opcion == "6":
                self.asignar_bus_a_conductor()
            elif opcion == "7":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")


# Ejecución del programa
if __name__ == "__main__":
    admin = Admin()
    admin.menu()
