# solution 1. using dict
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = '#'
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

    ################################################################################
    
    
    # solution 2. using 2 sets
    class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # s1 is words set
        self.s1 = set()
        # s2 is prefix set
        self.s2 = set()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.s1.add(word)
        for i in range(1, len(word)+1):
            self.s2.add(word[:i])
        
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.s1
 

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.s2
