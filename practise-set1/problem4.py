import os

# Function for printing the content of a Directory

def print_directory_contents(path):
    try:
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")

# Example usage
directory_path = input("Enter the directory path: ")
print_directory_contents(directory_path)