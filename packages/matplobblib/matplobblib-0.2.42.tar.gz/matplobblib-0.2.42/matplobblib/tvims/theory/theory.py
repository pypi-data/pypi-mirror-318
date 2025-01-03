from ...forall import *
import importlib.resources as pkg_resources
from PIL import Image
import IPython.display as display

def get_png_files():
    """
    Returns a list of file paths to PNG files in the MS-11-12 directory
    and displays them in a Jupyter notebook.
    """
    package = "matplobblib.tvims.theory.pdfs.MS-11-12"
    png_files = []
    try:
        for resource in pkg_resources.contents(package):
            if resource.endswith(".png"):
                with pkg_resources.path(package, resource) as file_path:
                    png_files.append(file_path)
    except Exception as e:
        print(f"Error accessing PNG files: {e}")
    return png_files

def display_png_files():
    """
    Displays PNG files in the MS-11-12 directory in a Jupyter notebook.
    """
    png_files = get_png_files()
    for file in png_files:
        img = Image.open(file)
        display.display(img)