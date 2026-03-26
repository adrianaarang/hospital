class Paciente:

    def __init__(self, edad, frecuencia_cardiaca, temperatura,
                 tiene_sintomas_infecciosos, esta_vacunado, es_emergencia_critica):

        self.edad = edad
        self.frecuencia_cardiaca = frecuencia_cardiaca
        self.temperatura = temperatura
        self.tiene_sintomas_infecciosos = tiene_sintomas_infecciosos
        self.esta_vacunado = esta_vacunado
        self.es_emergencia_critica = es_emergencia_critica


    def clasificar_prioridad(self):

        if self.es_emergencia_critica or self.temperatura > 120:
            return "Roja"

        elif self.temperatura >= 39 and self.frecuencia_cardiaca > 100:
            return "Naranja"

        elif self.edad < 12 or self.edad > 65:
            return "Amarilla"

        else:
            return "Verde"


    def asignar_destino(self):

        if self.tiene_sintomas_infecciosos and not self.esta_vacunado:
            return "Box de Aislamiento"

        else:
            return "Sala de Espera General"
