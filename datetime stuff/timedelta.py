from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain

#OUTPUT:
#delta
#datetime.timedelta(days=64, seconds=29156, microseconds=10)
