
#########################################
# IMPORT SoftwareAI Libs 
from softwareai.CoreApp._init_libs_ import *
#########################################

def execute_py(filepath):
    """
    Execute the Python code stored in the specified file.

    Parameters:
    ----------
    filename (str): The name of the Python file to execute.

    Returns:
    -------
    str: The standard output of the executed script.
    """
    try:
        result = subprocess.run(['python', filepath], capture_output=True, text=True, check=True)
        return f"Saída padrão: {result.stdout.strip()}" if result.stdout else "Execução concluída sem saída."
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar o código:\n{e.stderr.strip()}"
    except FileNotFoundError:
        return f"Erro: O arquivo '{filepath}' não foi encontrado."
    except Exception as e:
        return f"Erro inesperado: {str(e)}"
