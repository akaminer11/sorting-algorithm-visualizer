import random, time


class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(512), 512) # This is cool I learned about this for this project. It's much easier than making a helper function. Well, 4 lines of code easier.
        self.name = name
        
    def update_display(self, swap1=None, swap2=None):
        import main
        main.update(self, swap1, swap2)
    
    def run(self):
        self.start_time = time.time()
        self.time_elapsed = self.start_time - time.time()
        self.algorithm()
        return self.array, self.time_elapsed

    def swap(self, array, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def find_min_index(self, i):
        min_index = i
        for j in range(i+1, len(self.array)):
            if self.array[min_index] > self.array[j]:
                min_index = j
        return min_index


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")
    
    def algorithm(self):
        for i in range(len(self.array)):
            min_index = self.find_min_index(i)
            self.swap(self.array, i, min_index)
            self.update_display(self.array[i], self.array[min_index])


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self): # In my other project I made bubble sort way to complicated. Found a much easier way to do it.
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.swap(self.array, j, j+1)
                self.update_display(self.array[j], self.array[j+1])


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for step in range(len(self.array)):
            key = self.array[step]
            j = step

            while j  > 0 and self.array[j-1] > key:
                self.array[j] = self.array[j-1]
                j -= 1

            self.array[j] = key
            self.update_display(self.array[j], self.array[step])

class MergeSort(Algorithm): # most of this is yoinked from a previous project
    def __init__(self):
        super().__init__("MergeSort")
    
    def algorithm(self, array=[]):
        if array == []:
            array = self.array

        if len(array) == 1:
            return array

        mid = len(array) // 2

        L = self.algorithm(array[:mid])
        R = self.algorithm(array[mid:])

        return self.merge(L, R)

    def merge(self, L, R):
        merged = []
        left_index, right_index = 0, 0
        
        # go through the arrays and check for anything left over
        while left_index < len(L) and right_index < len(R):
            if L[left_index] > R[right_index]:
                merged.append(R[right_index])
                right_index += 1
            else:
                merged.append(L[left_index])
                left_index += 1

        # check for anything left over
        merged += L[left_index:]
        merged += R[right_index:]

        self.array = merged 

        # update display
        self.update_display()
        
        # return the new array
        return merged


class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")
    
    def algorithm(self, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        
        if start < end:
            pivot = self.partition(array, start, end)
            self.algorithm(array, start, pivot-1)
            self.algorithm(array, pivot+1, end)
        
    def partition(self, array, start, end):
        pivot = array[end]
        small_element_index = start - 1

        for x in range(start, end+1):
            if array[x] <= pivot:
                small_element_index += 1
                if small_element_index < x:
                    self.swap(array, small_element_index, x)
                    self.update_display(array[small_element_index], array[x])

        return small_element_index # return the partition