
def getSubnetMask(prefix):
  subnetBit = 32 - prefix
  if prefix == 25 or prefix == 17 or prefix == 9 or prefix == 1:
      value = 128
  else:
      value = 128
      value += pow(2, subnetBit)
    
  value = str(value)
  
  if prefix >= 25 and prefix <= 32: #4th octet
      res = "255.255.255."+value
  elif prefix >= 17 and prefix <= 23: #3rd octet
      res = "255.255."+value+".255"
  elif prefix >= 8  and prefix <= 16: # 2nd octet
      res = "255."+value+".255.255"
  else:
      res = "value"+".255.255.255"
  return res

print(getSubnetMask(17))
    
    
  
  
