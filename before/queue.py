class Queue:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return f"{[q_element for q_element in self.args]}"

    def shift(self, item):
        new_list = [item]
        new_list.extend(self.args)
        self.args = new_list
        print(f"{item} was successfully shifted to the queuy")

    def unshift(self):
        if(self.args):
            temp = self.args[0]
            self.args = self.args[1:]
            print(f"{temp} was successfully unshifted from the queuy")

    def showQueue(self):
        print(self.args)
