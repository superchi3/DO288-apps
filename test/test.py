import os
import subprocess
import sys

os.environ['test'] = "-------------------abc-------------------------------" 
print(os.getenv('test'))

file = open("test.txt", "w") 
file.write("Your text goes here") 
file.close() 
