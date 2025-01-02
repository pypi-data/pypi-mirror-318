import string

# Farhan Ali <i.farhanali.dev@gmail.com>

ALLOWED_CHARS = string.ascii_letters + string.digits + "-_.~"

def urlencode(string: str) -> str:
    """
    Encodes a string into a URL-safe format.
    """
    return ''.join(
        c if c in ALLOWED_CHARS else f"%{ord(c):02X}"
        for c in string
    )

def urldecode(string: str) -> str:
    """
    Decodes a URL-encoded string.
    """
    result = []
    i = 0

    while i < len(string):
        if string[i] == '%':
            try:
                result.append(chr(int(string[i+1:i+3], 16)))
                i += 3
            except (ValueError, IndexError):
                raise ValueError(f"Invalid encoding at position {i}: {string[i:i+3]}")
        else:
            result.append(string[i])
            i += 1
    
    return ''.join(result)
