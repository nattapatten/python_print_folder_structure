import os
import fnmatch

def load_gitignore(path):
    gitignore_path = os.path.join(path, '.gitignore')
    ignore_patterns = []
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r') as file:
            ignore_patterns = [line.strip() for line in file if line.strip() and not line.startswith('#')]
    return ignore_patterns

def is_ignored(path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False

def print_directory_tree(path, ignore_patterns, prefix=""):
    # Check if the path exists
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    # Get a sorted list of all items in the directory
    items = sorted(os.listdir(path))
    
    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        if is_ignored(item_path, ignore_patterns):
            continue

        is_last_item = index == len(items) - 1
        
        # Print the current item
        if os.path.isdir(item_path):
            print(f"{prefix}├── {item}/")
            # Recursively print the sub-directory with an updated prefix
            new_prefix = f"{prefix}│   " if not is_last_item else f"{prefix}    "
            print_directory_tree(item_path, ignore_patterns, new_prefix)
        else:
            print(f"{prefix}├── {item}")

if __name__ == "__main__":
    # Input the path you want to print
    directory_path = input("Enter the path of the directory you want to print: ")
    ignore_patterns = load_gitignore(directory_path)
    print(f"{os.path.basename(directory_path)}/")
    print_directory_tree(directory_path, ignore_patterns)
