from datetime import datetime
from collections import defaultdict
import pandas as pd

class card:
    '''
    Contains base card class attribute and methods
        
        Attributes:
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
            
        Methods:
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
    '''

    def __init__(self, acct_no, acct_title, card_no, pin_entered, amount = 0):
        '''
        Parameters
        ----------
        acct_title : str
            the name of the account holder
        acct_no : int
            account number associated with the card
        card_no : int
            card number
        pin_entered : int
            card pin number
        amount : int/float (optional)
            initial deposit into the account
        
        Raises
        ------
        NotImplementedError
            When account number/title, card number/pin are not provided.
        '''
        if (acct_no is None) | (acct_title is None) | (card_no is None) | (pin_entered is None):
            raise NotImplementedError("Please provide correct details to create a bank card")
        
        self.acct_title = acct_title
        self.acct_no = acct_no
        self.card_no = card_no
        self.__card_pin = pin_entered
        self.bal_curr = amount
        # Initialize balance records
        self.trans_hist = defaultdict(dict)
        self.trans_hist[datetime.now().strftime("%Y/%m/%d, %H:%M:%S")]= [amount, 'Initialized Account']
        
             
    def makePayment(self, pin_entered, amount, srvc_point="Unknown"):
        '''
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

        if amount > self.bal_curr:
            print("You do not have enough funds to withdraw {:.2f}.\n".format(amount))
        else:
            self.bal_curr -= amount
            print("${:.2f} has been withdrawn from card no. {} at {}.".format(amount, self.card_no, srvc_point))
            print("Remaining balance: ${:.2f}.\n".format(self.bal_curr))
            self.trans_hist[timestamp]= [-amount, srvc_point]


    def checkCode(self, pin_entered):
        '''
        INTERNAL FUNCTION
        Checks if the input pin is correct

        Parameters:
        ----------
        pin_entered : int. Must be four digits
        returns : True or False
        '''
        return self.__card_pin == pin_entered


    def changePIN(self, oldPIN, newPIN):
        '''
        Sets a new PIN for the card, requires old PIN.

        Parameters:
        ----------
        oldPIN : int. Must be four digits
        newPIN : int. Must be four digits
        returns : Status, True or False
        '''
        # Customer Authentication
        if (oldPIN is None) | (not self.checkCode(oldPIN)):
            print("Invalid pin code, please try again!")
            return
        else:
            self.__card_pin = newPIN
            print("Card pin code successfully changed!")
        return


    def checkBalance(self, pin_entered):
        '''
        Prints card holder, card account number and current balance

        Parameters:
        ----------
        pin_entered : int. Must be four digits
        returns : int, returns current account balance
        '''

        # Customer Authentication
        if (pin_entered is None) | (not self.checkCode(pin_entered)):
            print("Invalid pin code, please try again!")
            return
        else:
            print("Account Holder: {}".format(self.acct_title))
            print("Card Number: {}".format(self.card_no))
            print("Current Balance: ${:.2f}".format(self.bal_curr))
        return


    def checkTransactions(self, pin_entered):
        '''
        Prints summary information for the card balance.
        Parameters:
        ----------
        pin_entered : int. Must be four digits
        returns : none
        '''

        # Customer Authentication
        if (pin_entered is None) | (not self.checkCode(pin_entered)):
            print("Invalid pin code, please try again!")
            return
        else:
            print("Account Holder: {}".format(self.acct_title))
            print("Current Balance: ${:.2f}".format(self.bal_curr))
            print("Your balance history for the past transcations:\n")
            
            df = pd.DataFrame(self.trans_hist, index=['Amount', 'Card Service Point']).T
            print(df)