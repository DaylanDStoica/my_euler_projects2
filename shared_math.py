
# Daylan Stoica
# @DaylanDStoica
# 14 August 2022
#

# math functions for various computations

'''math computation header
gather prime factor list'''


from math import sqrt, ceil
def is_prime(number):
    ''' check that the number is prime, return True if prime'''
    # check that number is an integer
    if type(number) != int:
        if int(number) == number: #converting into integer is acceptable
            number = int(number)
            # for x in range(2, ceil( sqrt(number) )):
            #     print(f" {number}/{x} ")
            #     if number % x == 0:
            #         print(f"     {number} is not prime")
            #     else:

                    
        else: #number is not an integer
            print(f"cannot check that non-integer {number} is a prime. Assumed False")
            return False

    if number <= 1: #1 is not prime, 0 is not prime, negative numbers not prime
        return False
    elif number == 2:
        return True
    elif number == 3:
        return True
    result = True
    for x in range(2, ceil( sqrt(number) )+1):
    # for x in range(2, ceil( number/2) + 1):
        if x > number:
            break
        # print(f" {number}/{x} ")
        if number % x == 0:  # not prime
            # print(f"     {number} is not prime")
            result = False
            break
        else: #is prime
            # print(f"{x:6} is not factor of    {number:12}")
            continue

    return result


def build_prime_list(number):
    ''' compile list of primes for the number'''
    prime_list = []
    if is_prime(number):
        prime_list.append(number)
        return prime_list
    temp_num = number
    for x in range(2, ceil(sqrt(number)) +1): 
    # for x in range(2, ceil( number / 2) + 1):
        if is_prime(x): #if the number is prime
            while temp_num % x == 0: 
                # while the temp_num is divisible by x
                temp_num /= x
                prime_list.append(x) # add the x to list 
    # print("primelist: ", prime_list )
    # if is_prime(number): # if the starting number is a prime, include in the list
    #     prime_list.append(number)
    return prime_list

# print( build_prime_list(23) )
# build_prime_list(23)

def build_prime_dicbuilt(number):
    '''build dictionary of primes for the number'''
    prime_list = build_prime_list(number)
    prime_dict = {}
    for x in prime_list : 
        if x not in prime_dict.keys():
            prime_dict[x] = 0
        prime_dict[x] += 1

    return prime_dict

# for x in range(10):
#     # print(f" {x} prime_list {build_prime_list(x)}")
#     prime_list = build_prime_list(x)
#     print(f"{x:5} prime_list  {prime_list}")
#     prime_dict = build_prime_dict(x)
#     for k,v in prime_dict.items():
#         print(f"    {k:4} shows up {v:3} times as a factor for {x:3}")


def is_pandigital(n = 10):
    '''check that the number is pandigital
    length 10, has all of 0-9
    return boolean'''
    number = int(number)
    str_num = str(number)
    # if number >= 10**8 and len(str_num) == 10 and number <= 10**10:
    #     # 0123456789 - 9876543210
    #     print("10**")
    # else:
    #     return False
    if number < 10**8 or number > 10**10:
        # number either has too low or too high value to be possible
        return False

    if len(str_num) == 9:
        # because 0 is not persisted in leading number for int
        # restore the 0 in string form at the front
        str_num = '0' + str_num

    # digit_list = digit_nums
    held_digits = []
    for c in str_num:
        # go through the digits of the number
        # checking off the numbers as they are encountered, pop
        # if not c in digit_list:
        #     # c digit was already encountered, cannot do twice
        #     return False
        # else:
        #     digit_list.remove(c) 
        if c in held_digits:
            # digit c is already encountered
            return False
        else:
            held_digits.append(c)

def build_factor_list ( number):
    '''build and return a list of factors for a given integer'''
    factor_list = []
    for x in range(number+1):
        if number % x == 0:
            factor_list.append(x)
    return factor_list 