

# hours left until tomorrow

from datetime import datetime, timedelta

now = datetime.now()
tommorow = (now + timedelta(days = 1)).replace(hour=0, minute=0, second=0, microsecond=0)
print(tommorow - now)
print((tommorow - now).total_seconds() / 3600)