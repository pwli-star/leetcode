class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x:(x[0]*-1, x[1]))
        # print(people)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
