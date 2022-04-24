import os
import re
import sys
import glob

assert len(sys.argv) == 2
version = sys.argv[1]

assert re.match('^[0-9]+\.[0-9]+\.[0-9]+', version)

with open('mmtester/__init__.py', 'w') as f:
    f.write(f"__version__ = '{version}'\n")
    
for path in glob.glob('mmtester/*.cfg'):
    with open(path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith('version'):
            lines[i] = f'version = {version}\n'
            break

    with open(path, 'w') as f:
        f.writelines(lines)
    

