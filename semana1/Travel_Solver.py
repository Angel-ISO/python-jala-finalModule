""" 
Analisis

- viajes en autobús que duren más de 12 horas. Marean a nuestro usuario. sin mencionar la diferencia de lenguaje. poco ingles y japones
- opciones limitadas. solo podemos hacer uso de las opciones predefinidas
- buscar nuevas opciones

Diseño

- organizar viaje
- calcular costo
- viabilidad del pasajero


algoritmo
para el viaje 

- en base a los requerimientos seleccionar mejor viaje
- comprar el voleto
- subir al avion
- realizar las paradas especificas en el viaje seleccionado
- llegada

 """


class Travel_Solver:
    def __init__(self, budget, max_bus_duration, language_preference):
        self.budget = budget
        self.max_bus_duration = max_bus_duration
        self.language_preference = language_preference

    def select_best_option(self):
        if self.max_bus_duration <= 12 and self.budget >= 5550:
            return " Flight to Brazil next to Flight to Hawaii next to Flight to Japan $5550"
        if self.max_bus_duration > 12 and self.budget >= 5500:
            return " Flight to Peru next to Flight to Mexico next to Flight to Japan $5500"
        if 5 <= self.max_bus_duration <= 10 and self.budget >= 6800:
            return "Direct flight from Cochabamba to Japan $6800"
        return "No available options that match with your preferences."

def main():
    print("whats Up bro! We are travel solver. your best solution.")
    budget = float(input("Please enter your budget: $"))
    max_bus_duration = int(input("Please enter the maximum bus duration you can tolerate in hours: "))
    language_preference = input("Please enter your language pref13erence (spanish, english, or japanese). certanly thats doenst matter: ")

    solver = Travel_Solver(budget, max_bus_duration, language_preference)
    recommended_option = solver.select_best_option()
    print(f"The recommended travel option is: {recommended_option}")

main()
