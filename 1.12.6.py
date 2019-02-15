n = int(input())

mod10 = n % 10
mod100 = n % 100

if mod10 == 1 and mod100 != 11:
    end = ''
elif (1 < mod10 < 5) and not (11 < mod100 < 15):
    end = 'а'
else:
    end = 'ов'

print(f'{n} программист{end}')    