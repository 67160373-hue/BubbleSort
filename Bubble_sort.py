class BubbleSorter:
    def __init__(self, num):
        self.num = num
    def display(self):
        print(f"Current data{(self.num)}")
    def sort(self):
        for i in range (len(self.num)):
          for j in range(len(self.num)-1):
            if self.num[j] > self.num[j+1]:
                self.num[j], self.num[j + 1] = self.num[j+1], self.num[j]
          print(f"After Round {i+1} {self.num}")

nums = [64,34,25,12,22,11,90]
sorter = BubbleSorter(nums)
print("Before sorting:")
sorter.display()
sorter.sort()
print("After sorting:")
sorter.display()



