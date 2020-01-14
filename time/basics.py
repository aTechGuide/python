from datetime import datetime, timezone, timedelta

# Current time in our computer
print(datetime.now()) 

print(datetime.now(timezone.utc))

"""
- Recommendation -> our programmes should always work with UTC times.
- Store UTC times in your database, work with UTC times in your code.
- When we show time to a user, we convert it to their timezone.
"""

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today.strftime('%d-%m-%Y %H:%M:%S')) # String Format Time
print(tomorrow)

user_date = datetime.strptime("2020-01-11", '%Y-%m-%d') # String Parse Time
print(user_date)

