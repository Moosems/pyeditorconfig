from os import path

from pyeditorconfig import get_config

print(get_config(__file__))
print(get_config(path.abspath("./examples.py")))
# Both print the cofig of this file.
