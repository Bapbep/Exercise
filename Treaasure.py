import random

# Define the size of the grid
grid_size = 5

# Assign the player and treasure a random position on the grid
player_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

# Decide the maximum moves the player can make
max_moves = 10

# Calculate the initial distance between the player and the treasure location
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

initial_distance = calculate_distance(player_position, treasure_position)
print(f"Initial distance to the treasure: {initial_distance}")

# Allow player to make as many moves as maximum moves allowed
moves_count = 0
found_treasure = False

while moves_count < max_moves and not found_treasure:
    print(f"Your current position: {player_position}")
    move = input("Enter your move (N, S, E, W): ").upper()
    
    if move == 'N':
        player_position[1] += 1
    elif move == 'S':
        player_position[1] -= 1
    elif move == 'E':
        player_position[0] += 1
    elif move == 'W':
        player_position[0] -= 1
    else: 
       print("Illegal move. Please enter N, S, E, or W.")
        
    

    # Check for boundaries
    if player_position[0] < 0 or player_position[0] >= grid_size or player_position[1] < 0 or player_position[1] >= grid_size:
        print("Move not allowed. You cannot move outside the grid.")
        player_position[0] -= 1 if move == 'E' else 0
        player_position[1] -= 1 if move == 'N' else 0
        continue

    moves_count += 1
    current_distance = calculate_distance(player_position, treasure_position)
    
    if current_distance < initial_distance:
        print("You are getting closer to the treasure!")
    elif current_distance > initial_distance:
        print("You are moving farther from the treasure!")
    
    if player_position == treasure_position:
        found_treasure = True
        print("Congratulations! You've found the treasure!")
    else:
        print(f"Moves left: {max_moves - moves_count}")
        if moves_count == max_moves:
            print(f"No more moves. You've lost the game. The treasure was at {treasure_position}.")

# If the game ends without finding the treasure, show the treasure's location
if not found_treasure:
    print(f"The treasure was at {treasure_position}.")