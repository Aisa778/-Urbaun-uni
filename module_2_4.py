numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True  # когда число не делится на 2
for i in range(2, len(numbers)+1):
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
    else:
        primes.append(i)
print (primes)
print(not_primes)

# долго мучилась, почему в range(2, len(numbers)+1) начинается с индекса 2, ведь в списке числе это индекс числа 3
# я что то не поняла?