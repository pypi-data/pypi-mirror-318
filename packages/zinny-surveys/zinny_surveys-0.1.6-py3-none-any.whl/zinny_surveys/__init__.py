"""Convenience functions for working with surveya."""

from importlib import resources
import os
import json

# pylint: disable=line-too-long

def list_file_types():
    """
    Lists available file types.

    Returns:
        list: List of available file types.
    """
    base_path = resources.files("zinny_surveys").joinpath("data")
    return [file.name for file in base_path.iterdir() if file.is_dir()]


def list_scopes(file_type):
    """
    Lists available scopes for the specified file type.

    Args:
        file_type (str): 'surveys' or 'weights'.

    Returns:
        list: List of available scopes.
    """
    base_path = resources.files("zinny_surveys").joinpath("data").joinpath(file_type)
    print(base_path)
    return [file.name for file in base_path.iterdir() if file.is_dir()]


def list_files(file_type, scope):
    """
    Lists files in the specified scope and file_type.

    Args:
        file_type (str): 'surveys' or 'weights'.
        scope (str): 'shared' or 'local'.

    Returns:
        list: List of file paths relative to the file_type directory.
    """
    base_path = resources.files("zinny_surveys").joinpath("data").joinpath(file_type).joinpath(scope)
    if scope == "local":
        os.makedirs(base_path, exist_ok=True)  # Ensure local directories exist

    return [str(file.name) for file in base_path.iterdir() if file.is_file()]



def list_surveys(scope="shared"):
    """
    Lists surveys in the specified scope.

    Args:
        scope (str): 'shared' or 'local'.

    Returns:
        list: List of survey file names.
    """
    return list_files("surveys", scope)



def load_file(file_type, scope, file_name):
    """
    Loads a file's content.

    Args:
        file_type (str): 'surveys' or 'weights'.
        scope (str): 'shared' or 'local'.
        file_name (str): Name of the file to load.

    Returns:
        dict: Parsed JSON content.
    """
    base_path = resources.files("zinny_surveys").joinpath(f"data/{file_type}/{scope}")
    file_path = base_path.joinpath(file_name)
    print(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with file_path.open("r") as f:
        return json.load(f)


def load_survey(file_name, scope="shared"):
    """
    Loads a survey file.

    Args:
        file_name (str): Name of the survey file to load.

    Returns:
        dict: Parsed JSON content.
    """
    return load_file("surveys", scope, file_name)


def validate_survey_file(content):
    """
    Validate file content.

    Args:
        content (dict): Content to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Example: Check required keys
    required_keys = ["id", "name", "criteria"]
    return all(key in content for key in required_keys)


def save_file(file_type, file_name, content):
    """
    Saves content to a file in the local directory.

    Args:
        file_type (str): 'surveys' or 'weights'.
        file_name (str): Name of the file to save.
        content (dict): Content to save as JSON.

    Returns:
        str: Path to the saved file.
    """
    base_path = resources.files("zinny_surveys").joinpath(f"data/{file_type}/local")
    os.makedirs(base_path, exist_ok=True)

    file_path = base_path.joinpath(file_name)
    with file_path.open("w") as f:
        json.dump(content, f, indent=4)

    return str(file_path)


# def upload_to_contrib(file_type, file_name, content):
#     """
#     Upload a file to the contribution repository.

#     Args:
#         file_type (str): 'surveys' or 'weights'.
#         file_name (str): Name of the file.
#         content (dict): Content to upload.

#     Returns:
#         Response: Response from the server.
#     """

#     return f"Not Currently Implemented.\n{file_type}, {file_name}, {content}"  # Placeholder for testing
#     # import requests
#     # url = f"https://contrib.thezinny.com/{category}/{file_name}"
#     # response = requests.post(url, json=content)
#     # response.raise_for_status()
#     # return response
