def getnextIp(ipaddr):
     nextvalidIp = ""
     nextIp = str(ipaddr).split('.')
     for ip in nextIp:
         if int(ip) < 0 or int(ip) > 255:
             return "invalid IP"
     
     firstOctet,sndOctet,TrdOctet,FthOctet = nextIp
     modified = False
     #"192.168.10.255"
     if int(nextIp[3]) < 255:
         FthOctet = int(nextIp[3]) + 1
         modified = True
     else:
         if int(nextIp[3]) == 255:
            FthOctet = 0
            if int(nextIp[2]) < 255:
                TrdOctet = int(nextIp[2]) + 1
                modified = True
            else:
                if int(nextIp[2]) == 255:
                    TrdOctet = 0
                    modified = True
                    secOctet=True
    
     if not modified :
         if int(nextIp[2]) < 255:  # third octet also 255
             TrdOctet = int(nextIp[2]) + 1
             modified = True
         else:
            if int(nextIp[2]) == 255:
                TrdOctet=0
            if int(nextIp[1]) < 255:
                sndOctet = int(nextIp[1]) + 1
                modified = True
            else:
                if int(nextIp[1]) == 255:
                    sndOctet = 0
                    modified = True
                    firstOctet=True

     if not modified or secOctet:
         if int(nextIp[1]) < 255:
             sndOctet = int(nextIp[1]) + 1
             modified = True
         else:
             if int(nextIp[0]) < 255:
                 #sndOctet = 0
                 firstOctet =  int(nextIp[0]) + 1
                 modified = True
             else:
                 if int(nextIp[0]) == 255:
                    firstOctet = 0
                    modified = True
                    #firstOct=True
         
     if not modified or firstOctet:
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


#ipaddr = "192.168.10.1"
#ipaddr = "192.255.255.255" - Fials for this input 
ipaddr = "192.255.255.255"
getnextIp(ipaddr)
     
