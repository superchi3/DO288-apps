import os
import subprocess
import sys

os.environ['test'] = "-------------------abc-------------------------------" 

file = open("/tmp/hello.txt", "w") 
file.write("Your text goes here") 
file.close() 

os.environ['test'] = 'kevin'
