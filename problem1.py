"""Euler Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

import time

def check_if_multiple_of(multiple:int, number: int) -> bool:
    remainder = number % multiple
    if remainder == 0:
        return True
    else:
        return False
        
start_time = time.time() 
full_set_of_numbers:int = range(1,1000)
running_sum:int = 0

for i in full_set_of_numbers:
    if check_if_multiple_of(3,i):
        running_sum = running_sum + i
    elif check_if_multiple_of(5,i):
        running_sum = running_sum + i
    else:
        pass

print(f"Sum of numbers: {running_sum}")
end_time = time.time()
print(f"Time elapsed: {end_time-start_time} seconds")