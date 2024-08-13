"""Exercise:
    Sum the even numbers in a list"""

# List of numbers to include both odd and even
nums = [1, 2, 3, 4, 5, 6]

sum = 0

# Update the sum by adding in this number only if it is even
for num in nums:
    # Check if the number is even
    if int(num / 2) * 2 == num:
        sum += num

print(sum)
