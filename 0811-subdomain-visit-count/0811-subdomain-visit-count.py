class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp = defaultdict(int)
        
        for cpdomain in cpdomains:
            website = cpdomain.split(" ")
            freq = int(website[0])
            domains = website[1]
            
            websiteDomain = ""
            for domain in domains.split(".")[::-1]:
                if websiteDomain == "":
                    websiteDomain = domain
                else:
                    websiteDomain = domain + "." + websiteDomain
                cp[websiteDomain] += freq
        answer = []
        
        for key in cp.keys():
            answer.append(str(cp[key]) + " " + key)
        return answer
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        k = []
        k1 = []
        res = []
        j = []
        d = {}
        for i in range(len(cpdomains)):
            k.append(cpdomains[i].split())
        for i in range(len(k)):
            k1.append([k[i][0],k[i][1].split(sep = ".")])
        
        for i in range(len(k1)):
            res.append(".".join(k1[i][1][0:]))
            res.append(".".join(k1[i][1][1:]))
            res.append(k1[i][1][-1])
        print(res)
        
            
       