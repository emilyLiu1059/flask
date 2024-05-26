class Account : 
  def __init__(self, owner, balance = 0):
    self.owner = owner
    self.balance = balance
  
  def __repr__(self):
    return f"Account Owner: {self.owner}, Balance: {self.balance}"
  
  def deposit(self, dep_amt):
    self.balance = self.balance + dep_amt
    print("Deposit was accepted!")

  def withdraw(self, wd_amt):
    if self.balance >= wd_amt:
      self.balance = self.balance - wd_amt
      print("Withdrawal successful!")
    else:
      print("Funds not available.")

acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)