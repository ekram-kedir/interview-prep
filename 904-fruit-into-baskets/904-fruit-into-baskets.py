class Solution:
    def totalFruit(self, fruit: List[int]) -> int:
            begin=0
            end=0
            window=0
            ws={}
            while end<len(fruit):
                ws[fruit[end]]=end
                if len(ws)>= 3:
                    val=min(ws.values())
                    del ws[fruit[val]]
                    begin=val+1
                window=max(window,end-begin+1)
                end+=1
            return window