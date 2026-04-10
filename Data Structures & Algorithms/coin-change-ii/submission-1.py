class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def recurse(current_index, current_amount):
            if(current_amount == amount):
                return 1
            if(current_amount > amount):
                return 0
            
            if(current_index >= len(coins)):
                return 0
            
            #take the path where we choose same number
            if((current_index, current_amount) not in memo):
                choose = recurse(current_index, current_amount+coins[current_index])
            
                #take path where we choose different number, current amount stays the same
                donot = recurse(current_index+1, current_amount)
                memo[(current_index, current_amount)] = choose + donot
            
            return memo[(current_index, current_amount)]


        return (recurse(0, 0))
        