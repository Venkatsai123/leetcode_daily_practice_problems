class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        ans = []
        for j in range(n):
            ans1 = []
            for i in range(m):
                ans1.append(matrix[i][j])
            ans.append(ans1)
        return ans
