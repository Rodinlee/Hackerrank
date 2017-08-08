# mutations.py

'''
Input Format
The first line contains a string, S.
The next line contains integer i, 
denoting the index location and a character c(separated by a space.)

Output Format
Using any of the methods explained above, replace the character at index i with character c
'''

input_string = input()
input_position, input_character = input().split()

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

new_string = mutate(input_string, input_position, input_character)
print(new_string)
