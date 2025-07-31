class Solution:
    def works(self, s):
        return s == str(int(s)) and int(s) <= 255 and int(s) >= 0

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if self.works(a) and self.works(b) and self.works(c) and self.works(d):
                        ans.append(f'{a}.{b}.{c}.{d}')
        return ans


#restore_Ip with backtracking 
def restoreIpAddressesAlt(s):
    """
    Alternative implementation with slightly different structure
    """
    def backtrack(start, path, result):
        # If we have 4 parts and used all characters
        if len(path) == 4:
            if start == len(s):
                result.append('.'.join(path))
            return
        
        # Try each possible length for next part
        for i in range(start, min(start + 3, len(s))):
            part = s[start:i + 1]
            
            # Validate the part
            if (len(part) == 1 or 
                (len(part) > 1 and part[0] != '0')) and int(part) <= 255:
                
                path.append(part)
                backtrack(i + 1, path, result)
                path.pop()
    
    result = []
    backtrack(0, [], result)
    return result
