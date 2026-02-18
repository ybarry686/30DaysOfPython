import statistics
from collections import Counter

class Statistics():
    def __init__(self, lst):
        self.lst = lst
    
    def count(self):
        count = 0
        
        for num in self.lst:
            count += 1
                
        return count
    
    def min(self):
        smallest = float('inf')
        
        for num in self.lst:
            if num < smallest:
                smallest = num      
        
        return smallest
                
    def max(self):
        largest = float('-inf')
        
        for num in self.lst:
            if num > largest:
                largest = num

        return largest
    
    def range(self):
        lowest = self.min()
        highest = self.max()

        return highest - lowest
  
    def mean(self):
        sum_lst = 0

        for num in self.lst:
            sum_lst += num
                        
        return sum_lst / len(self.lst)

    def median(self):
        sorted_lst = self.merge_sort(self.lst)
        n = len(sorted_lst)

        if n % 2 != 0:
            mid = sorted_lst[n // 2]
        else:
            left_val = sorted_lst[(n // 2) - 1]
            right_val = sorted_lst[n // 2]
            mid = (left_val + right_val) / 2
        
        return mid

    def merge_sort(self, arr):
        # Helper function for sorting
        n = len(arr)

        if n == 1:
            return arr
        
        mid = len(arr) // 2
        l_half = arr[:mid]
        r_half = arr[mid:]

        l_half = self.merge_sort(l_half)
        r_half = self.merge_sort(r_half)
        l_index, r_index = 0, 0

        sorted_arr = [0] * n
        i = 0

        while l_index < len(l_half) and r_index < len(r_half):
            if l_half[l_index] < r_half[r_index]:
                sorted_arr[i] = l_half[l_index]
                l_index += 1
            else:
                sorted_arr[i] = r_half[r_index]
                r_index += 1
            
            i += 1
        
        while l_index < len(l_half):
            sorted_arr[i] = l_half[l_index]
            l_index += 1
            i += 1

        while r_index < len(r_half):
            sorted_arr[i] = r_half[r_index]
            r_index += 1
            i += 1

        return sorted_arr

    def mode(self):
        counts = Counter(self.lst)
        max_count = max(counts.values())
        
        modes = {val for val, count in counts.items() if count == max_count}
        
        res = {}

        for num in modes:
            res['mode'] = num
            res['count'] = counts[num]
        
        return res

    def std(self):
        return round(self.var() ** 0.5, 3)
    
    def var(self):
        avg = self.mean()
        
        deviations = [(num - avg) ** 2 for num in self.lst]
        sum_deviations = 0

        for num in deviations:
            sum_deviations += num

        variance = sum_deviations / len(self.lst)

        return variance

    def freq_dist(self):
        freq = Counter(self.lst)
        freq_dist = []

        for val, count in freq.items():
            relative_freq = round((count / len(self.lst)) * 100, 3)
            pair = (relative_freq, val)
            
            freq_dist.append(pair)

        return freq_dist

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats = Statistics(ages)
print(stats.count())
print(stats.min())
print(stats.max())
print(stats.mean())
print(stats.median())
print(stats.range())
print(stats.mode())
print(stats.std())
print(stats.var())
print(stats.freq_dist())



