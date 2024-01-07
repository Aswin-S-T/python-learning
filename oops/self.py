class Number:
    def __init__(self,value):
        self.value = value

    def print_number(self):
        return self.value

x = Number(44)
print(x.print_number())