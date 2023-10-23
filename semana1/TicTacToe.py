"""

modelo de cascada

1. Analisis

-crear juego basado en jugador 1 y jugador2
- tener el tablero de juego con logica ( 3 * 3 )

2. Diseño
- turnos especificados
- verificar patrones en ilera
- ganador en base al resultado de ileras. Caso contrario seria empate

3. Algoritmo

- tener logica de turnos predeterminada para los jugadores
- turnos repartidos entre 5 para el jugador 1 y 4 para el 2
- solo reviso un posible ganador cuando almenos en el tablero esten ubicadas 5 fichas, ni tampoco puede exeder el limite de 9  fichas
- aisgnar ganador en funcion al resultado obtenido
- volver a jugar?


implementacion 
"""

class Player:
    def __init__(self, name, Max_Token_Number):
        self.name = name
        self.Max_Token_Number = Max_Token_Number


    #necesitare  metodo para añadir ficha
"""  def add_token(self):
        self.token += 1
 """
class Token:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position

#tambien necesitare metodo para asignar pocision y obtener la posicion donde quiero poner la ficha
    def set_position(self, row, col):
         self.position = (row, col)

    def get_position(self):
            return self.position


class Dashboard:    
    def __init__(self, players, moves):        
        self.players = players
        self.moves = moves

        #tambien necesitare metodo de  recibir las fichas añadidas por el jugador. tambien establecer la posicion en el tablero de 3 * 3
        #encontrar a mi ganador 
        #asignarles el turno especifico 


    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player.token.symbol
            self.current_player.token.set_position(row, col)
            return True
        else:
            return False

