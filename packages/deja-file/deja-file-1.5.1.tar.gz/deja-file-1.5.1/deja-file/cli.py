import os
import hashlib
import sys

def calculate_md5(filepath):
    """
    Calculate the MD5 hash of a file.
    
    Args:
        filepath (str): Path to the file.
        
    Returns:
        str: MD5 hash of the file or an empty string if an error occurs.
    """
    try:
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return ""


def find_duplicates(directory):
    """
    Find duplicate files in the specified directory using MD5 hashes.

    Args:
        directory (str): The directory to scan for duplicates.
        
    Returns:
        dict: A dictionary where keys are MD5 hashes and values are lists of file paths with the same hash.
    """
    hash_map = {}

    # Walk through the directory and hash each file
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)

            if file_hash:
                if file_hash in hash_map:
                    hash_map[file_hash].append(file_path)
                else:
                    hash_map[file_hash] = [file_path]

    return hash_map


def delete_files(files):
    """
    Delete files except the first one in a duplicate group.
    
    Args:
        files (list): A list of file paths that are duplicates.
    """
    for file_path in files[1:]:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m deja-file <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    print(f"Scanning directory: {directory}")

    # Find duplicates
    hash_map = find_duplicates(directory)

    duplicates_found = False

    # Check for duplicates
    for file_hash, file_paths in hash_map.items():
        if len(file_paths) > 1:
            duplicates_found = True
            print(f"\nDuplicate files found (MD5: {file_hash}):")
            for i, file_path in enumerate(file_paths, 1):
                print(f"  {i}. {file_path}")

            choice = input("Do you want to delete all except the first file? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                delete_files(file_paths)

    if not duplicates_found:
        print("No duplicate files found.")
