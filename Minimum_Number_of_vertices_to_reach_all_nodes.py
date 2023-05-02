class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        source = set()
        destination = set()
        for row in edges:
            source.add(row[0])
            destination.add(row[1])
        ans = []
        return source-destination
