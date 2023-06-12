class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def find(email):
            if email == parents[email]:
                return email
            parents[email] = find(parents[email]) 
            return parents[email]
        
        def union(email1, email2):
            parent1 = find(email1)
            parent2 = find(email2)
            if parent1 != parent2:
                parents[parent1] = parent2
        
        
        n = len(accounts)
        parents = {}  
        owners = {} 
        
        
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                parents[email] = email  
                owners[email] = name  
        
        for account in accounts:
            for i in range(2, len(account)):
                union(account[i], account[i - 1])
        
        
        merged_accounts = {}  
        
        for email in parents:
            parent = find(email)
            if parent in merged_accounts:
                merged_accounts[parent].append(email)
            else:
                merged_accounts[parent] = [email]
        
        
        result = []
        for parent, emails in merged_accounts.items():
            result.append([owners[parent]] + sorted(emails))
        
        return result
