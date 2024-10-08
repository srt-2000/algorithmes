from bitarray import bitarray

class BloomFilter(object):

    def __init__(self, size, number_expected_elements=100000):
        self.size = size
        self.number_expected_elements = number_expected_elements
        self.bloom_filter = bitarray(self.size)
        self.bloom_filter.setall(0)
        self.number_hash_functions = round(self.size/self.number_expected_elements)

    def _hash_djb2(self, s):
        our_hash = 5381
        for x in s:
            our_hash = ((our_hash << 5) + our_hash) + ord(x)
        return our_hash % self.size

    def _hash(self, item, k):
        return self._hash_djb2(str(k) + item)

    def add_to_filter(self, item):
        for n in range(self.number_hash_functions):
            self.bloom_filter[self._hash(item, n)] = 1

    def check_is_not_in_filter(self, item):
        for n in range(self.number_hash_functions):
            if self.bloom_filter[self._hash(item, n)] == 0:
                return True
        return False

bloom_filter = BloomFilter(1000000, 100000)
base_ip = "192.168.1."
bloom_filter.add_to_filter(base_ip + str(1))
bloom_filter.add_to_filter(base_ip + str(98))
bloom_filter.add_to_filter(base_ip + str(101))

print(f"A Bloom filter for negative IP address.\nWe have a base IP:{base_ip}\nAnd we add some sample ens for 3 addresses in filter: 1, 98, 101")
print("If we have a very large massive with 100000 IP,\nand we have to find IPs which are not allowed,\nwe use Bloom filter:\n")

for i in range(1, 100000):
    if not bloom_filter.check_is_not_in_filter(base_ip + str(i)):
        print(base_ip + str(i))

#https://habr.com/ru/companies/otus/articles/541378/