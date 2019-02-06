# Script to rename bulk files in a directory
import os 

os.chdir('dir path')

for f in os.listdir():
  os.rename(f, f.replace('value to replace','new value'))
