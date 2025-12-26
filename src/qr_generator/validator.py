# src/qr_generator/validator.py

from typing import Tuple 

Max_Qr_Byte= 2953



def validate_data(data:str)->Tuple[bool,str]:
    """
   Validates the data before the QR code is generated.

   Args:
     data:(str): Data to encode in the QR

  Returns:
    Tuple[bool,string]:[isvalid, error-message] 
    """
    if not isinstance(data,str):
        return False,"Input data must be a string"
    
    if not data.strip():
        return False,"Input data cannot e empty"
    
    byte_length=len(data.encode("utf-8"))
    if byte_length>Max_Qr_Byte:
        return False, f"The input data exceeds the QR code size limit{Max_Qr_Byte} bytes"
    
    return True,""