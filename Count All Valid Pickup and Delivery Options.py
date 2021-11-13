"""
Intuition 1
Assume we have already n - 1 pairs, now we need to insert the nth pair.
To insert the first element, there are n * 2 - 1 chioces of position。
To insert the second element, there are n * 2 chioces of position。
So there are (n * 2 - 1) * n * 2 permutations.
Considering that delivery(i) is always after of pickup(i), we need to divide 2.
So it's (n * 2 - 1) * n.


Intuition 2
We consider the first element in all 2n elements.
The first must be a pickup, and we have n pickups as chioce.
Its pair can be any position in the rest of n*2-1 positions.
So it's (n * 2 - 1) * n.


Intuition 3
The total number of all permutation obviously eauqls to 2n!.
For each pair, the order is determined, so we need to divide by 2.
So the final result is (2n)!/(2^n)


Complexity
For each run, Time O(N), Space O(1).
Also we can cache the result, so that O(1) amortized for each n.
But in doesn't help in case of LC.
Also we can pre calculate all results, so that we have O(N) space and O(1) time.
"""

class Solution:
    def countOrders(self, n: int) -> int:
        a = 1
        for i in range(2, n+1):
            a *= i*(2*i-1)
        return a % (10**9 + 7)
