from typing import Set, Union, Optional
from flask import redirect, session
import functools
import hashlib

from serverLib import configs

def checkLogin(func):
    """
    The decorator for enforcing password-protected pages.
    """
    
    @functools.wraps(func)
    def decofunc(*args, **kwargs):
        if not session.get("admin", False):
            return redirect("/login")
        return func(*args, **kwargs)
    return decofunc

def checkAdmin(func):
    """
    The decorator for making sure logged in users don't try to log in again.s
    """
    
    @functools.wraps(func)
    def decofunc(*args, **kwargs):
        if session.get("admin", False):
            return redirect("/admin")
        return func(*args, **kwargs)
    return decofunc

SYMBOLS: str = "~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/"
upper: str = ''.join([chr(x + 97) for x in range(26)])
nums: str = ''.join([str(x) for x in range(10)])

def intersectionCheck(set1: Set[chr], set2: Union[Set[chr], str]) -> bool:
    """
    The function for finding if two sets have any identical values.

    Parameters:
        set1 (Set[chr]): One of the sets to compare.
        set2 (Union[Set[chr], str]): The other set to compare.

    Returns:
        bool: Whether the two sets share any values.
    """

    return not set1.intersection(set2)

def strength(pw: str) -> Optional[str]:
    """
    The function to verify a password's strength.

    Parameters:
        pw (str): The password to check.

    Returns:
        Optional[str]: A str on faliure, None on success.
    """

    pw_asSet: set[chr] = set(pw)
    if len(pw) < 8: return "Password needs at least 8 characters"
    if intersectionCheck(pw_asSet, upper): return "Password needs at least 1 uppercase letter"
    if intersectionCheck(pw_asSet, nums): return "Password needs at least 1 number"
    if intersectionCheck(pw_asSet, SYMBOLS): return "Password needs at least 1 symbol"
    return

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

    with open(f"{configs.DATA_FOLDER}/admin_hash.hash") as f:
        store: str = f.read()
    
    if hashlib.sha256(password.encode()).hexdigest() == store:
        return True
    
    return False

def update(new: str) -> Optional[str]:
    """
    The function to update the stored password hash.

    Parameters:
        new (str): The password to replace the old one with.

    Returns:
        Optional[str]: A str on faliure, None on success.
    """
    if not (msg := strength(new)) is None:
        return msg
    
    with open(f"{configs.DATA_FOLDER}/admin_hash.hash", "w") as f:
        f.write(hashlib.sha256(new.encode()).hexdigest())

    return