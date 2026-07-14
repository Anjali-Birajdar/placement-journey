import math
from collections import Counter


class Solution:
    def minAnagramLength(self, s):
        n = len(s)
        factors = []

        # Find the factors of the length of the string
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                k = n // i
                if k != i:
                    factors.append(i)
                    factors.append(k)
                else:
                    factors.append(i)

        factors.sort()  # Sort the factors in ascending order

        for factor in factors:
            # Count the frequency of characters in the first segment
            first_segment_freq = Counter(s[:factor])

            is_anagramic = True

            # Check if the rest of the segments have the same character frequency
            for i in range(factor, n, factor):
                segment_freq = Counter(s[i:i + factor])
                if first_segment_freq != segment_freq:
                    is_anagramic = False
                    break

            if is_anagramic:
                return factor

        return n
