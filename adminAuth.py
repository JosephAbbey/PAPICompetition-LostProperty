from typing import Set, Union
from serverLib import serverLib
import hashlib

# DECORATOR HERE

SYMBOLS: str = "~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/"
upper: str = ''.join([chr(x + 97) for x in range(26)])
nums: str = ''.join([str(x) for x in range(10)])

def intersectionCheck(pwSet: Set[chr], check: Union[Set[chr], str]) -> bool:
    return not pwSet.intersection(check)

def strength(pw: str) -> Union[bool, str]:
    pw_asSet = set(pw)
    if len(pw) < 8: return "Password needs at least 8 characters"
    if intersectionCheck(pw_asSet, upper): return "Password needs at least 1 uppercase letter"
    if intersectionCheck(pw_asSet, nums): return "Password needs at least 1 number"
    if intersectionCheck(pw_asSet, SYMBOLS): return "Password needs at least 1 symbol"
    return True

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

    with open(f"{serverLib.configs.DATA_FOLDER}/admin_hash.hash") as f:
        store: str = f.read()
    
    if hashlib.sha256(password).hexdigest() == store:
        return True
    
    return False

def update(new: str) -> Union[bool, str]:
    """
    The function to update the stored password hash.

    Parameters:
        new (str): The password to replace the old one with.

    Returns:
        bool: True if password was valid.
    """
    if not (msg := strength(new)):
        return msg
    
    with open(f"{serverLib.configs.DATA_FOLDER}/admin_hash.hash", "w") as f:
        f.write(hashlib.sha256(new).hexdigest())

    return True