class CustomStack(object):

    def __init__(self, maxSize):
        self.max_size = maxSize
        self.cur_size = 0
        self.data = [[0,0]] * self.max_size
        print(self.data)

    def push(self, x):
        if self.cur_size < self.max_size:
            self.data[self.cur_size] = [x, 0]
            self.cur_size += 1
        print(self.data, "push")
    def pop(self):
        if self.cur_size <= 0:
            return -1

        val, inc = self.data[self.cur_size-1]
        self.cur_size -= 1

        if self.cur_size > 0:
            self.data[self.cur_size-1][1] += inc

        print(self.data, "pop")
        return val + inc

    def increment(self, k, val):
        self.data[min(self.cur_size-1, k-1)][1] += val
        print(self.data, "increment")


# Your CustomStack object will be instantiated and called as such:
maxSize = 5  # Example value for the maxSize
x = 10       # Example value for push
k = 2        # Example value for increment index
val = 3 

obj = CustomStack(maxSize)
obj.push(x)
obj.push(x)

param_2 = obj.pop()
obj.increment(k,val)
