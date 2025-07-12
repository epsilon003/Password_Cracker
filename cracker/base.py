from abc import ABC, abstractmethod

class BaseCracker(ABC):
    def __init__(self, hash_list, wordlist):
        self.hash_list = hash_list
        self.wordlist = wordlist
        self.cracked = {}

    @abstractmethod
    def crack(self):
        pass
