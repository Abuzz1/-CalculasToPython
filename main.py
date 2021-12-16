# i = input("Input: ")

class convert():
    def __init__(self, input, lam):
        self.input = input
        self.lam = lam
    def run(self):
        check = lambda: True if self.lam is True else False
        lambda:  lam() if check()== True else nan()
          





a = convert("foo", True)



a.print()