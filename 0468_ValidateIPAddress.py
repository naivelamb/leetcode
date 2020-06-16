"""
https://leetcode.com/problems/validate-ip-address/
"""

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            return self.isIPV4(IP)
        elif ':' in IP:
            return self.isIPV6(IP)
        else:
            return 'Neither'

    def isIPV4(self, IP):
        IP = IP.split('.')
        if len(IP) != 4:
            return 'Neither'

        for num in IP:
            if not num.isdigit():
                return 'Neither'
            if num[0] == '0' and len(num) > 1:
                return 'Neither'
            num = int(num)
            if num < 0 or num > 255:
                return 'Neither'
        return 'IPv4'

    def isIPV6(self, IP):
        IP = IP.split(':')
        if len(IP) != 8:
            return 'Neither'

        for num in IP:
            num = num.lower()
            if len(num) > 4 or len(num) < 1:
                return 'Neither'
            if num[0] == '-':
                return 'Neither'

            try:
                num = int(num, 16)
            except:
                return 'Neither'

            if num < 0 or num > 2**17 - 1:
                return 'Neither'
        return 'IPv6'   
