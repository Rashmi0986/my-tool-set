# Use the pathlib module to join the files  from different platform (windows mac and Unix)
# ref - https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


import os 
import re


regex = r'''^.*Exception.*$'''
for dirPath,dirNames,files in os.walk('IPV4_ADDR/'):
    curDir = os.path.join(dirPath) # needed to find in the curreDirectory or else throws file not found exception 
    for fileName in files:
        curFile = os.path.join(curDir , fileName)
        if os.stat(curFile).st_size != 0: # if current file is not empty
            result = []
            with open(curFile) as f:
                 for (i,line) in enumerate(f):
                     m = re.findall(regex, line)
                     if m:
                        print(f'{m} found in {fileName} located at path {curFile} at line num {i+1}')
                        
 
 
 
 """
 output :
 
 
 
['NoSuchMethodException'] found in logger.txt located at path IPV4_ADDR/logger.txt at line num 1
['NullPointerException'] found in logger.txt located at path IPV4_ADDR/logger.txt at line num 4
['NumberFormatException'] found in logger.txt located at path IPV4_ADDR/logger.txt at line num 7
['RuntimeException'] found in logger.txt located at path IPV4_ADDR/logger.txt at line num 11
['StringIndexOutOfBoundsException'] found in logger.txt located at path IPV4_ADDR/logger.txt at line num 15
['ServiceException'] found in logger.txt located at path IPV4_ADDR/logger.txt at line num 18
['FileNotFoundException'] found in file_6.txt located at path IPV4_ADDR/Dir_2/file_6.txt at line num 1
['IOException'] found in file_6.txt located at path IPV4_ADDR/Dir_2/file_6.txt at line num 4
['InterruptedException'] found in file7.txt located at path IPV4_ADDR/Dir_2/file7.txt at line num 1
['NoSuchFieldException'] found in file8.txt located at path IPV4_ADDR/Dir_2/file8.txt at line num 1
['ArrayIndexOutOfBoundsException'] found in file_4.txt located at path IPV4_ADDR/Dir_1/file_4.txt at line num 1
['ClassNotFoundException'] found in file_4.txt located at path IPV4_ADDR/Dir_1/file_4.txt at line num 3
['ArithmeticException'] found in file_3.txt located at path IPV4_ADDR/Dir_1/file_3.txt at line num 1
['myArithmeticException'] found in file_3.txt located at path IPV4_ADDR/Dir_1/file_3.txt at line num 3
['NullPointerException'] found in file_3.txt located at path IPV4_ADDR/Dir_1/file_3.txt at line num 4



""""
