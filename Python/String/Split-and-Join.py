# Hackerrankg Python Strings
# String Split and Join

'''
Task
You are given a string. Split the string on a " " delimiter and join using - hyphen
Input Format
The first line contains a string consisting of space separated words
Output Format
Print the formatted string as explained above
'''

# Solution 1
line = input()
def split_and_join(line):
    lines = line.slpit()
    lines = "-".join(new_lines)
    return lines

print(split_and_join(line))

# Solution 2
print(input().replace("","-"))

# Solution 3
print("-".join(input().split()))