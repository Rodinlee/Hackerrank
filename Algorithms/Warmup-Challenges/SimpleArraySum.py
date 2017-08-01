# Simple Array Sum

# Solution 1

n = int(input().strip())
arr = list(map(int, input().strip().split()))

def ArraySum(n, ar):
  sum = 0
  for elem in range(n):
    sum += arr[elem]
  return sum

result = SimpleArray(n, arr)
print(result)

# Solution 2

n = int(input().strip())
arr = list(map(int, input.split()))
print(sum(arr))
