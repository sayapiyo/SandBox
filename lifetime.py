import datetime

today = datetime.date.today()
bithday = datetime.date(2014,1,1)
life = today - bithday
print(life.days)
