import os
from pathlib import Path

p = Path(os.path.realpath(__file__))
parent = p.parent.parent.parent
print()
print(os.path.join(parent,"geckodriver"))
print()
