class Player:
    def __init__(self, name, token):
            self.name = name
            self.token = token

class Dashboard:
    def __init__(self):
         self.cell_list = self.create_cells()  
         
    def play(self, jugador1, jugador2):
        self.make_movement(jugador1)
        self.make_movement(jugador2)
     
           

    def make_movement (self, jugador):    
            self.draw_board()
            move_player= self.get_player_move()
            selected_cell = self.get_cell(move_player)
            if(selected_cell.token == "" ):
                token = jugador.token
                selected_cell.token = token  
            else:
                 raise ValueError("posicion invalida")    

    def create_cells(self):
        return [Cell(i) for i in range(9)]  



    def draw_board(self):
        for i in range(3):
            row = [self.cell_list[i * 3 + j].token if self.cell_list[i * 3 + j].token else " " for j in range(3)]
            print(" | ".join(row))
            if i < 2:
                print("-" * 9)  


    def get_player_move(self):
            while True:
                try:
                    move = int(input("Bienvenido. Elige una celdacha de (0-8): "))
                    if 0 <= move <= 8:
                        break
                    else:
                        print("Movimiento incorrecto debe seleccionar una celda de 0 a 8.")
                except ValueError:
                    print("valor no encontrado que sea uno de 0 a 8 porfa")
            return move

     

class Cell:
    def __init__(self, position):
            self.position = position
            self.token= ""            
class Token:
    def __init__(self, symbol):
        self.symbol = symbol
