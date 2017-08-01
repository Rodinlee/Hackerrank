# Compare the Triplets

# Solution 1

a_triplet = map(int, input().split())
b_triplet = map(int, input().split())

a_points = 0
b_points = 0

for a_val, b_val in zip(a_triplet, b_triplet):
    if a_val > b_val:
        a_points += 1
    elif a_val < b_val:
        b_points += 1
print(a_points, b_points)


# Solution 2

lines = int(input(input().strip())
a_triplet = list(map(int, input().split())
b_triplet = list(map(int, input().split())

def CompareTriplets(first, second):
    a_points = 0
    b_points = 0
    for elem in range(lines):
        if first[elem] > second[elem]:
            a_points += 1
        elif first[elem] < second[elem]:
            b_points += 1
    return (a_points, b_points)
    
result = CompareTriplets(a_triplet, b_triplet)
print(" ".join(map(str, result)))
