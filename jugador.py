import math
import random

class Jugador():
    def __init__(self, juego):
        self.juego = juego

    def hacer_movimiento(self, juego):
        pass

class JugadorHumano(Jugador):
    def __init__(self, juego):
        super().__init__(juego)

    def hacer_movimiento(self, juego):
        cuadrado_valido = False
        val = None
        while not cuadrado_valido:
            cuadrado = input(self.juego + ' Juega ahora. Posiciones del tablero (0-8): ')
            try:
                val = int(cuadrado)
                if val not in juego.movimientos_disponibles():
                    raise ValueError
                cuadrado_valido = True
            except ValueError:
                print('Cuadrado inválido, elige otro.')
        return val

class JugadorComputadorAi(Jugador):
    def __init__(self, juego):
        super().__init__(juego)

    def hacer_movimiento(self, juego):
        if len(juego.movimientos_disponibles()) == 9:
            cuadrado = random.choice(juego.movimientos_disponibles())
        else:
            cuadrado = self.minimax(juego, self.juego)['posición']
        return cuadrado

    def minimax(self, estado, Jugador):
        max_Jugador = self.juego
        otro_Jugador = 'O' if Jugador == 'X' else 'X'

        if estado.ganador_actual == otro_Jugador:
            return {'posición': None, 'puntaje': 1 * (estado.num_cuadrados_vacios() + 1) if otro_Jugador == max_Jugador else -1 * (
                        estado.num_cuadrados_vacios() + 1)}
        elif not estado.cuadrados_vacios():
            return {'posición': None, 'puntaje': 0}

        if Jugador == max_Jugador:
            mejor = {'posición': None, 'puntaje': -math.inf}
        else:
            mejor = {'posición': None, 'puntaje': math.inf}
        for posible_movimiento in estado.movimientos_disponibles():
            estado.hacer_movimiento(posible_movimiento, Jugador)
            sim_puntaje = self.minimax(estado, otro_Jugador)

            estado.tablero[posible_movimiento] = ' '
            estado.ganador_actual = None
            sim_puntaje['posición'] = posible_movimiento

            if Jugador == max_Jugador:
                if sim_puntaje['puntaje'] > mejor['puntaje']:
                    mejor = sim_puntaje
            else:
                if sim_puntaje['puntaje'] < mejor['puntaje']:
                    mejor = sim_puntaje
        return mejor




