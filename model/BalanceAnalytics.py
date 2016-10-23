class BalanceAnalytics:

   
    @staticmethod
    def checkBalanceAfterPurchase(price, balance):
        return balance - price

    @staticmethod
    def checkBalanceChangeEffects(price, balance):
        try:
            newBalance = BalanceAnalytics.checkBalanceAfterPurchase(price,balance)
            expenditure = balance-newBalance
            rate = expenditure*100/balance
            return {'newBalance':newBalance, 'rate': rate }
            
        except:

            return {'newBalance': 0, 'rate': 0 }
    
 
        