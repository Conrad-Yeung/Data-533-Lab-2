from . import Account as ac
from datetime import datetime

class Chequing(ac.Account):
    def __init__(self,name,amount=0,maxlimit = 1000):
        ac.Account.__init__(self,name,amount)
        self.trans_lim = maxlimit
        self.actype = "Chequings"
    
    def details(self):
        print("The account holder is: {}.".format(self.name))
        print("The account number is: {}.".format(self.ac))
        print("The account type is: {}".format(self.actype))
        print("Your current balance is: ${:.2f}.".format(self.bal))
        print("Your current transaction limit is: ${:.2f}.".format(self.trans_lim))
    
    def change_lim(self,newlim):
        if self.trans_lim < newlim:
            print("Your transaction limit has increased from ${:.2f} to ${:.2f}.".format(self.trans_lim,newlim))
            self.trans_lim = newlim
        elif self.trans_lim > newlim:
            print("Your transaction limit has decreased from ${:.2f} to ${:.2f}.".format(self.trans_lim,newlim))
            self.trans_lim = newlim
        else:
            print("Your transaction limit is already ${:.2f}.".format(self.trans_lim))
    
    def withdraw(self,amount=0):
        timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        if amount > self.trans_lim:
            print("Your current transaction limit is ${:.2f}, therefore you are unable to withdraw the requested amount of ${:.2f}.".format(self.trans_lim,amount)) 
        elif amount > self.bal:
            print("You do not have enough funds to withdraw {:.2f}".format(amount))
        else:
            self.bal-=amount
            print("${:.2f} has been withdrawn from account {}".format(amount,self.ac))
            print("Current balance: ${:.2f}".format(self.bal))
            
            if len(self.bal_hist) < 30: #Record Balance 
                self.bal_hist.append(self.bal)
                self.bal_time.append(timestamp)
            else:
                self.bal_hist.pop(0)
                self.bal_time.pop(0)
                
            if len(self.recent_transact) < 30: #Recent Transactions
                self.recent_transact.append(-amount)
                self.trans_time.append(timestamp)
            else:
                self.recent_transact.pop(0)
                self.trans_time.pop(0)