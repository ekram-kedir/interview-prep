class Solution:
    def compress(self, chars: List[str]) -> int:
        count,l,r=0,0,0
        ans=[]
        while r<len(chars):
            if chars[l]==chars[r]:
                count+=1
                r+=1
            if r==len(chars) or chars[l]!=chars[r]:
                ans.append(str(chars[l]))
                if 1<count<10:
                    ans.append(str(count))
                elif count>=10:
                    count = str(count)
                    n = 0
                    while n < len(count):
                        ans.append(str(count[n]))
                        n += 1
                count = 0
                l = r
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)
                