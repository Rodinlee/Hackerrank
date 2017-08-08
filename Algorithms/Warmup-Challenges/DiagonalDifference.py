# DiagonalDifference.py

'''
Input Format
The first line contains a single integer, N.
The next N lines denote the matrix's rows, with each  line containing N
space-separated integers describing the columns.

Output Format
Print the absolute difference between the two sums of the matrix's
diagonals as a single integer.
'''

import sys

n = int(input().strip())
a = []

for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
