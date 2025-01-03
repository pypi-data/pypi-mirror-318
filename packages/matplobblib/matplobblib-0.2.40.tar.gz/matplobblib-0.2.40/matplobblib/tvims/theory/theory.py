from ...forall import *
import importlib.resources as pkg_resources


def get_png(file_name):
    """
    Fetch a PNG file from the embedded 'pdfs' directory.

    :param file_name: Name of the PNG file to fetch (e.g., 'file1.png').
    :return: The full path to the PNG file.
    """
    try:
        with pkg_resources.path(__package__, f"pdfs/{file_name}") as path:
            return str(path)
    except FileNotFoundError:
        raise ValueError(f"File {file_name} does not exist in the 'pdfs' directory.")

show_img(get_png('page_1.png'))