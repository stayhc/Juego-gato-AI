import math
import time
from jugador import JugadorHumano, JugadorComputadorAi

class gato():
    def __init__(self):
        self.tablero = self.crear_tablero()
        self.ganador_actual = None

    @staticmethod
    def crear_tablero():
        return [' ' for _ in range(9)]

    def print_tablero(self):
        for fila in [self.tablero[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(fila) + ' |')

    @staticmethod
    def print_tablero_nums():
        # 0 | 1 | 2
        numero_tablero = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for fila in numero_tablero:
            print('| ' + ' | '.join(fila) + ' |')

    def hacer_movimiento(self, cuadrado, letra):
        if self.tablero[cuadrado] == ' ':
            self.tablero[cuadrado] = letra
            if self.ganador(cuadrado, letra):
                self.ganador_actual = letra
            return True
        return False

    def ganador(self, cuadrado, letra):
        # revisa la fila
        fila_ind = math.floor(cuadrado / 3)
        fila = self.tablero[fila_ind*3:(fila_ind+1)*3]
        # print('fila', fila)
        if all([s == letra for s in fila]):
            return True
        col_ind = cuadrado % 3
        columna = [self.tablero[col_ind+i*3] for i in range(3)]
        # print('col', columna)
        if all([s == letra for s in columna]):
            return True
        if cuadrado % 2 == 0:
            diagonal1 = [self.tablero[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letra for s in diagonal1]):
                return True
            diagonal2 = [self.tablero[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letra for s in diagonal2]):
                return True
        return False

    def cuadrados_vacios(self):
        return ' ' in self.tablero

    def num_cuadrados_vacios(self):
        return self.tablero.count(' ')

    def movimientos_disponibles(self):
        return [i for i, x in enumerate(self.tablero) if x == " "]


def jugar(juego, jugador_x, jugador_o, print_juego=True):

    if print_juego:
        juego.print_tablero_nums()

    letra = 'X'
    while juego.cuadrados_vacios():
        if letra == 'O':
            cuadrado = jugador_o.hacer_movimiento(juego)
        else:
            cuadrado = jugador_x.hacer_movimiento(juego)
        if juego.hacer_movimiento(cuadrado, letra):

            if print_juego:
                print(letra + ' realiza un movimiento a la posición {} del juego'.format(cuadrado))
                juego.print_tablero()
                print('')

            if juego.ganador_actual:
                if print_juego:
                    print(letra + ' Ha ganado!')
                return letra  # sale del ciclo y termina el juego
            letra = 'O' if letra == 'X' else 'X'  # cambia de jugador

        time.sleep(.8)

    if print_juego:
        print('Es un empate, bien jugado.')

if __name__ == '__main__':
    jugador_x = JugadorComputadorAi('X')
    jugador_o = JugadorHumano('O')
    t = gato()
    jugar(t, jugador_x, jugador_o, print_juego=True)

