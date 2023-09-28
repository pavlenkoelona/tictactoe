# Definir el tablero del juego
board = [" " for _ in range(9)]

# Función para imprimir el tablero
def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")

# Función para verificar si alguien ha ganado
def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Función principal del juego
def main():
    current_player = "X"
    while True:
        print_board()
        position = int(input(f"Jugador {current_player}, elige una posición (1-9): ")) - 1

        if board[position] == " ":
            board[position] = current_player
            if check_winner(current_player):
                print_board()
                print(f"¡Jugador {current_player} ha ganado!")
                break
            elif " " not in board:
                print_board()
                print("¡Empate!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Esa posición ya está ocupada. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

