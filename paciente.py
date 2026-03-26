class Paciente:

    def __init__(self, edad, frecuencia_cardiaca, temperatura,
                 tiene_sintomas_infecciosos, esta_vacunado, es_emergencia_critica):

        self.edad = edad
        self.frecuencia_cardiaca = frecuencia_cardiaca
        self.temperatura = temperatura
        self.tiene_sintomas_infecciosos = tiene_sintomas_infecciosos
        self.esta_vacunado = esta_vacunado
        self.es_emergencia_critica = es_emergencia_critica