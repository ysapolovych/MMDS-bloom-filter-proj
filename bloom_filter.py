import mmh3
import numpy as np

class BloomFilter:
    def __init__(self, filter_path=None, n_elements=1000, fp_prob=0.1):
        # https://ebrary.net/25915/computer_science/hashing_functions
        # bitarray size
        self.size = -int((n_elements * np.log(fp_prob)) / np.log(2)**2)
        # n of hash functions
        self.k = int((self.size * np.log(2)) / n_elements)
        # bitarray
        if filter_path is None:
            self.filter = np.zeros(self.size).astype(int)
            print(f'Initiazied filter of size {self.size}')
        else:
            self.filter = self.load_filter(filter_path)

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

    def save_filter(self, out_path):
        np.save(out_path, self.filter)

    def load_filter(self, in_path):
        self.filter = np.load(in_path)
