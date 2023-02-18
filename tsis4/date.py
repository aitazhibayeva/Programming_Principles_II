#Ex 1
import datetime
before = datetime.date.today() - datetime.timedelta(days=5)
print(f'5 days before current date is: {before}')


#Ex 2
import datetime
tod = datetime.date.today()
yes = datetime.date.today() - datetime.timedelta(days=1)
tom = datetime.date.today() + datetime.timedelta(days=1)
print(f'Today is {tod}')
print(f'Yesterday is {yes}')
print(f'Tomorrow is {tom}')


#Ex 3
import datetime
date = datetime.datetime.today().replace(microsecond=0)
print(date)


#Ex 4
from datetime import datetime
def diff_in_sec(first, second):
    difference = first - second
    return difference.days * 24 * 3600 + difference.seconds

date1 = datetime.today()
year = input('Enter any previous or current year:\n')
month = input('Enter the month:\n')
day = input('Enter the day:\n')
hour = input('Enter the hour:\n')
minute = input('Enter the minute:\n')
second = input('Enter the second:\n')
date2 = datetime.strptime(f'{year}/{month}/{day} {hour}:{minute}:{second}', f'%Y/%m/%d %H:%M:%S')
print('Difference in seconds is:', diff_in_sec(date1, date2))