import mmh3
import numpy as np

class BloomFilter:
    def __init__(self, n_elements, fp_prob=0.1):
        # https://ebrary.net/25915/computer_science/hashing_functions
        # bitarray size
        self.size = -int((n_elements * np.log(fp_prob)) / np.log(2)**2)
        # n of hash functions
        self.k = int((self.size * np.log(2)) / n_elements)
        # bitarray
        self.filter = np.zeros(self.size).astype(int)
        print(f'Initiazied filter of size {self.size}')

    def insert(self, element):
        for i in range(self.k):
            hash = mmh3.hash(element, i) % self.size
            self.filter[hash] = 1

    def check(self, element):
        for i in range(self.k):
            hash = mmh3.hash(element, i) % self.size
            if self.filter[hash] != 1:
                return False
        return True
