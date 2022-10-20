import os, sys

try:

    __import__("wowx").rmx()

except Exception as e:

    exit(str(e))
