









import os, sys

try:

    __import__("bdump").__nahid__()

    __import__("bdump").menu()

except Exception as e:

    exit(str(e))
