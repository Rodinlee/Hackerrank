# Find a String

'''
Input Format
The first line of input contains the original string.
The next line contains the substring.

Output Format
Output the integer number indicating 
the total number of occureences of the substring in the original string.
'''

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string) == sub_string]:
            count += 1
    return count_


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)


