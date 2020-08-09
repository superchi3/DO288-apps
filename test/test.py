import os
import subprocess
import sys

os.environ['test'] = "-------------------abc-------------------------------" 
print(os.getenv('test'))
