import os

def create_directories():
    directories = ["sessions", "logs", "JSON", "TrainingData"]
    for dir in directories:
        os.makedirs(dir, exist_ok=True)

def save_session_data(session_id, data):
    session_path = f"sessions/session_{session_id}.dat"  # Adjust format as needed
    with open(session_path, 'w') as file:
        file.write(data)

def save_log(log_data):
    log_path = "logs/logfile.log"  # Adjust naming as needed
    with open(log_path, 'a') as file:
        file.write(log_data + '\n')

def save_json(session_id, json_data):
    json_path = f"JSON/session_{session_id}.json"
    with open(json_path, 'w') as file:
        file.write(json_data)

def save_training_data(data):
    training_data_path = "TrainingData/training_data.db"  # Adjust format as needed
    # Code to save data to the database

# Initialize directories at the start of the program
create_directories()

# Example usage
# save_session_data("01aee661", "Session data here")
# save_log("Log entry")
# save_json("01aee661", '{"key": "value"}')
# save_training_data("Processed training data")
