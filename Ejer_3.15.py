class Calificacion:
    def __init__(self, calificacion, asistencia):
        self.calificacion = calificacion
        self.asistencia = asistencia

    def obtener_calificacion(self):
        if self.calificacion > 9.0 and self.asistencia == 1:
            return "A Excelente con Mención Honorífica"
        elif self.calificacion > 9.0 and self.asistencia != 1:
            return "A Excelente"
        elif self.calificacion > 8.0 and self.asistencia == 1:
            return "B Muy bien con Mención"
        elif self.calificacion > 8.0 and self.asistencia != 1:
            return "B Muy Bien"
        elif self.calificacion > 7.5:
            return "C Bien"
        else:
            return "R Reprobado. Lo siento mucho"

    def mostrar_resultado(self):
        print(f"La calificación es {self.obtener_calificacion()}")


calificacion_numerica = float(input("Dame una calificación: \n"))
asistencia = int(input('Dame la asistencia: 1 si asistió o 0 si no asistió: \n'))
mi_calificacion = Calificacion(calificacion_numerica, asistencia)
mi_calificacion.mostrar_resultado()
