from serverLib import serverLib
import hashlib

# DECORATOR HERE

def login(password: str) -> bool:
    """
    The function to verify if the supplied password is the stored admin password.

    Parameters:
        password (str): The supplied password.

    Returns:
        bool: True if password is correct.
    """

    if len(password.strip()) == 0:
        return False

    with open(f"{serverLib.config.DATA_FOLDER}/admin_hash.hash") as f:
        store: str = f.read()
    
    if hashlib.sha256(password).hexdigest() == store:
        return True
    
    return False

def update(new: str) -> bool:
    """
    The function to update the stored password hash.

    Parameters:
        new (str): The password to replace the old one with.

    Returns:
        bool: True if password was valid.
    """

    if len(new.strip()) == 0:
        return False

    