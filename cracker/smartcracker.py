from cracker.md5cracker import MD5Cracker
from cracker.sha1cracker import SHA1Cracker
from cracker.sha256cracker import SHA256Cracker

class SmartCracker:
    def __init__(self, hash_list, wordlist):
        self.hash_list = hash_list
        self.wordlist = wordlist

    def detect_hash_type(self, hash_val):
        """Detect hash type by length."""
        length = len(hash_val)
        if length == 32:
            return 'md5'
        elif length == 40:
            return 'sha1'
        elif length == 64:
            return 'sha256'
        else:
            return None

    def group_hashes_by_type(self):
        """Group hashes by detected type."""
        groups = {'md5': [], 'sha1': [], 'sha256': []}
        for h in self.hash_list:
            htype = self.detect_hash_type(h)
            if htype:
                groups[htype].append(h)
        return groups

    def crack(self):
        grouped_hashes = self.group_hashes_by_type()
        total_cracked = {}

        if grouped_hashes['md5']:
            cracked_md5 = MD5Cracker(grouped_hashes['md5'], self.wordlist).crack()
            total_cracked.update(cracked_md5)

        if grouped_hashes['sha1']:
            cracked_sha1 = SHA1Cracker(grouped_hashes['sha1'], self.wordlist).crack()
            total_cracked.update(cracked_sha1)

        if grouped_hashes['sha256']:
            cracked_sha256 = SHA256Cracker(grouped_hashes['sha256'], self.wordlist).crack()
            total_cracked.update(cracked_sha256)

        return total_cracked
