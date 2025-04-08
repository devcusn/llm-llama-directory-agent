import os


def create_directory(path):
    """
    Create a directory if it does not exist.

    Args:
        path (str): The path to the directory to create.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created.")
    else:
        print(f"Directory {path} already exists.")


def delete_directory(path):
    """
    Delete a directory if it exists.

    Args:
        path (str): The path to the directory to delete.
    """
    if os.path.exists(path):
        os.rmdir(path)
        print(f"Directory {path} deleted.")
    else:
        print(f"Directory {path} does not exist.")


def list_directories(path):
    """
    List all directories in the given path.

    Args:
        path (str): The path to list directories from.
    """
    if os.path.exists(path):
        directories = [d for d in os.listdir(
            path) if os.path.isdir(os.path.join(path, d))]
        print(f"Directories in {path}: {directories}")
    else:
        print(f"Path {path} does not exist.")


def rename_directory(old_path, new_path):
    """
    Rename a directory.

    Args:
        old_path (str): The current path of the directory.
        new_path (str): The new path for the directory.
    """
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Directory renamed from {old_path} to {new_path}.")
    else:
        print(f"Directory {old_path} does not exist.")


if __name__ == "__main__":
    create_directory("example_dir")
    create_directory("example_dir/subdir")
    create_directory("example_dir/subdir")
