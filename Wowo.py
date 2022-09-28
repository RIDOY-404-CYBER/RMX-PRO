import os, sys

try:

    __import__("pub").rmx()

except Exception as e:

    exit(str(e))
