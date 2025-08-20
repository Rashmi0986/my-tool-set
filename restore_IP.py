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
def restoreIpAddresses(s):
    res = []
    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append(".".join(path))
            return
        for l in range(1, 4):
            if start + l > len(s):
                break
            part = s[start:start+l]
            if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                continue
            backtrack(start + l, path + [part])
    backtrack(0, [])
    return res


