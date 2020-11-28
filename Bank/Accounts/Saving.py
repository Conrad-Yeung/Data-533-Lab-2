from . import Account as ac
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Saving(ac.Account):
    def __init__(self,name,amount=0,maxlimit = 1000,intrate=0):
        ac.Account.__init__(self,name,amount)
        self.trans_lim = maxlimit
        self.actype = "Savings"
        self.intrate = intrate
        self.fixed_amount = 0
        self.datestart = 0
        self.dateend = 0
        self.fix_dep_inprocess = 0
                                                   
    def setfixdeposit(self,amount,intrate=0.01,test=False):
        if test == True:
            self.dateend = datetime.now()

        if self.fix_dep_inprocess == 1 and datetime.now().strftime("%Y/%m/%d") == self.dateend.strftime("%Y/%m/%d"): #Have fixed deposit created - lockin = OVER
            print("Your fixed depot created on {} is complete.".format(self.datestart.strftime("%Y/%m/%d")))
            self.deposit(self.fixed_amount+(self.fixed_amount*self.intrate))
            self.fix_dep_inprocess = 0
            self.datestart = 0
            self.dateend = 0
        elif self.fix_dep_inprocess == 1 and datetime.now().strftime("%Y/%m/%d") != self.dateend.strftime("%Y/%m/%d"):
            print("You already have a fixed deposit in process. The current amount locked in is ${:.2f} at a rate of {:.2f}. The amount will be made available on {}.".format(self.fixed_amount,self.intrate*100,self.dateend.strftime("%Y/%m/%d")))
            return 
        elif self.fix_dep_inprocess == 0: #Creation - no current fixed deposit therefore initialize
            self.datestart = datetime.now()
            self.dateend = self.datestart + relativedelta(years=1)
            self.fix_dep_inprocess = 1
            self.fixed_amount = amount
            self.intrate = intrate
            print("Your deposit of ${:.2f} has been fixed for a year with an interest rate of {:.2f}%.".format(self.fixed_amount,self.intrate*100))
            print("On {}, ${} will be added to your Savings account.".format(self.dateend.strftime("%Y/%m/%d"),self.fixed_amount+(self.fixed_amount*self.intrate)))   

    def change_lim(self,newlim):
        if self.trans_lim > newlim:
            print("Your transaction limit has increased from ${:.2f} to ${:.2f}.".format(self.trans_lim,newlim))
            self.trans_lim = newlim
        elif self.trans_lim < newlim:
            print("Your transaction limit has decreased from ${:.2f} to ${:.2f}.".format(self.trans_lim,newlim))
            self.trans_lim = newlim
        else:
            print("Your transaction limit is already ${:.2f}.".format(self.trans_lim))            
            
    def details(self):
        print("The account holder is: {}.".format(self.name))
        print("The account number is: {}.".format(self.ac))
        print("The account type is: {}".format(self.actype))
        print("Your current balance is: ${:.2f}.".format(self.bal))
        print("Your current transaction limit is: ${:.2f}.".format(self.trans_lim))
        print("--------------------------------------------")
        if self.fix_dep_inprocess == 0:
            print("You currently have no fixed deposits in process.")
        else:
            print("You currently have ${:.2f} fixed at an interest rate of {:.2f}%".format(self.fixed_amount,self.intrate*100))
            print("On {}, ${} will be added to your Savings account.".format(self.dateend.strftime("%Y/%m/%d"),self.fixed_amount+(self.fixed_amount*self.intrate)))   
        
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