class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}

        for index in range(numCourses):
            graph[index] = []        

        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        visiting = set()
        visited = set()
        output = []


        def recurse(index):

            if(index in visiting):
                return False

            if(index in visited):
                return True


            visiting.add(index)

            for prereq in graph[index]:
                cycle_detect = recurse(prereq)
                if(not cycle_detect):
                    return False

            
            visiting.remove(index)
            output.append(index)
            visited.add(index)

            return True 
        result = True
        for index in range(numCourses):
            result &= recurse(index)
        
        if(not result):
            return []
        else:
            return output



        