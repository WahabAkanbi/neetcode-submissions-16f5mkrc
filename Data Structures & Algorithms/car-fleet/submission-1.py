class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        position_time = []

        #iterate through each car and find the relative time it takes to get there

        for index in range(len(position)):
            timeToTarget = (target - position[index]) / speed[index]
            position_time.append((position[index], timeToTarget))

        #sort all of these now by the position
        position_time = sorted(position_time)
        initial_time = 0
    
        for index in range(len(position_time) -1, -1, -1):
            #closest to target is the larget position so start backwards
            curr_car_time = position_time[index][1]
            if(curr_car_time > initial_time):
                fleet += 1
                initial_time = position_time[index][1]
        
        return fleet

