converted_amounts = [
    3.14,
    2,
    1.57,
    10,
    9.82,
    5,
    7.26,
    4,
    6,
    2.58,
    8,
    12,
    0.35,
    15,
    3,
    2.98,
    11,
    6.35,
    4.79,
    9,
    1,
    13,
    7,
    2,
]

sum_manual = 0
for value in converted_amounts:
    sum_manual += value

print(sum_manual)
print(sum(converted_amounts))
