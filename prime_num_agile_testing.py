# Agile testing script (Demo)
'''Check if num is prime or not.
Develop a command-line application that accepts any positive integer, n, where 0<=n<=1,000, and determine whether it is a prime
number. If n is a prime number, then return message stating prime number. If n is not a prime number, then return message stating "Not prime number".
If n is not a valid input, then the application should display a help message.

Test cases
case#  Input  Expected  Comments
               Output
  1      3    True      Tests within boundaries
  2    1000   False     Tests equal to upper bound
  3      0    False     Tests equal to lower bound
  4     -1    None      Tests below lower bound
  5    1001   None      Tests above upper bound
  6     "a"   None      Tests for int datatype
  7    (5,7)  None      Tests for correct # of inputs
  8    None   None      Tests for no input
'''

import math
# is_prime is a placeholder function that you want to test
def is_prime(num):
    # not a prime >>> should return False
    if num == 0:
        return False
    # this is within the boundaries
    if num >= 0 and num <= 1000:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True
    return None

def passed(final,exp):
    count = 0
    for i in range(0,len(exp)):
        if final[i]== exp[i]:
            count+=1
    return (count/len(exp))*100
        
if __name__ == "__main__":
# driver code
    final_result = []
    exp_result = [True, False, False, None, None, None, None, None]
    # checks for prime number or not and invalid inputs
    primes = [3, 1000, 0, -1, 1001, "a", (3,4), ""]
    for prime in primes:
        try:
            final_result.append(is_prime(prime))
        except:
            final_result.append(None)

    # Did all tests pass?
    if final_result == exp_result:
        print(passed(final_result,exp_result), "% tests passed. Yippee Kaiyay :)")
    else:
        print(passed(final_result,exp_result), "% tests passed")
