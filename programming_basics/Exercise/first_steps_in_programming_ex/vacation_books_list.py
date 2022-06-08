book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_reading_time = book_pages / pages_per_hour
required_hours = total_reading_time / days
print(required_hours)
