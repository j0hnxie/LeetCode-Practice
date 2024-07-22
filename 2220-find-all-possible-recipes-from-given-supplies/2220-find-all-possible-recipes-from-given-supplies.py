class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_list = {}
        supplies = set(supplies)
        n = len(recipes)
        indegrees = {}

        print(n)
        for idx in range(n):
            recipe = recipes[idx]
            ingredient_list = ingredients[idx]
            for ingredient in ingredient_list:
                if ingredient not in supplies:
                    cur_ingredients = adj_list.get(ingredient, [])
                    cur_ingredients.append(recipe)
                    adj_list[ingredient] = cur_ingredients
                    indegrees[recipe] = indegrees.get(recipe, 0) + 1
        
        queue = deque()
        for recipe in recipes:
            if indegrees.get(recipe, 0) == 0:
                queue.append(recipe)
        
        res = []
        while queue:
            cur_recipe = queue.popleft()
            res.append(cur_recipe)

            neighbor_recipes = adj_list.get(cur_recipe, [])
            for neighbor_recipe in neighbor_recipes:
                indegrees[neighbor_recipe] = indegrees.get(neighbor_recipe, 0) - 1
                if indegrees[neighbor_recipe] == 0:
                    queue.append(neighbor_recipe)

        return res


        
            
        
