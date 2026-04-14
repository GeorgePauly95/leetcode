class IterativeSolution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        while n / 2 != 1.0:
            n = n / 2
            if n < 1:
                return False
        else:
            return True


class RecursiveSolution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        return self.isPowerOfTwo(n / 2)
