import hashlib
from .base import BaseCracker

class SHA1Cracker(BaseCracker):
    def crack(self):
        for h in self.hash_list:
            for word in self.wordlist:
                if hashlib.sha1(word.encode()).hexdigest() == h:
                    self.cracked[h] = word
                    break
        return self.cracked
