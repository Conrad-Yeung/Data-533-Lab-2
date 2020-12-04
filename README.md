# Data-533-Lab-2

Group: Conrad Yeung and Aamir Khan  
Package: Bank  
Sub-packages: accounts and cards

1) account modules:  
a) account (base) class:  
        i) Deposit  
        ii) Withdraw  
        iii) Summary  
b) savings (inherits base) class:  
        i) Inherits – Deposit, Withdraw, Summary  
        ii) Set Max Withdrawal for Savings  
        iii) Interest Rate (show interest rate)  
c) chequings (inherits base) class:  
        i) Inherits – Deposit, Withdraw, Summary
        ii) Set Max Withdrawal for Chequings
        
2) cards modules:  
a) card (base) class:  
        i) makePayment  
        ii) changePIN  
        iii) checkBalance  
        iv) checkTransactions  
        v) makePayment (ABSTRACT)  
b) credit (inherits card) class:    
        i) Inherits – makePayment, changePIN, checkBalance and checkTransactions  
        ii) setCreditLimit  
        iii) checkCreditLimit  
        iv) makePayment (OVERLOADED)  
        v) checkTransactions (OVERLOADED)  
c) debit (inherits card) class:    
        i) Inherits – makePayment, changePIN, checkBalance and checkTransactions    
        ii) setTransactionLimit    
        iii) checkTransactionLimit  
        iv) changeCardType  
        v) checkCardType  
        vi) makePayment (OVERLOADED)  
  
Key Functions:
1)	Deposit:  Money goes into account
2)	Withdraw: Money leaves account  
a)	Pay – Money leaves account
3)	Summary: Balance, Past 10 transactions
4)	Set Max …: Max withdrawal amount per transaction
a)	Set Credit/Transaction Limit: Max withdrawal amount per transaction
5)	Interest Rate – Show current interest rate
6)	Type of Card: Debit Card Details (Type of Card, Max Transaction Limit, Owner Name)

