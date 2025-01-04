
#########################################
# IMPORT SoftwareAI Libs 
from softwareai.CoreApp._init_libs_ import *
#########################################

def autosave(code, name_script):
    """
    Save the provided Python code string to a file.

    Parameters:
    ----------
    code_string (str): The Python code to save.
    name_script (str): The name of the file where the code will be saved.

    Returns:
    -------
    None
    """
    with open(name_script, 'w', encoding="utf-8") as file:
        file.write(code)