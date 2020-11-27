from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


class Account:
    def __init__(self,name,account_number,amount=0,):
        self.name = name
        self.ac = account_number
        self.bal = amount
        self.bal_hist = [amount] #Initialize Balance History
        self.bal_time = [datetime.now().strftime("%Y/%m/%d, %H:%M:%S")] #Initialize Balance History
        self.recent_transact = []
        self.trans_time = []
        
    def deposit(self,amount=0):
        self.bal += amount
        timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        print("${:.2f} has been deposited to account {}".format(amount,self.ac))
        print("Current balance: ${:.2f}".format(self.bal))
        
        if len(self.bal_hist) < 30: #Record Balance
            self.bal_hist.append(self.bal)
            self.bal_time.append(timestamp)
        else:
            self.bal_hist.pop(0)
            self.bal_time.pop(0)
            
        if len(self.recent_transact) < 30: #Recent Transactions
            self.recent_transact.append(amount)
            self.trans_time.append(timestamp)
        else:
            self.recent_transact.pop(0)
            self.trans_time.pop(0)
             
    def withdraw(self,amount=0):
        timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        if amount > self.bal:
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
                
    def summary(self):
        print("Account Holder: {}".format(self.name))
        print("Current Balance: ${:.2f}".format(self.bal))
        print("Your balance history for the past 30 transcations:")
        
        #Create Plot of Balance
        fig,ax = plt.subplots()
        x = np.arange(1,len(self.bal_hist)+1)
        
        ax.plot(x,self.bal_hist,marker="o")
        ax.set_xticks(x)
        plt.xticks(rotation=65)
        ax.set_xticklabels(self.bal_time)
        formatter = ticker.FormatStrFormatter('$%1.2f')
        ax.yaxis.set_major_formatter(formatter)
        ax.grid()
        
        plt.title("Account balance over past 30 transactions")
        plt.xlabel("Date and time of transcation (YYYY/MM/DD HH:MM:SS)")
        plt.ylabel("Account balance")
