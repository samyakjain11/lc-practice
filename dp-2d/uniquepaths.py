# class Solution:
def uniquePaths( m: int, n: int) -> int:
    # you can go down and right for each thing
    # recursive function definition:
    # if inside bounds: cur_unique_paths = uniquePaths(down) + uniquePaths(right)
    # else return 0
    def recursive_subproblem(x: int, y:int):
        if x >= 0 and x < m - 1 and y >= 0 and y < n - 1:
            return recursive_subproblem(x + 1, y) + recursive_subproblem(x, y + 1)
        if x == m and y == n:
            return 1
        else:
            return 0  

    memoized = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # print(memoized)
    for x in reversed(range(m)):
        for y in reversed(range(n)):
            if  x == m - 1 and y == n - 1:
                memoized[x][y] = 1
            elif x >= 0 and x < m and y >= 0 and y < n:
                memoized[x][y] = memoized[x + 1][y] + memoized[x][y + 1]

    return memoized[0][0]

ret = uniquePaths(3, 7)
print(ret)

