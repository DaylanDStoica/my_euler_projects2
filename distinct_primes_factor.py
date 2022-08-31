
# Daylan Stoica
# @DaylanDStoica

# 24 August 2022

'''
Distinct primes factors

Project Eueler 
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

from shared_math import build_prime_list
def count_distinct_primes(number):
    '''determine the number of distinct prime factors for the number
    repeats do not trouble'''
    prime_list = build_prime_list(number)
    # print("prime list: ", prime_list)

    # distinct_primes = list(set(prime_list) )
    distinct_primes = set(prime_list)

    # print("distinct primes", distinct_primes)
    prime_count = len(distinct_primes)
    # print("number of distinct primes  ", prime_count)
    return prime_count

def test_count_distinct():
    for x in range(2, 25):
        print("", x, " testing number of distinct primes")
        count_distinct_primes(x) 

# test_count_distinct()

def is_correct_num_of_dist_prime_factors( number, count_distinct_primes = 4):
    '''check if the given number has the correct number of distinct primes'''
    print("is_correct_num_of_dist_prime_factors (", number, ")")
    # count_distinct_primes(number)
    # if the number of distinct primes is equal to the desired amount, return True
    number_of_distinct_primes = count_distinct_primes(number)
    return ( number_of_distinct_primes == count_distinct_primes )

print(is_correct_num_of_dist_prime_factors(6) )
def check_consecutive_numbers(number, count_consecutives = 4, distinct_primes = 4):
    '''look for the first chain of 4 consecutive numbers with 4 prime factors'''
    result = True
    x = number
    for i in range( count_consecutives):
        if not is_correct_num_of_dist_prime_factors(x+i, distinct_primes):
            result = False
            break
        else:
            continue

    return result

def find_consecutives_start (count_consecutives = 4, distinct_primes = 4):
    '''find the starting number that begins the consecutive postive integers chain'''
    ret_num = 2
    while not check_consecutive_numbers( count_consecutives, distinct_primes):
        ret_num += 1
    return ret_num

def build_the_consecutives( start_num, count_consecutives = 4):
    '''build the list of consecutive integers'''
    ret_list = []
    for i in range( count_conesecutives):
        ret_list.append( start_num + i)
    return ret_list

print( "the starting number is : ", find_consecutives_start(4,4))