from paciente import Paciente


pacientes = [

    Paciente(70, 90, 38.5, True, False, False),
    Paciente(8, 110, 39.2, False, True, False),
    Paciente(30, 80, 36.5, False, True, False),
    Paciente(0, 80, 36.5, False, True, False)

]


for paciente in pacientes:

    prioridad = paciente.clasificar_prioridad()
    destino = paciente.asignar_destino()

    print("Resumen del paciente")
    print("Edad:", paciente.edad)
    print("Prioridad:", prioridad)
    print("Destino:", destino)
    print("---------------------")
