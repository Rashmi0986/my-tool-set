# Script to search Ipv4 address in files 

import os 
import re


regex = r'''\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b''' 

for dirPath,dirNames,files in os.walk('IPV4_ADDR/'):
    curDir = os.path.join(dirPath) # needed to find in the curreDirectory or else throws file not found exception 
    for fileName in files:
        curFile = os.path.join(curDir , fileName)
        if os.stat(curFile).st_size != 0: # if current file is not empty
            result = []
            with open(curFile) as f:
                 for line in f:
                     result.extend(re.findall(regex, line, re.MULTILINE)) # in the same line multiple occurances of valid / invlaid IP address
                 if len(result) > 0:
                     print(f'Valid Ipv4 address found in file Path :{curFile} {result}') 
                     
""""                   
output
  
  
Valid Ipv4 address found in file Path :IPV4_ADDR/Dir_2/file_3 ['10.10.10.20', '20.20.20.20']
Valid Ipv4 address found in file Path :IPV4_ADDR/Dir_2/file_4 ['56.30.40.20']
Valid Ipv4 address found in file Path :IPV4_ADDR/Dir_3/file_5.txt ['46.30.50.20', '74.30.40.20']
Valid Ipv4 address found in file Path :IPV4_ADDR/Dir_1/file_1.txt ['10.20.30.40', '50.20.30.45', '67.37.84.30', '78.39.20.30', '0.0.0.0', '255.255.255.255', '200.100.2.32']
Valid Ipv4 address found in file Path :IPV4_ADDR/Dir_1/file_2.txt ['20.30.40.30', '24.36.40.20', '56.37.20.35']


"""
# udpated version of thsi code 
import os
import re

# Precompiled regex — faster for repeated use
IPV4_REGEX = re.compile(
    r'''\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b'''
)

BASE_DIR = 'IPV4_ADDR'

def find_ipv4_addresses_in_file(file_path):
    result = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                result.extend(IPV4_REGEX.findall(line))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return result

def scan_directory_for_ipv4(base_dir):
    for dirpath, _, filenames in os.walk(base_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                if os.path.getsize(filepath) == 0:
                    continue
            except OSError as e:
                print(f"Error getting size of {filepath}: {e}")
                continue

            ips_found = find_ipv4_addresses_in_file(filepath)
            if ips_found:
                print(f"✅ Valid IPv4 address(es) found in: {filepath} → {ips_found}")

if __name__ == "__main__":
    scan_directory_for_ipv4(BASE_DIR)




  
