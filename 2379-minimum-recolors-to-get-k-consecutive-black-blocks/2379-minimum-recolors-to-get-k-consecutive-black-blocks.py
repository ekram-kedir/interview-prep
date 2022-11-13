class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0 
        r = k-1
        block = 0
        min_block = k 
        while r < len(blocks):
            count = Counter(blocks[l:r+1]) 
            if "W" in count:
                block = count["W"]
            min_block = min(min_block , block) 
            l += 1
            r += 1
            block = 0
        return min_block
