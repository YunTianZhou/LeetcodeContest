class XorBasis:
    def __init__(self, n: int):
        self.b = [0] * n

    def insert(self, x: int):
        b = self.b

        for i in range(len(b) - 1, -1, -1):
            if x & (1 << i):
                if b[i] == 0:
                    b[i] = x
                    return
                x ^= b[i]

    def max_xor(self) -> int:
        b = self.b
        res = 0

        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        
        return res
