opened_file = open("2022_sales.txt")
read_file = opened_file.read()
first_3_orders = read_file[:23]
print(first_3_orders)
opened_file.close()
