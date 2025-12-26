import qrcode 
from  qrcode.constants import ERROR_CORRECT_L



def generate_qr(data:str,output_path:str)->bool:
    """
    generate the qr code from the given data and saves it as an image.
    
    Args: 
    data(str): The data to encode in the QR code.
    output_path: The path where the qr image will be saved 
    
    Returns:
    bool: True if the image as generate successfully else return false
    """
    try:
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white") 
        img.save(output_path)

        return True
    except Exception:
        return False