import numpy as np
import math
import random
import time
import pygame
import sys
#Constants

blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

row_count = 6
column_count = 7

square_size = 100
width = column_count * square_size
height = (row_count + 1) * square_size 
size = (width, height)
radius = int(square_size/2 - 5)

node_count = 0


#Core Board Logic
def create_board():
    board = np.zeros((row_count,column_count))
    return board

def is_valid_column(board,col):
    return board[row_count-1][col] == 0

def get_next_open_row(board,col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r
    
def drop_piece(board,row,col,piece):
    board[row][col] = piece

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board,piece):
    #Horizontal 
    for c in range(column_count - 3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #Vertical
    for c in range(column_count):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #Positive Diagonal
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #Negative Diagonal
    for c in range(column_count - 3):
        for r in range(3,row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


 #Scoring & Heuristics
            
def evaluate_window(window,piece):
    score = 0

    enemy_piece = 1
    if piece == 1:
        enemy_piece = 2
    
    if window.count(piece) == 4:
        score += 1000
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2   
    if window.count(enemy_piece) == 3 and window.count(0) == 1:
        score -= 10
    
    return score

def score_position(board,piece):
    score = 0
    center_col = 3
    for r in range(row_count):
        if board[r][center_col] == piece:
            score += 3

    #Horizontal Check
    for c in range(column_count - 3):
        for r in range(row_count):
            window = [board[r][c], board[r][c+1], board[r][c+2], board[r][c+3]]
            score += evaluate_window(window, piece)
    #Vertical Check
    for c in range(column_count):
        for r in range(row_count - 3):
            window = [board[r][c], board[r+1][c], board[r+2][c], board[r+3][c]]
            score += evaluate_window(window, piece)
    #Positive Diagonal Check
    for c in range(column_count - 3):
        for r in range(row_count - 3):
            window = [board[r][c], board[r+1][c+1], board[r+2][c+2], board[r+3][c+3]]
            score += evaluate_window(window, piece)
    #Negative Diagonal Check
    for c in range(column_count - 3):
        for r in range(3,row_count):
            window = [board[r][c], board[r-1][c+1], board[r-2][c+2], board[r-3][c+3]]
            score += evaluate_window(window, piece)
    return score


#AI - Minimax Algorithm
def get_valid_column(board):
    valid_column = []
    for col in range(column_count):
        if is_valid_column(board, col):
            valid_column.append(col)
    return valid_column

def terminal_state(board):
    return winning_move(board,1) or winning_move(board,2) or len(get_valid_column(board)) == 0 

def minimax(board,depth,alpha,beta,maximizingPlayer):

    global node_count
    node_count +=1

    valid_column = get_valid_column(board)
    is_terminal = terminal_state(board)
   
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board,2):
                return (None,1000000)
            if winning_move(board,1):
                return (None,-1000000)
            else:
                return (None,0)
        else:
            return (None,score_position(board,2))
    if maximizingPlayer:    #AIprint 
        value = -math.inf
        column = random.choice(valid_column)

        for col in valid_column:    
            row = get_next_open_row(board,col)
            board_copy = board.copy()
            drop_piece(board_copy,row,col,2)

            new_score = minimax(board_copy,depth-1,alpha,beta,False)[1]

            if new_score > value:
                value = new_score
                column = col

            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return column, value

    else:               #Player
        value = math.inf
        column = random.choice(valid_column)

        for col in valid_column:
            row = get_next_open_row(board,col)
            board_copy = board.copy()
            drop_piece(board_copy,row,col,1)

            new_score = minimax(board_copy,depth-1,alpha,beta,True)[1]

            if new_score < value:
                value = new_score
                column = col

            beta = min(beta, value)
            if alpha >= beta:
                break

        return column, value

#GUI & Main Game Loop
def draw_board(board):
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c*square_size, r*square_size+square_size, square_size, square_size))
            pygame.draw.circle(screen, black, (int(c*square_size+square_size/2), int(r*square_size+square_size+square_size/2)), radius)
    
    for c in range(column_count):
        for r in range(row_count):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), radius)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, yellow, (int(c*square_size+square_size/2), height-int(r*square_size+square_size/2)), radius)
    pygame.display.update()

#starting the game 
while True:
    try:
        Ai_depth = int(input("Enter AI Search Depth (1-6): "))
        if 1 <= Ai_depth <= 6:
            break
        else:
            print("Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Numbers only.")

game_start_time = time.time()
total_ai_think_time = 0
total_ai_nodes = 0

board = create_board()
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4 AI")
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 50)
game_over = False
turn = 0


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0,0, width, square_size))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red, (posx, int(square_size/2)), radius)
            pygame.display.update()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0,0, width, square_size))
            
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/square_size))
                
                if is_valid_column(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    
                    if winning_move(board, 1):
                        label = myfont.render("You Won!", 1, red)
                        screen.blit(label, (40,10))
                        game_over = True
                        
                    turn += 1
                    turn = turn % 2
                    draw_board(board)
    
    if turn == 1 and not game_over:
        pygame.draw.rect(screen, black, (0,0, width, square_size))
        label = myfont.render("AI is thinking...", 1, yellow)
        screen.blit(label, (40,10))
        pygame.display.update()
        
        node_count = 0 
        
        start_time = time.time()                                                                                                                               
        col, minimax_score = minimax(board, Ai_depth, -math.inf, math.inf, True)
        end_time = time.time()
        
        time_taken = round((end_time - start_time) * 1000)
        
        total_ai_think_time += time_taken
        total_ai_nodes += node_count
        
        print(f"AI chose column: {col} | Nodes evaluated: {node_count} | Time taken: {time_taken} ms")
        
        if is_valid_column(board, col):
            pygame.time.wait(500) 
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            
            if winning_move(board, 2):
                pygame.draw.rect(screen, black, (0,0, width, square_size))
                label = myfont.render("AI won!", 1, yellow)
                screen.blit(label, (40,10))
                game_over = True
                
            draw_board(board)
            turn += 1
            turn = turn % 2

    if game_over:
        print("\n===================================")
        print("Game Summary: ")
        print("===================================\n")

        if winning_move(board, 1):
            print("Player 1 won!")
        elif winning_move(board, 2):
            print("AI won!")
        else:
            print("draw")
        print("\n")

        total_moves = np.count_nonzero(board)
        game_duration = round(time.time() - game_start_time, 2)

        print(f"Total Game Duration: {game_duration} seconds")
        print(f"Total Moves Played: {total_moves} moves")
        print(f"Total AI Nodes Evaluated: {total_ai_nodes} nodes")
        print(f"Total AI Think Time: {round(total_ai_think_time / 1000, 2)} seconds \n")

        pygame.time.wait(3000)
        sys.exit()