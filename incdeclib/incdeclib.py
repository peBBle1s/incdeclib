class incdecnum:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1
        return self

    def decrement(self):
        self.value -= 1
        return self

    def __repr__(self):
        return str(self.value)

# Example usage
num = incdecnum(5)
print(num)          # Output: 5
num.inc()
print(num)          # Output: 6
num.dec()
print(num)          # Output: 5
