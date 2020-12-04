from datetime import datetime
from . import card as cc


class credit(cc.card):
    __manager_pwd = 7777
    '''
    Contains credit card class attributes and methods
        
        Base Class Attributes:
        -----------
        acct_title : str
            the name of the account holder
        acct_no : int
            account number associated with the card
        card_no : int
            card number
        card_pin : int
            card pin number
        bal_curr : int/float
            current balance of the account
        trans_hist: dictionary with datetime(keys): transaction details(values)
            time/transaction history of account (past 30 transactions)
            
        Credit Card Class Attributes:
        -----------
        credit_limit : int
            card maximum credit limit allowed        
        interest_rate : int
            interest percent accrued on the credit amount   

        Base Class Methods:
        --------
        makePayment
            Withdraws money from the card and prints new account balance. 
        
        checkCode - INTERNAL FUNCTION
            Checks if the input pin is correct

        changePIN
            Sets a new PIN for the card, requires old PIN.

        checkBalance
            Prints card holder, card account number and current balance
                    
        checkTransactions
            Prints summary information as well as graph of past 30 changes to your account balance.

        Credit Card Class Methods:
        --------
        setCreditLimit
            Set maximum limit for the credit taken from the account.     

        checkCreditLimit
            Check maximum limit for the credit taken from the account.     

        
    '''


    def __init__(self, acct_no, acct_title, card_no, card_pin, amount = 0, credit_limit = 0, interest_rate = 0):
        '''
        Parameters
        ----------
        credit_limit : int
            card maximum credit limit allowed        
        interest_rate : int
            interest percent accrued on the credit amount   
        '''
        cc.card.__init__(self, acct_no, acct_title, card_no, card_pin, amount)

        self.credit_limit = credit_limit
        self.interest_rate = interest_rate        

                
    def setCreditLimit(self, pin_entered, mgr_code_entered, newlim = 0):
        '''
        Changes the credit maximum limit of the card.
            
            Parameters:
            -----------
            newlim : int/float. 
                Must be positive number
            pin_entered : int. 
                Must be four digits   
            mgr_code_entered: int. 
                Branch Manager Code (same for all objects). Only manager allowed to alter credit limit.
        '''
        # Manager Authentication
        if (mgr_code_entered is None)|(mgr_code_entered != credit.__manager_pwd):
            print("Unauthorized access. Only branch manager can alter the credit limit!")
            return

        # Customer Authentication
        if (pin_entered is None) | (not self.checkCode(pin_entered)):
            print("Invalid pin code, please try again!")
            return
        else:
            print("Account Holder: {}".format(self.acct_title))
            print("Card Number: {}".format(self.card_no))
            print("Current Balance: ${:.2f}".format(self.bal_curr))

        if (newlim is None) | (newlim < 0):
            print("Card credit limit must be positive.\n")
            return
        
        if self.credit_limit < newlim:
            print("Your transaction limit has increased from ${:.2f} to ${:.2f}.\n".format(self.credit_limit,newlim))
            self.credit_limit = newlim
        elif self.credit_limit > newlim:
            print("Your transaction limit has decreased from ${:.2f} to ${:.2f}.\n".format(self.credit_limit,newlim))
            self.credit_limit = newlim
        else:
            print("Your transaction limit is already ${:.2f}.\n".format(self.credit_limit))


    def checkCreditLimit(self, pin_entered):
        '''
        Check the credit maximum limit of the card.
            
            Parameters:
            -----------
            pin_entered : int. 
                Must be four digits 
        '''

        # Customer Authentication
        if (pin_entered is None) | (not self.checkCode(pin_entered)):
            print("Invalid pin code, please try again!")
        else:
            print("Your card credit limit is ${:.2f}.\n".format(self.credit_limit))


    def makePayment(self, pin_entered, amount, srvc_point="Unknown"):
        '''
        OVERLOADED METHOD FROM BASE CLASS
        Make purchase payment at service point and print new account balance. 
         
        Parameters:
        ----------
        pin_entered : int
            card pin number
        amount : int/float
            charged amount (Must be positive number)
        srvc_point: string
            service point where payment was made
        '''
        # Customer Authentication
        if (pin_entered is None) | (not self.checkCode(pin_entered)):
            print("Invalid pin code, please try again!")
            return
        
        if (amount is None) | (amount <= 0):
            print("Invalid amount entered")
            return

        timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

        if amount > self.bal_curr + self.credit_limit:
            print("Your withdrawl amount {:.2f} is over your credit limit of ${}.\n".format(amount, self.credit_limit))
            print("Available balance: ${:.2f}.\n".format(self.bal_curr))
        else:
            self.bal_curr = self.bal_curr - amount
            print("${:.2f} has been withdrawn from card no. {} at {}.".format(amount, self.card_no, srvc_point))
            print("Available balance: ${:.2f}.\n".format(self.bal_curr))
            self.trans_hist[timestamp]= [-amount, srvc_point]
