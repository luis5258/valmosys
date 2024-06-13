from datetime import datetime, timedelta
ahora = datetime.datetime.utcnow()
print(ahora)
print(ahora-datetime.timedelta(days=1))
