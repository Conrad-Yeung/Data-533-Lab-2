# Data-533-Lab-2

Group: Conrad Yeung and Aamir Khan  

Package: Bank  

Sub-packages: accounts and cards

Description:  
This package can be used to manage bank customers. There are two subpackages accounts and cards. Accounts subpackage is for corporate customers using bank for large transactions. Cards subpackage is for retail customers who would like to use their bank account with card transactions.

Package Usage:  
The main folder contains two jupyter notebooks `Test_Account.ipynb` and `Test_Card.ipynb` that have the code showing interaction with the package modules.  

1) Account modules:  
a) Base Account class:  
        i) Deposit  
        ii) Withdraw  
        iii) Summary  
b) Savings (inherits Base) class:  
        i) Inherits – Deposit, Withdraw, Summary  
        ii) Set Max Withdrawal for Savings  
        iii) Interest Rate (show interest rate)  
c) Chequings (inherits Base) class:  
        i) Inherits – Deposit, Withdraw, Summary
        ii) Set Max Withdrawal for Chequings
        
2) cards modules:  

a) card (base) class:  

- makePayment (ABSTRACT)  
    Withdraws money from the card and prints new account balance.  
    Payment will be specific to the card type.  
    Sub-classes credit and debit implement this function  
        
- checkCode (INTERNAL FUNCTION)  
    Checks if the entered PIN code is correct  

- changePIN  
    Sets a new PIN for the card, requires old PIN.  

- checkBalance  
    Prints card holder, card account number and current balance  

- checkTransactions  
    Prints summary information of past transactions.  

b) credit (inherits card) class:  

- Inherits – makePayment, changePIN, checkBalance and checkTransactions  

- setCreditLimit  
    Set maximum limit for the credit taken from the account.     

- checkCreditLimit  
    Check maximum limit for the credit taken from the account.    

- setInterestRate  
    Changes the credit card interest rate  

- checkInterestRate  
    Check the credit card interest rate  

- makePayment (OVERLOADED)  
    Make purchase payment at service point and print new account balance.  

- checkTransactions (OVERLOADED)  
    Prints summary information for the credit card balance.  

c) debit (inherits card) class:  

- Inherits – makePayment, changePIN, checkBalance and checkTransactions   

- setTransactionLimit  
    Set maximum limit for the daily amount withdrawn from the account.     

- checkTransactionLimit  
    Check maximum limit for the daily amount withdrawn from the account.         

- changeCardType  
    Changes the type of the card to one of diamond, gold or platinum   

- checkCardType  
    Displays the type of the debit card.    

- makePayment (OVERLOADED)  
    Make purchase payment at service point and print new account balance.   
