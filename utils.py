import os

def ensure_directory_exists(directory):
    """Ensure that a directory exists. If it doesn't, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
