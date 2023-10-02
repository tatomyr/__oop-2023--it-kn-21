class MyIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_count:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

iterator = MyIterator(5)  

for item in iterator:
    print(item)
