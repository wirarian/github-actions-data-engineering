import datetime

print("Starting data pipeline...")

data = [
    {"customer": "Alice", "sales": 100},
    {"customer": "Bob", "sales": 200},
    {"customer": "Charlie", "sales": 150},
]

total_sales = sum(row["sales"] for row in data)

print(f"Number of records: {len(data)}")
print(f"Total sales: ${total_sales}")

print(f"Pipeline completed at {datetime.datetime.now()}")