class DatabaseConnection:
    def __init__(self):
        print("Database connection established.")
    
    def __del__(self):
        print("Database connection closed.")