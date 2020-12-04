from datetime import datetime
from collections import defaultdict
import pandas as pd

class Card:
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

    def __init__(self, acct_no, acct_title, card_no, card_pin, amount = 0):
        '''
        Parameters
        ----------
        acct_title : str
            the name of the account holder
        acct_no : int
            account number associated with the card
        card_no : int
            card number
        card_pin : int
            card pin number
        amount : int/float (optional)
            initial deposit into the account
        
        Raises
        ------
        NotImplementedError
            When account number/title, card number/pin are not provided.
        '''
        if (acct_no is None) | (acct_title is None) | (card_no is None) | (card_pin is None):
            raise NotImplementedError("Please provide correct details to create a bank card")
        
        self.acct_title = acct_title
        self.acct_no = acct_no
        self.card_no = card_no
        self.card_pin = card_pin
        self.bal_curr = amount
        # Initialize balance records
        self.trans_hist = defaultdict(dict)
        self.trans_hist[datetime.now().strftime("%Y/%m/%d, %H:%M:%S")]= [amount, 'Initialized Account']
        
             
    def makePayment(self, card_no, card_pin, amount, srvc_point="Unknown"):
        '''
        Make purchase payment at service point and print new account balance. 
         
        Parameters:
        ----------
        card_no : int
            card number
        card_pin : int
            card pin number
        amount : int/float
            charged amount (Must be positive number)
        srvc_point: string
            service point where payment was made
        '''
        # Authentication
        if (card_no is None) | (card_pin is None):
            print("Invalid card or pin Number, please contact your bank.")
            return
        elif (amount is None) | (amount <= 0):
            print("Invalid amount entered")
            return

        timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        if amount > self.bal_curr:
            print("You do not have enough funds to withdraw {:.2f}.\n".format(amount))
        else:
            self.bal_curr -= amount
            print("${:.2f} has been withdrawn from card no. {} at {}.".format(amount, card_no, srvc_point))
            print("Remaining balance: ${:.2f}.\n".format(self.bal_curr))
            self.trans_hist[timestamp]= [-amount, srvc_point]


    def checkCode(self, oldPIN):
        '''
        INTERNAL FUNCTION
        Checks if the input pin is correct

        Parameters:
        ----------
        oldPIN : int. Must be four digits
        returns : True or False
        '''
        return self.card_pin == oldPIN


    def changePIN(self, oldPIN, newPIN):
        '''
        Sets a new PIN for the card, requires old PIN.

        Parameters:
        ----------
        oldPIN : int. Must be four digits
        newPIN : int. Must be four digits
        returns : Status, True or False
        '''
        if not self.checkCode(oldPIN):
            print("Invalid pin code, please try again!")
        else:
            self.card_pin = newPIN
            print("Card pin code successfully changed!")
        return


    def checkBalance(self, card_no, card_pin):
        '''
        Prints card holder, card account number and current balance

        Parameters:
        ----------
        card_no : int. Must be four digits
        card_pin : int. Must be four digits
        returns : int, returns current account balance
        '''
        if not self.checkCode(card_pin):
            print("Invalid pin code, please try again!")
        else:
            print("Account Holder: {}".format(self.acct_title))
            print("Card Number: {}".format(self.card_no))
            print("Current Balance: ${:.2f}".format(self.bal_curr))
        return



    def checkTransactions(self, card_no, card_pin):
        '''
        Prints summary information as well as graph of past 30 changes to your account balance.
        '''
        print("Account Holder: {}".format(self.acct_title))
        print("Current Balance: ${:.2f}".format(self.bal_curr))
        print("Your balance history for the past 30 transcations:\n")
        
        df = pd.DataFrame(self.trans_hist, index=['Amount', 'Card Service Point']).T
        print(df)