class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        # indirect = [len(ingredients[i] )for i in range(len(ingredients))]
        for row in range(len(ingredients)):
            for col in ingredients[row]:
                graph[col].append(recipes[row])
                indegree[recipes[row]] += 1

        queue = deque(supplies)
        recipes = set(recipes)

        ans = []
        while queue:
            val = queue.popleft()
            if val in recipes:
                ans.append(val)
            
            for item in graph[val]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
        
        return ans