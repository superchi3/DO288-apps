import os
import subprocess
import sys

os.environ['test'] = "-------------------abc-------------------------------" 
print(os.getenv('test'))

file = open("/tmp/hello.txt", "w") 
file.write("Your text goes here") 
file.close() 
