#!/usr/bin/env python3

class Wrapper:
    def __init__(self):
        self.var1 = "a"
        self.var2 = "b"
        self.var3 = "c"
        self.var4 = "d"

        self.db = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                   'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}


    def show_info(self):
        print(self.var1)
        print(self.var2)
        print(self.var3)
        print(self.var4)


    def get_data(self, n):
        if n.lower() in self.db.keys:
            return self.db[n]
        else:
            print("invalid key.")
            return
