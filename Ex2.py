"""
Consider we have an array of number ranges which is sorted based on lower number
of ranges. We want to find the array of ranges which has all distinct ranges from
input array after merging ranges which overlap each other.

Sample input: [(1, 3), (4, 7), (5, 9), (11, 18), (12, 15)]
Sample output: [(1, 3), (4, 9), (11, 18)]
"""

#ranges = [(1, 3), (4, 7), (5, 9), (11, 18), (12, 15)]
ranges = [range(1,4), range(4,8), range(5,10), range(11,19), range(12,15)]



for i in range(len(ranges)-1):
    if ranges[i][-1] <  ranges[i+1][1]: print ranges[i]
    elif ranges[i][-1] >= ranges[i+1][1]: print range(ranges[i][0], ranges[i+1][-1])


