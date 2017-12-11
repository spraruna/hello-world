number = num = int(input('Enter a number:'))
digit = len(str(number))

sum = 0
while num > 0:
    temp = num % 10
    sum += temp ** digit
    num //= 10

if sum == number:
    print('Armstrong')
else:
    print('Not Armstrong')
