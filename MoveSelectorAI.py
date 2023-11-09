class PokemonType:
    # Define effectiveness of types against each other
    effectiveness_chart = {
        # Example: "Fire": {"Grass": 2.0, "Water": 0.5, ...}
    }

    @staticmethod
    def calculate_effectiveness(move_type, opponent_type):
        return PokemonType.effectiveness_chart.get(move_type, {}).get(opponent_type, 1)

class Move:
    # Existing definition

class BattleAI:
    # Existing definition

    def calculate_type_advantage(self, move, opponent_type):
        return PokemonType.calculate_effectiveness(move.move_type, opponent_type)

    def evaluate_move(self, move, opponent_type, current_status):
        score = 0
        type_advantage = self.calculate_type_advantage(move, opponent_type)
        # Add logic to calculate move score based on power, accuracy, type advantage, and status effects
        return score * type_advantage  # Example scoring

    # Existing select_move method

# Example usage
move_list = [Move("Thunderbolt", "Electric", 90, 100, None), ...]  # Populate with actual moves
battle_ai = BattleAI(move_list)
selected_move = battle_ai.select_move(available_moves, opponent_pokemon_type, current_status)
