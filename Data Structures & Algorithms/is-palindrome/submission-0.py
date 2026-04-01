class Solution:
    def isPalindrome(self, s: str) -> bool:
        ct = re.sub(r'[^a-zA-Z0-9]', '', s)
        ct=ct.lower()
        return ct==ct[::-1]