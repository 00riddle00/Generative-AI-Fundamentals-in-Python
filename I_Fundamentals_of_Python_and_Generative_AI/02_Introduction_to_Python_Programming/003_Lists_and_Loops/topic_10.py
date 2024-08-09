opened_file = open("2022_sales.txt")
total_for_2022 = 0
file_lines = opened_file.readlines()

for line in file_lines:
    stripped_line = line.rstrip()
    sales_total = float(stripped_line)
    total_for_2022 += sales_total

opened_file.close()

print(total_for_2022)
