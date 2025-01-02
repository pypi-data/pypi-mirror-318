import re
from . import utils

# Farhan Ali <i.farhanali.dev@gmail.com>

def parse(cookies: str, delimiter: str = ";") -> dict[str, str]:
    """
    Parses a cookie string and returns a dictionary of cookies.
    
    Parameters:
    cookies (str): The cookie string to parse.
    delimiter (str): The delimiter separating key-value pairs (default: ';').
    
    Returns:
    dict[str, str]: A dictionary of parsed cookies.
    """
    cookies = cookies.strip(delimiter)
    matches = re.findall(fr"\s*(.*?)=(.*?){delimiter}\s*", cookies)
    
    parsed: dict[str, str] = {}
    if not matches:
        return parsed
    
    for match in matches:
        if len(match) == 2:
            parsed[match[0].strip()] = utils.urldecode(match[1].strip())
    
    return parsed


def encode(cookies: dict[str, str]) -> str:
    """
    Encodes a dictionary of cookies into a cookie string format.
    
    Parameters:
    cookies (dict[str, str]): The dictionary of cookies to encode.
    
    Returns:
    str: The encoded cookie string.
    """
    encoded = [f"{name}={utils.urlencode(value)}" for name, value in cookies.items()]
    return "; ".join(encoded)

def get_cookie(cookie: str, name: str, delimiter: str=";") -> str | None:
    return parse(cookie, delimiter).get(name)