import threading

class PrimosSphGrm(threading.Thread):
    def __init__(self, row):
        super().__init__()
        self.row = row
        self.count_primes = 0

    def run(self):
        self.count_primes = sum(map(self.is_prime_sph_grm, self.row))
        print(f"{threading.current_thread().name} -> {self.count_primes}")

    def is_prime(self, x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def is_prime_sph_grm(self, x):
        if(self.is_prime(x) and self.is_prime(x * 2 + 1)):
            return 1
        return 0

matrix = [
    [2, 8, 21, 33],
    [53, 77, 101, 117],
    [419, 477, 503, 601]
    ]

for row in matrix:
    thread = PrimosSphGrm(row)
    thread.start()