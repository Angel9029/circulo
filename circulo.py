import math

"""
Construcctor del objeto Circulo
"""


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def circunferencia(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * self.radio ** 2


if __name__ == "__main__":
    instancia_circulo = Circulo(10)
    print(f"La circunferencia es: {instancia_circulo.circunferencia()}")
    print(f"El area es: {instancia_circulo.area()}")