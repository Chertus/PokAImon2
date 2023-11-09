import time
from basic_ai import BasicAI  # Assuming you have a BasicAI class
from PyBoy import PyBoy

# Specify the ROM file name and path
rom_file = "PokemonRed.gb"

# Create a PyBoy instance
pyboy_instance = PyBoy(rom_file)

# Initialize AI
basic_ai = BasicAI()

# Ensure the emulator is running
while not pyboy_instance.tick():
    # Add debugging statement to check if emulator is running
    print("Emulator is running...")

# Main game loop
while True:
    # Check if the emulator is still running
    if not pyboy_instance.tick():
        # Add debugging statement to indicate emulator stopped
        print("Emulator stopped unexpectedly.")
        break
    
    # Your game logic here, including AI actions
    # ...

    # Example: AI action
    action = basic_ai.choose_action()
    # Execute the action using PyBoy API
    # ...

    # You can add more debugging statements as needed to track progress

    # Add a delay to control script execution speed (optional)
    time.sleep(0.1)

# Cleanup and exit
pyboy_instance.stop()
