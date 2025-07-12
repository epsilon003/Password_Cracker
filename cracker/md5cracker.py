import hashlib
from .base import BaseCracker

class MD5Cracker(BaseCracker):
    def crack(self):
        for h in self.hash_list:
            for word in self.wordlist:
                if hashlib.md5(word.encode()).hexdigest() == h:
                    self.cracked[h] = word
                    break
        return self.cracked
