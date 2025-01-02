# cookiesparser

[![GitHub](https://img.shields.io/github/license/farhaanaliii/cookiesparser)](https://github.com/farhaanaliii/cookiesparser/blob/main/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/farhaanaliii/cookiesparser)](https://github.com/farhaanaliii/cookiesparser/releases)
[![PyPI](https://img.shields.io/pypi/v/cookiesparser)](https://pypi.org/project/cookiesparser/)

# Description
**cookiesparser** is a mini module for parsing cookies 🍪✨. This basic but super useful tool allows you to easily extract and encode cookies from strings.

# Installation
You can install cookiesparser using pip:
```
pip install cookiesparser
```

# Usage
```python
import cookiesparser as cparser

c = "token=xyz789; userId=42; color=blue;"
parsed = cparser.parse(c)
encoded = cparser.encode(parsed)
token = cparser.get_cookie(c, "token")
print(f"Orignal: {c}")
print(f"Parsed: {parsed}")
print(f"Encoded: {encoded}")
print(f"Token: {token}")
```
 # Output
 ```
Orignal: token=xyz789; userId=42; color=blue;
Parsed: {'token': 'xyz789', 'userId': '42'}
Encoded: token=xyz789; userId=42
Token: xyz789
```

# Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/farhaanaliii/cookiesparser).

# License
cookiesparser is released under the [Apache License](https://github.com/farhaanaliii/cookiesparser/blob/main/LICENSE).
