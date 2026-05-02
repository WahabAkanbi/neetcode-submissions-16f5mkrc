class charNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.head = charNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = charNode()
            curr = curr.children[char]
        curr.end = True #end of the word

        # root-> A->D->D
        # root ->B -> A->D
        #(0, root) (1, A), (2, D), (3, D)
        
    def search(self, word: str) -> bool:
        
        def dfs(curr_index, curr):
            if(curr_index == len(word)):
                return curr.end #makes sense we return if last element is T/F

            leads_end = False
            curr_letter = word[curr_index]

            if(curr_letter in curr.children):
                leads_end |= dfs(curr_index+1, curr.children[curr_letter])
            elif(curr_letter == "."):
                #try every children
                for key, value in curr.children.items():
                    leads_end |= dfs(curr_index+1, value)  
            else:
                return False
            
            return leads_end
                    
        curr = self.head
        #the goal is to run DFS Algo starting at index 0 and seeing if we can get all the way to the end
        return dfs(0, curr)

        
