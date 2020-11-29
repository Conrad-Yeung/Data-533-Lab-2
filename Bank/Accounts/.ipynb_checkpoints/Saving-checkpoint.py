from datetime import datetime
from dateutil.relativedelta import relativedelta

from . import Account as ac

class Saving(ac.Account):
    '''
    Inherits from base class "account". 
        
        Attributes:
        -----------
        name : str
            the name of the account holder
        ac : int
            account number
        bal : int/float
            balance of the account
        bal_hist : list of ints/floats
            balance history of account (past 30 changes of balance)
        bal_time : list of datetime (YYYY/MM/DD HH/MM/SS)
            times of balance history
        recent_transact: 
            balance history of account (past 30 transactions)
        trans_time : list of datetime (YYYY/MM/DD HH/MM/SS)
            times of transcations
        
        trans_lim: int/float
            max transaction limit
        actype : str
            account type will always be 'Savings'
        
        intrate : float
            interest rate
        fixed_amount : int/float
            amount for set for fixed interest
        datestart : datetime 
            date amount is fixed
        dateend : datetime
            date amount is released
        fix_dep_inprocess: int
            limited to 1 fixed deposit at a time
            
        Methods:
        --------
        i) details
            Prints account holder, account number, account type, current balance, transaction limit, current amount fixed, interest rate, when it will be released and how much.
            
        ii) deposit(amount = 0)
            Deposits money into the account and prints new account balance. 
         
            Parameters:
            ----------
            amount : int/float (optional). Must be positive number.
        
        iii) withdraw(amount=0)
            Withdraws money from the account and prints new account balance. 
            
            Parameters:
            ----------
            amount : int/float (optional). Must be positive number. Must be less than current account balance. Must be less than trans_lim.
        
        iv) summary
            Prints summary information as well as graph of past 30 changes to your account balance.
        
        v) change_lim(newlim=self.trans_lim)
            Changes the transaction limit of the account.
            
            Parameters:
            -----------
            newlim : int/float. Must be positive number          
        
        vi) setfixdeposit(amount=0,intrate=self.intrate,test=False)
            Create fixed deposit or check if one is existing.
            
            Parameters:
            -----------
            amount : int/float. Must be positive number greater than 0.
            intrate : float (default = 0.01). Must be positive number greater than 0 and less than 1
            test : bool (default = False). Testing parameter for datetime variables
        '''
    def __init__(self,name,amount=0,maxlimit = 1000,intrate=0.01):
        '''
        Parameters
        ----------
        name : str
            the name of the account holder
        amount : int/float (optional)
            initial deposit into the account must be positive number.
        maxlimit: int/float (optional)
            initial withdrawl limit must be positive number.
        intrate: float (optional):
            initial interest rate. must be positive number greater than 0.
            
        Raises
        ------
        NotImplementedError
            When initial deposit, maxlimit or interest rate is less than 0. Interest rate cannot be 0.
        '''
        if amount < 0 or maxlimit < 0 or intrate <=0:
            raise NotImplementedError("Initial deposit, max limit and interest rate must be non-negative.")
        ac.Account.__init__(self,name,amount)
        self.trans_lim = maxlimit
        self.actype = "Savings"
        self.intrate = intrate
        self.fixed_amount = 0
        self.datestart = 0
        self.dateend = 0
        self.fix_dep_inprocess = 0         

    def details(self):
        '''
        Prints account holder, account number, account type, current balance, transaction limit, current amount fixed, interest rate, when it will be released and how much.
        '''
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
           
    def withdraw(self,amount=0):
        '''
        Withdraws money from the account and prints new account balance. 
            
            Parameters:
            ----------
            amount : int/float (optional). Must be positive number. Must be less than current account balance. Must be less than trans_lim.
        '''
        if amount < 0:
            print("Amount to withdraw must be greater than 0")
            return
        
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

    def change_lim(self,newlim=self.trans_lim):
        '''
        Changes the transaction limit of the account.
            
            Parameters:
            -----------
            newlim : int/float. Must be positive number
        '''
        if newlim < 0:
            print("Account limit must be greater than 0.")
            return
        
        if self.trans_lim < newlim:
            print("Your transaction limit has increased from ${:.2f} to ${:.2f}.".format(self.trans_lim,newlim))
            self.trans_lim = newlim
        elif self.trans_lim > newlim:
            print("Your transaction limit has decreased from ${:.2f} to ${:.2f}.".format(self.trans_lim,newlim))
            self.trans_lim = newlim
        else:
            print("Your transaction limit is already ${:.2f}.".format(self.trans_lim))
###        
    def setfixdeposit(self,amount=0,intrate=self.intrate,test=False):
        '''
        Create fixed deposit or check if one is existing.
            
            Parameters:
            -----------
            amount : int/float. Must be positive number greater than 0.
            intrate : float (default = 0.01). Must be positive number greater than 0.
            test : bool (default = False). Testing parameter for datetime variables.
        '''
        if test == True: #For testing purposes
            self.dateend = datetime.now()
        
        if amount <=0: 
            print("Amount for a fixed deposit must be greater than 0")
            return
        
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
