from ...forall import *
import importlib.resources as pkg_resources
from PIL import Image
import IPython.display as display

THEORY = []

def get_png_files_from_subdir(subdir):
    """
    Returns a list of file paths to PNG files in the given subdirectory.
    """
    package = f"matplobblib.tvims.theory.pdfs.{subdir}"
    png_files = []
    try:
        for resource in pkg_resources.contents(package):
            if resource.endswith(".png"):
                with pkg_resources.path(package, resource) as file_path:
                    png_files.append(file_path)
    except Exception as e:
        print(f"Error accessing PNG files in {subdir}: {e}")
    return png_files

def display_png_files_from_subdir(subdir):
    """
    Displays PNG files from a given subdirectory in the Jupyter notebook.
    """
    png_files = get_png_files_from_subdir(subdir)
    for file in png_files:
        img = Image.open(file)
        display.display(img)

# Dynamically create functions for each subdirectory
def create_subdir_function(subdir):
    """
    Dynamically creates a function to display PNG files from a given subdirectory.
    The function is named display_png_files_{subdir}.
    """
    global THEORY
    # Define the function dynamically
    def display_function():
        """
        Automatically generated function to display PNG files.
        """
        display_png_files_from_subdir(subdir)
    
    # Set the function name dynamically
    display_function.__name__ = f"display_png_files_{subdir}"
    
    # Add a descriptive docstring
    display_function.__doc__ = (
        f"Display all PNG files from the '{subdir}' subdirectory in the Jupyter notebook.\n\n"
        f"This function is dynamically generated to work with the subdirectory '{subdir}' "
        f"inside the 'pdfs' directory of the library.\n\n"
        f"Example:\n"
        f"    >>> {display_function.__name__}()\n"
        f"Args"
    )
    
    # Add the function to the global namespace
    globals()[display_function.__name__] = display_function
    THEORY.append(display_function)
    print(f"Function {display_function.__name__} added to list.")  # Debug print

def list_subdirectories():
    """
    List subdirectories in the 'matplobblib.tvims.theory.pdfs' package.
    """
    package = "matplobblib.tvims.theory.pdfs"
    subdirs = []
    
    # List all items in the package
    for item in pkg_resources.resource_listdir(package, ''):
        # Check if the item is a directory
        item_path = f"{package}/{item}"
        if pkg_resources.resource_isdir(item_path):
            subdirs.append(item)
    
    return subdirs

# Get subdirectories dynamically
subdirs = list_subdirectories()
print(subdirs)

# Create functions for each subdirectory dynamically
for subdir in subdirs:
    create_subdir_function(subdir)

# Check the list content
print("Functions in list:", [func.__name__ for func in THEORY])