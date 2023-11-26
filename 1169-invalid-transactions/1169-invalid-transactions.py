class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        answer = []
        self.storeValue = defaultdict(list)
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            self.storeValue[name].append([time,amount,city])
        
        for index in range(len(transactions)):
            name, time, amount, city = transactions[index].split(",")
            if int(amount) > 1000:
                answer.append(transactions[index])
            else:
                for transaction in self.storeValue[name]:
                    time_i, amount_i , city_i = transaction
                    if city != city_i and abs(int(time) - int(time_i)) <= 60:
                        answer.append(transactions[index])
                        break

        return answer