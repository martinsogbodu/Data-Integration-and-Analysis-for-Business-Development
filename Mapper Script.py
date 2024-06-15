# mapper.py
import sys

for line in sys.stdin:
    data = line.strip().split(',')
    customer_id = data[0]
    country = data[6]
    total_sales = float(data[10])
    print(f'{country}\t{total_sales}')
