class Math:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
print(Math.is_prime(7))  # виведе True
print(Math.is_prime(12))  # виведе False
