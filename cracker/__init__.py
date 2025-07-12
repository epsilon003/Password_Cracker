# cracker/__init__.py

"""
Cracker Module Package

Includes hash-specific password crackers:
- SHA256Cracker
- MD5Cracker
- SHA1Cracker
"""

from .sha256cracker import SHA256Cracker
from .md5cracker import MD5Cracker
from .sha1cracker import SHA1Cracker
