# calculate_move_weights.py

from move_list import move_list_dict

# Define the weights for speed, utility, and special conditions
speed_weight = {
    "fast": 1.2,
    "normal": 1.0,
    "slow": 0.8
}

utility_weight = {
    "none": 1.0,
    "paralyze": 1.1,
    "burn": 1.05,
    "freeze": 1.15,
    "poison": 1.05,
    "sleep": 1.1
}

# Function to check for additional effects in the description
def check_additional_effects(description):
    if "to fall asleep" in description or "User sleeps" in description:
        return "sleep"
    if "sleeping opponent" in description:
        return "sleep_bonus"
    return "none"

# Function to update the move weights in the dictionary
def update_move_weights(move_dict):
    for move, details in move_dict.items():
        # Check for additional effects based on the description
        additional_effect = check_additional_effects(details.get("Description", ""))
        
        # Calculate the weight based on power, speed, utility, and additional effects
        power_score = details.get("Power", 0)  # Default to 0 if Power not found
        speed_score = speed_weight.get(details.get("Speed", "normal"), 1.0)
        utility_score = utility_weight.get(details.get("Utility", "none"), 1.0)
        
        # If there's a bonus for using the move against a sleeping opponent
        if additional_effect == "sleep_bonus" and "sleep" in move_dict:
            utility_score += 0.2  # Adding a bonus weight

        details["weight"] = power_score * speed_score * utility_score

# Update the weights in the move list dictionary
update_move_weights(move_list_dict)

# Print the updated move list dictionary with weights
for move, details in move_list_dict.items():
    print(f"{move}: {details}")

# Optionally, if you want to sort the moves by weight
sorted_moves = sorted(move_list_dict.items(), key=lambda x: x[1]['weight'], reverse=True)
print("\nSorted Moves by Weight:")
for move, details in sorted_moves:
    print(f"{move}: Weight = {details['weight']}")
