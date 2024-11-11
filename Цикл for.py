numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
primes = []
not_primes = []
for i in range(0, len(numbers)):
    if numbers[i] == 2:
        primes.append(numbers[i])
    for j in range(1, i):
        #print(i, j)
        is_prime = numbers[i] % numbers[j] == 0
        if is_prime:
            not_primes.append(numbers[i])
            break
    if not is_prime:
        primes.append(numbers[i])
print(primes)
print(not_primes)
