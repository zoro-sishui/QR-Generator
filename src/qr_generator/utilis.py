import os
import re


def sanitize_filename(filename:str)->str:
    """
    Removes the special character from the filename 
    """
    filename=filename.strip().lower()
    filename = re.sub(r"[^a-z0-9_\-\.]", "_", filename)
    return filename 

def ensurepngextension(filename:str)->str:
    """ 
    ensures that the file name contains the extension .png 
    """
    if not filename.endswith(".png"):
        return(f"{filename}.png")
    return filename

def prepare_outputpath(filename:str)->str:
    """
    sanitize the filename and join it with output directory

    """
    safe_name=sanitize_filename(filename)
    safe_name=ensurepngextension(safe_name)
    return os.path.join(os.getcwd(),safe_name)
