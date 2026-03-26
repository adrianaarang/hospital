from paciente import Paciente



paciente1 = Paciente(70, 90, 38.5, True, False, False)
paciente2 = Paciente(8, 110, 39.2, False, True, False)
paciente3 = Paciente(30, 80, 36.5, False, True, False)
paciente4 = Paciente(0, 80, 36.5, False, True, False)



pacientes = [paciente1, paciente2, paciente3, paciente4]



for paciente in pacientes:


    if paciente.es_emergencia_critica or paciente.temperatura > 41:
        prioridad = "Roja"

    elif paciente.temperatura >= 39 and paciente.frecuencia_cardiaca > 100:
        prioridad = "Naranja"

    elif paciente.edad < 12 or paciente.edad > 65:
        prioridad = "Amarilla"

    else:
        prioridad = "Verde"



    if paciente.tiene_sintomas_infecciosos and not paciente.esta_vacunado:
        destino = "Box de Aislamiento"

    else:
        destino = "Sala de Espera General"



    print("Resumen del paciente")
    print("Edad:", paciente.edad)
    print("Prioridad:", prioridad)
    print("Destino:", destino)
