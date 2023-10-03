class IO():
    def get_str(self):
        self.s = input()

    def print_str(self):
        print(self.s.upper())

x = IO()
x.get_str()
x.print_str()