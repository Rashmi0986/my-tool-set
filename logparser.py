import os 
import re


regex = r'''Exception'''
for dirPath,dirNames,files in os.walk('IPV4_ADDR/'):
    curDir = os.path.join(dirPath) # needed to find in the curreDirectory or else throws file not found exception 
    for fileName in files:
        curFile = os.path.join(curDir , fileName)
        if os.stat(curFile).st_size != 0: # if current file is not empty
            result = []
            with open(curFile) as f:
                 for (i,line) in enumerate(f):
                     m = re.search(regex, line)
                     if m:
                        print (f' {m.group()} found in {fileName} located at path {curFile} at line num {m.span()[0]}')



"""
Output :

 RASHMIBSs-MacBook-Pro:RealPython_All_files rashmibs$ python3 logParser.py 
 Exception found in logger.txt located at path IPV4_ADDR/logger.txt at line num 12
 Exception found in logger.txt located at path IPV4_ADDR/logger.txt at line num 11
 Exception found in logger.txt located at path IPV4_ADDR/logger.txt at line num 12
 Exception found in logger.txt located at path IPV4_ADDR/logger.txt at line num 7
 Exception found in logger.txt located at path IPV4_ADDR/logger.txt at line num 22
 Exception found in logger.txt located at path IPV4_ADDR/logger.txt at line num 7
 Exception found in file_6.txt located at path IPV4_ADDR/Dir_2/file_6.txt at line num 12
 Exception found in file_6.txt located at path IPV4_ADDR/Dir_2/file_6.txt at line num 2
 Exception found in file7.txt located at path IPV4_ADDR/Dir_2/file7.txt at line num 11
 Exception found in file8.txt located at path IPV4_ADDR/Dir_2/file8.txt at line num 11
 Exception found in file_4.txt located at path IPV4_ADDR/Dir_1/file_4.txt at line num 21
 Exception found in file_4.txt located at path IPV4_ADDR/Dir_1/file_4.txt at line num 13
 Exception found in file_3.txt located at path IPV4_ADDR/Dir_1/file_3.txt at line num 10
 Exception found in file_3.txt located at path IPV4_ADDR/Dir_1/file_3.txt at line num 12
 """"

#Updated Code using pathlib
from pathlib import Path
import re

regex = re.compile(r'Exception')

root = Path("IPV4_ADDR")

for path in root.rglob("*"):   # recursive walk
    if path.is_file() and path.stat().st_size > 0:   # non-empty files only
        
        with path.open("r", encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, start=1):
                if regex.search(line):
                    print(f'Exception found in {path.name} located at {path} at line {lineno}')
                    
 Exception found in file_3.txt located at path IPV4_ADDR/Dir_1/file_3.txt at line num 11
 

