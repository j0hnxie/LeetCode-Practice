class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        memo = defaultdict(list)
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time, amount = int(time), int(amount)
            memo[time].append((name, city))

        seen = set()
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time, amount = int(time), int(amount)

            if amount > 1000:
                result.append(transaction)
                continue

            broken = False
            for possible_time in range(time - 60, time + 61):
                if possible_time not in memo:
                    continue
                
                for other_name, other_city in memo[possible_time]:
                    if other_name == name and other_city != city:
                        result.append(transaction)
                        broken = True
                        break
                
                if broken:
                    break
            
        return result

    #     class Solution:
    # def invalidTransactions(self, transactions: List[str]) -> List[str]:
    #     result = []
    #     memo = {}
    #     for transaction in transactions:
    #         name, time, amount, city = transaction.split(",")
    #         time, amount = int(time), int(amount)

    #     seen = set()
    #     for transaction in transactions:
    #         name, time, amount, city = transaction.split(",")
    #         time, amount = int(time), int(amount)

    #         if amount > 1000:
    #             result.append(transaction)
    #             continue

    #         broke = False
    #         for possible_time in range(time - 60, time + 61):
    #             if possible_time not in memo:
    #                 continue
                
    #             other_name, other_city, other_amount = memo[possible_time]
    #             if other_name == name and other_city != city:
    #                 result.append(transaction)
    #                 result.append(other_name + "," + str(possible_time) + "," + str(other_amount) + "," + other_city)
    #                 del memo[possible_time]
    #                 broke = True
                    
    #                 break

    #         if not broke:
    #             memo[time] = (name, city, amount)
            
    #     return result