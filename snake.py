import os
import random

# Snake Game
snake_position = [1, 1]
food_position = [random.randint(0, 9), random.randint(0, 9)]
score = 0

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(10):
        for j in range(10):
            if [i, j] == snake_position:
                print("S", end=' ')
            elif [i, j] == food_position:
                print("F", end=' ')
            else:
                print(".", end=' ')
        print()

while True:
    print_board()
    move = input("Move (WASD): ").lower()
    if move == 'w':
        snake_position[0] -= 1
    elif move == 's':
        snake_position[0] += 1
    elif move == 'a':
        snake_position[1] -= 1
    elif move == 'd':
        snake_position[1] += 1

    if snake_position == food_position:
        score += 1
        food_position = [random.randint(0, 9), random.randint(0, 9)]
    
    if snake_position[0] < 0 or snake_position[0] > 9 or snake_position[1] < 0 or snake_position[1] > 9:
        print("Game Over!")
        break
