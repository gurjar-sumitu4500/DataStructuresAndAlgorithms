class Solution:
    def toh(self, N, from_rod, to_rod, aux_rod):
        count = 0

        def tower(n, from_rod, to_rod, aux_rod):
            nonlocal count
            if n == 1:
                step(n, from_rod, to_rod)
                return count
            tower(n - 1, from_rod, aux_rod, to_rod)
            step(n, from_rod, to_rod)
            tower(n - 1, aux_rod, to_rod, from_rod)
            return count

        def step(n, from_rod, to_rod):
            nonlocal count
            print("move disk {} from rod {} to rod {}".format(n, from_rod, to_rod))
            count += 1

        return tower(N, from_rod, to_rod, aux_rod)
