from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        A valid IP address consists of exactly four integers separated
        by single dots. Each integer is between 0 and 255 (inclusive) and
        cannot have leading zeros.

        For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
        but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
        addresses.
        Given a string s containing only digits, return all possible valid IP
        addresses that can be formed by inserting dots into s.
        You are not allowed to reorder or remove any digits in s.
        You may return the valid IP addresses in any order.

        >>> Solution().restoreIpAddresses("25525511135")
        ['255.255.11.135', '255.255.111.35']
        >>> Solution().restoreIpAddresses("0000")
        ['0.0.0.0']
        >>> Solution().restoreIpAddresses("101023")
        [['1.0.10.23','1.0.102.3','10.1.0.23','10.10.2.3','101.0.2.3']
        """
        if 4 > len(s) > 12:
            return []

        ans = set()

        def find(prefix: str, s: str):
            if not s and prefix.count('.') == 3:
                ans.add(prefix)
            elif s:
                if prefix:
                    prefix += '.'
                if s[0] == '0':
                    find(prefix + '0', s[1:] if len(s) > 0 else '')
                else:
                    for i in range(1, 4):
                        if s[0:i] and int(s[0:i]) < 256:
                            find(prefix + s[0:i], s[i:])

        find('', s)
        return list(ans)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
