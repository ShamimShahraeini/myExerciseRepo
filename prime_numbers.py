
number_of_lines = 2
lines=[]
for i in range(number_of_lines):
    lines.append(input())

low, high = int(lines[0]), int(lines[1])
primes = []

for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1
    
    if num == 2:
        primes.append(2)
    if num == 3:
        primes.append(3)

    if num % 2 == 0:
        continue
        
    if num % 3 == 0:
        continue

    iter = 3

    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
        iter += 2

    if flag == 0:
        primes.append(num)

result = '\n'.join(map(str, primes))

print(result)