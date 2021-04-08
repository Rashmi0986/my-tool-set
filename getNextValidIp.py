'''
192.168.10.255
192.168.11.0

0    1   2   3
192.168.255.255
192.169.0.0


192.168.10.6
192.168.10.7
'''

def getnextIp(ipaddr):
     nextvalidIp = ""
     nextIp = str(ipaddr).split('.')
     for ip in nextIp:
         if int(ip) < 0 or int(ip) > 255:
             return "invalid IP"
     
     firstOctet,sndOctet,TrdOctet,FthOctet = nextIp
     modified = False
     if int(nextIp[3]) < 255:
         FthOctet = int(nextIp[3]) + 1
         modified = True
     else:
         if int(nextIp[3]) == 255:
             FthOctet = 0
             TrdOctet = int(nextIp[2]) + 1
             modified = True
    
     if not modified:
         if int(nextIp[2]) < 255:  # third octet also 255
             TrdOctet = int(nextIp[2]) + 1
             modified = True
         else:
             if int(nextIp[2]) == 255:
                 TrdOctet = 0
                 sndOctet = int(nextIp[1]) + 1
                 modified = True

     if not modified:
         if int(nextIp[1]) < 255:
             sndOctet = int(nextIp[1]) + 1
             modified = True
         else:
             if int(nextIp[1]) == 255:
                 sndOctet = 0
                 firstOctet =  int(nextIp[0]) + 1
                 modified = True
         
     if not modified:
          if int(nextIp[0]) < 255:
              firstOctet = int(nextIp[0]) + 1
              modified = True
          else:
              if int(nextIp[0]) == 255:
                  return "Can't generate next IP" 
         
     nextvalidIp =  str(firstOctet) + '.' 
     nextvalidIp += str(sndOctet) + '.' 
     nextvalidIp +=    str(TrdOctet) + '.' 
     nextvalidIp += str(FthOctet)

     print (nextvalidIp)


ipaddr = "192.168.10.1"
ipaddr = "192.168.10.255"
getnextIp(ipaddr)
     
