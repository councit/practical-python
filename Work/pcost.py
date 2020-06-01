# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
	headers = next(f).split(',')
	total_cost = 0.0

	for line in f:
		row = line.split(',')

		num1 = float(row[1])
		num2 = float(row[-1])
		total_cost += num1 * num2

	print(f'Total cost {total_cost}')







