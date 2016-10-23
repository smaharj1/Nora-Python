class BalanceAnalytics:

   
    @staticmethod
    def checkBalanceAfterPurchase(items,balance):
        finalBalance = balance
        for i in items:
            finalBalance = finalBalance - i['price']
        return finalBalance 

    @staticmethod
    def checkBalanceChangeEffects(items, balance):
        newBalance = self.checkBalanceAfterPurchase(items,balance)
        expenditure = balance-newBalance
        rate = expenditure*100/balance
        return {'newBalance':newBalance,
                'rate': rate 
                }
    
 
        