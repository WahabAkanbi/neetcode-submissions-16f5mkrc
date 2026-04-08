class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tabulate = {}
        #imagine a point at the end of cost array
        def min_recurse(index):
            if(index == 0 or index == 1):
                return 0
            if(index not in tabulate):
                one_step = min_recurse(index-1)  + cost[index-1]
                two_step = min_recurse(index-2) + cost[index -2]
                tabulate[index]= min(one_step, two_step)

            return tabulate[index]

        min_cost = min_recurse(len(cost))#technically last index
        return min_cost

        