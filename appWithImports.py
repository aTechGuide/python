
"""
Whenever we import something, the thing we're importing is now called a module. 
And it is executed in module mode, which is essentially the same as executing it in normal mode, or script mode but there are some minor differences

Basically, file_operations is the module and app.py is script
"""

# Method 1 to import
# import importingFiles.utils.file_operations
# importingFiles.utils.file_operations.save_to_file('Almaas Ali', 'resources/importing_files/data.txt')
# print(importingFiles.utils.file_operations.read_file('resources/importing_files/data.txt'))

"""
# Method 2 to import
from importingFiles.utils.file_operations import save_to_file, read_file
save_to_file('Rolf', 'resources/importing_files/data.txt')
print(read_file('resources/importing_files/data.txt'))
"""

from importingFiles.utils.file_operations import *
from importingFiles.find import hello


save_to_file('Rolf', 'resources/importing_files/data.txt')
print(read_file('resources/importing_files/data.txt'))

"""
- Whenever we run a file as a script, __name__ = __main__
"""
print(__name__)






