import pandas as pd

data = pd.read_fwf("day1.txt", header=None)

left = data[0].sort_values().to_list()
right = data[1].sort_values().to_list()

diff = 0
for i in range(len(left)):
    diff += abs(left[i] - right[i])
    
print(diff)