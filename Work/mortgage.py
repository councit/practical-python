# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0

# while principal > 0:
# 	principal = principal * (1 + rate / 12) - payment
# 	total_paid = total_paid + payment

# print('Total paid:', round(total_paid, 2))

# Exercise 1.8
first_year_payment = payment + 1000
month_count = 0
for i in range(12):
	principal = principal * (1 + rate / 12) - first_year_payment
	total_paid = total_paid + first_year_payment
	month_count += 1
	print(month_count, total_paid, principal)

while principal > 0:
	principal = principal * (1 + rate / 12) - payment
	total_paid = total_paid + payment
	month_count += 1
	print(month_count, total_paid, principal)
print('Total Paid:', total_paid, 'Months:', month_count)

