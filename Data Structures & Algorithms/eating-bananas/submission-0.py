class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #num_piles
        # h is number of hours you get to eat it all

        k_min = 1
        k_max = max(piles)
        while k_min <= k_max:
            #compute how long itd take to eat
            k = ((k_max - k_min) // 2) + k_min

            time = 0
            for banana in piles:
                time += -(-banana // k)
            #if not move on
            #if yes try a smaller val, if no skip
            
            if time > h :
                #try bigger k
                k_min = k + 1
            else: #update_kmax
                k_max = k - 1

        return k_min

    

        