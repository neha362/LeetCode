# Closest Prime Numbers in Range, solved Mar 7 2025
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # initialize i, j both to the default values
        i, j = -1, -1
        # keep track of the previous prime number explored
        curr = -1
        # edge case (if i = 2, then the smallest distance between two primes is 1)
        if left <= 2 and right >= 3:
            return [2, 3]
        # the case where left < 2 and right < 3 means no primes
        elif right < 3:
            return [-1, -1]
        # for every odd number (we've eliminated the 2-case), check if the distance between 
        #the last and current primes is greater than that between i and j (if i and j are both not -1)
        # update i, j accordingly
        for a in range(left + (1 - left % 2), right + 1, 2):
            if i != -1 and j != -1 and j - i == 2:
                return [i, j]
            elif self.is_prime(a):
                if i == -1 and j == -1:
                    if curr != -1:
                        i, j = curr, a
                else:
                    print(a, curr, j, i)
                    if a - curr < j - i:
                        i, j = curr, a
                curr = a
        return [i, j]

  #helper method to determine if a is prime (checks for mod x == 0 for x between 2 and sqrt(a))
    def is_prime(self, a):
        for b in range(2, int(a**0.5) + 1):
            if a % b == 0:
                return False
        return True
