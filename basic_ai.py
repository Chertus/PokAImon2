import random
from move_list import move_list  # Assuming move_list.py contains a dictionary named move_list
from calculate_move_weights import calculate_move_weight  # Assuming calculate_move_weights.py contains this function

class BasicAI:
    def __init__(self):
        # Initialize AI components
        self.actions = ["move1", "move2", "move3", "move4", "run", "item", "switch_pokemon"]

    def choose_action(self, state):
        # Decide on an action based on the current state
        if self.should_switch_pokemon(state):
            return "switch_pokemon"
        
        effective_moves = self.filter_effective_moves(state)
        if effective_moves:
            return random.choice(effective_moves)
        else:
            return random.choice(self.actions)

    def filter_effective_moves(self, state):
        # Filter moves based on their effectiveness and other factors
        effective_moves = []
        player_pokemon = state['player_pokemon']
        opponent_pokemon = state['opponent_pokemon']

        for move in player_pokemon['moves']:
            if move in move_list:
                move_data = move_list[move]
                move_weight = calculate_move_weight(move_data, opponent_pokemon)
                if move_weight > 0:  # Assuming a positive weight indicates effectiveness
                    effective_moves.append(move)
        return effective_moves

    def should_switch_pokemon(self, state):
        # Determine if the player should switch Pokémon
        # Placeholder for switch logic based on status, abilities, etc.
        return False

# Example usage
if __name__ == "__main__":
    # Example game state (should be replaced with actual data)
    current_state = {
        "player_pokemon": {
            "name": "Pikachu",
            "moves": ["Thunderbolt", "Quick Attack"],
            # ... other stats
        },
        "opponent_pokemon": {
            "name": "Squirtle",
            # ... other stats
        }
    }

    ai = BasicAI()
    action = ai.choose_action(current_state)
    print(f"Chosen action: {action}")

