from timeit import default_timer
from functools import cache

MIX_1 = 2**6  # 64 == 2^6
MIX_2 = 2**5  # 32 == 2^5
MIX_3 = 2**11 # 2^11 == 2048
PRUNE_FACTOR = 2**24 # 2^^24 == 16777216

def get_initial_secret_numbers():
    ACTUAL_FILE = "input.txt"
    TEST_FILE = "input_test.txt"
    initial_secret_numbers = []
    with open(ACTUAL_FILE, "r") as input_file:
        for line in input_file.readlines():
            initial_secret_numbers.append(int(line.strip()))

    return initial_secret_numbers

def print_binary(n):
    #print(n)
    print("{:025b}".format(n))

@cache
def calculate_next_secret_number1(n):
    n1 = n * MIX_1
    n = n1 ^ n
    n = n % PRUNE_FACTOR
    n1 = n // MIX_2
    n = n1 ^ n
    n = n % PRUNE_FACTOR
    n1 = n * MIX_3
    n = n1 ^ n
    n = n % PRUNE_FACTOR
    return n

def calculate_next_secret_number2(n):
    n ^= n << 6
    n %= PRUNE_FACTOR
    n ^= n >> 5
    n %= PRUNE_FACTOR
    n ^= n << 11
    n %= PRUNE_FACTOR
    return n

initial_secret_numbers = get_initial_secret_numbers()
total = 0
for secret_number in initial_secret_numbers:
    for _ in range(2000):
        secret_number = calculate_next_secret_number1(secret_number)
    total += secret_number
    # print(secret_number)
print(total)

'''
outputs = [[],[]]
for o, f in enumerate([calculate_next_secret_number1, calculate_next_secret_number2]):
    start = default_timer()
    for n in range(1000000):
        outputs[o].append(f(n))
    end = default_timer()
    print(end - start)
print(outputs[0] == outputs[1])
'''
